import { logger } from './logger.js';
import { buildItemBody } from './shopify-client.js';

export function createSyncEngine({ githubClient, stateStore }) {
  const operations = new Map();

  function serialize(shopifyId, operation) {
    const key = String(shopifyId);
    const previous = operations.get(key) ?? Promise.resolve();
    const current = previous.catch(() => {}).then(operation);
    operations.set(key, current);
    current.then(
      () => {
        if (operations.get(key) === current) operations.delete(key);
      },
      () => {
        if (operations.get(key) === current) operations.delete(key);
      }
    );
    return current;
  }

  async function upsertProductInternal(product) {
    const shopifyId = String(product.id);
    const title = product.title || `Shopify product ${shopifyId}`;
    const body = buildItemBody(product);

    let entry = stateStore.get(shopifyId);

    // Cache miss (fresh state file, or item created before this process started):
    // fall back to a full-board scan keyed on the Shopify Product ID field.
    if (!entry) {
      const found = await githubClient.findItemByShopifyId(shopifyId);
      if (found) {
        entry = found;
        stateStore.set(shopifyId, entry);
      }
    }

    if (entry) {
      try {
        await githubClient.updateDraftIssue(entry.draftIssueId, { title, body });
        logger.info('Updated existing project item', { shopifyId, itemId: entry.itemId });
        return { action: 'updated', ...entry };
      } catch (err) {
        const found = await githubClient.findItemByShopifyId(shopifyId);
        if (found) {
          if (found.itemId !== entry.itemId) {
            await githubClient.updateDraftIssue(found.draftIssueId, { title, body });
            stateStore.set(shopifyId, found);
            return { action: 'updated', ...found };
          }
          throw err;
        }
        logger.warn('Project item no longer exists; recreating it', {
          shopifyId,
          error: err.message,
        });
        stateStore.remove(shopifyId);
      }
    }

    const created = await githubClient.createDraftIssue({ title, body });
    await githubClient.setShopifyIdField(created.itemId, shopifyId);
    stateStore.set(shopifyId, created);
    logger.info('Created new project item', { shopifyId, itemId: created.itemId });
    return { action: 'created', ...created };
  }

  async function deleteProductInternal(shopifyId) {
    const key = String(shopifyId);
    let entry = stateStore.get(key);
    if (!entry) {
      entry = await githubClient.findItemByShopifyId(key);
      if (!entry) {
        logger.warn('Delete requested for a product with no known project item, skipping', {
          shopifyId: key,
        });
        return { action: 'skipped' };
      }
    }
    try {
      await githubClient.deleteItem(entry.itemId);
    } catch (err) {
      const found = await githubClient.findItemByShopifyId(key);
      if (found) throw err;
    }
    stateStore.remove(key);
    logger.info('Deleted project item', { shopifyId: key, itemId: entry.itemId });
    return { action: 'deleted', ...entry };
  }

  return {
    upsertProduct: (product) => serialize(product.id, () => upsertProductInternal(product)),
    deleteProduct: (shopifyId) =>
      serialize(shopifyId, () => deleteProductInternal(shopifyId)),
  };
}
