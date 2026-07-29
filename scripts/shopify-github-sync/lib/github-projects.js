import { env } from './env.js';

const GITHUB_GRAPHQL_URL = 'https://api.github.com/graphql';
export const SHOPIFY_ID_FIELD_NAME = 'Shopify Product ID';

async function githubGraphQL(query, variables) {
  const res = await fetch(GITHUB_GRAPHQL_URL, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.GITHUB_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query, variables }),
  });

  if (res.status === 429 || res.status >= 500) {
    const err = new Error(`GitHub GraphQL transient error: HTTP ${res.status}`);
    err.retryable = true;
    throw err;
  }

  const json = await res.json();

  if (json.errors?.length) {
    const messages = json.errors.map((e) => e.message).join('; ');
    const err = new Error(`GitHub GraphQL error: ${messages}`);
    err.retryable = json.errors.some((e) => e.type === 'RATE_LIMITED');
    throw err;
  }

  return json.data;
}

const PROJECT_FIELDS_BY_ORG = `
  query($login: String!, $number: Int!) {
    organization(login: $login) {
      projectV2(number: $number) {
        id
        fields(first: 50) {
          nodes { ... on ProjectV2FieldCommon { id name } }
        }
      }
    }
  }
`;

const PROJECT_FIELDS_BY_USER = `
  query($login: String!, $number: Int!) {
    user(login: $login) {
      projectV2(number: $number) {
        id
        fields(first: 50) {
          nodes { ... on ProjectV2FieldCommon { id name } }
        }
      }
    }
  }
`;

async function resolveProject(login, number) {
  const org = await githubGraphQL(PROJECT_FIELDS_BY_ORG, { login, number });
  if (org.organization?.projectV2) return org.organization.projectV2;

  const user = await githubGraphQL(PROJECT_FIELDS_BY_USER, { login, number });
  if (user.user?.projectV2) return user.user.projectV2;

  throw new Error(`Project #${number} not found for "${login}" as an organization or a user.`);
}

const CREATE_TEXT_FIELD = `
  mutation($projectId: ID!, $name: String!) {
    createProjectV2Field(input: { projectId: $projectId, dataType: TEXT, name: $name }) {
      projectV2Field { ... on ProjectV2FieldCommon { id name } }
    }
  }
`;

async function ensureShopifyIdField(projectId, existingFields) {
  const found = existingFields.find((f) => f.name === SHOPIFY_ID_FIELD_NAME);
  if (found) return found.id;

  const data = await githubGraphQL(CREATE_TEXT_FIELD, { projectId, name: SHOPIFY_ID_FIELD_NAME });
  return data.createProjectV2Field.projectV2Field.id;
}

const CREATE_DRAFT_ISSUE = `
  mutation($projectId: ID!, $title: String!, $body: String!) {
    addProjectV2DraftIssue(input: { projectId: $projectId, title: $title, body: $body }) {
      projectItem {
        id
        content { ... on DraftIssue { id } }
      }
    }
  }
`;

const UPDATE_DRAFT_ISSUE = `
  mutation($draftIssueId: ID!, $title: String!, $body: String!) {
    updateProjectV2DraftIssue(input: { draftIssueId: $draftIssueId, title: $title, body: $body }) {
      draftIssue { id }
    }
  }
`;

const SET_TEXT_FIELD = `
  mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $value: String!) {
    updateProjectV2ItemFieldValue(input: {
      projectId: $projectId, itemId: $itemId, fieldId: $fieldId, value: { text: $value }
    }) {
      projectV2Item { id }
    }
  }
`;

const DELETE_ITEM = `
  mutation($projectId: ID!, $itemId: ID!) {
    deleteProjectV2Item(input: { projectId: $projectId, itemId: $itemId }) {
      deletedItemId
    }
  }
`;

const FIND_ITEMS_PAGE = `
  query($projectId: ID!, $after: String) {
    node(id: $projectId) {
      ... on ProjectV2 {
        items(first: 100, after: $after) {
          pageInfo { hasNextPage endCursor }
          nodes {
            id
            content { ... on DraftIssue { id } }
            fieldValueByName(name: "${SHOPIFY_ID_FIELD_NAME}") {
              ... on ProjectV2ItemFieldTextValue { text }
            }
          }
        }
      }
    }
  }
`;

export function createGithubProjectsClient() {
  let cache = null;

  async function init() {
    if (cache) return cache;
    const project = await resolveProject(env.GITHUB_PROJECT_OWNER, Number(env.GITHUB_PROJECT_NUMBER));
    const fieldId = await ensureShopifyIdField(project.id, project.fields.nodes);
    cache = { projectId: project.id, fieldId };
    return cache;
  }

  return {
    init,

    async createDraftIssue({ title, body }) {
      const { projectId } = await init();
      const data = await githubGraphQL(CREATE_DRAFT_ISSUE, { projectId, title, body });
      const item = data.addProjectV2DraftIssue.projectItem;
      return { itemId: item.id, draftIssueId: item.content.id };
    },

    async updateDraftIssue(draftIssueId, { title, body }) {
      await githubGraphQL(UPDATE_DRAFT_ISSUE, { draftIssueId, title, body });
    },

    async setShopifyIdField(itemId, shopifyId) {
      const { projectId, fieldId } = await init();
      await githubGraphQL(SET_TEXT_FIELD, { projectId, itemId, fieldId, value: String(shopifyId) });
    },

    async deleteItem(itemId) {
      const { projectId } = await init();
      await githubGraphQL(DELETE_ITEM, { projectId, itemId });
    },

    async findItemByShopifyId(shopifyId) {
      const { projectId } = await init();
      let after = null;
      do {
        const data = await githubGraphQL(FIND_ITEMS_PAGE, { projectId, after });
        const page = data.node.items;
        const match = page.nodes.find((n) => n.fieldValueByName?.text === String(shopifyId));
        if (match) return { itemId: match.id, draftIssueId: match.content?.id };
        after = page.pageInfo.hasNextPage ? page.pageInfo.endCursor : null;
      } while (after);
      return null;
    },
  };
}
