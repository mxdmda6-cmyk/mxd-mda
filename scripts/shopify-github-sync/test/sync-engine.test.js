import assert from 'node:assert/strict';
import test from 'node:test';
import { createSyncEngine } from '../lib/sync-engine.js';

function createStateStore(initial = {}) {
  const entries = new Map(Object.entries(initial));
  return {
    get: (id) => entries.get(String(id)) ?? null,
    set: (id, value) => entries.set(String(id), value),
    remove: (id) => entries.delete(String(id)),
    entries,
  };
}

test('delete finds and removes a project item when the local cache is empty', async () => {
  const stateStore = createStateStore();
  const githubClient = {
    findItemByShopifyId: async () => ({ itemId: 'item-1', draftIssueId: 'draft-1' }),
    deleteItem: async (itemId) => assert.equal(itemId, 'item-1'),
  };
  const engine = createSyncEngine({ githubClient, stateStore });

  const result = await engine.deleteProduct('123');

  assert.equal(result.action, 'deleted');
  assert.equal(stateStore.get('123'), null);
});

test('delete treats a missing remote item as complete after an ambiguous API failure', async () => {
  const stateStore = createStateStore({
    123: { itemId: 'item-1', draftIssueId: 'draft-1' },
  });
  const githubClient = {
    deleteItem: async () => {
      throw new Error('item already deleted');
    },
    findItemByShopifyId: async () => null,
  };
  const engine = createSyncEngine({ githubClient, stateStore });

  const result = await engine.deleteProduct('123');

  assert.equal(result.action, 'deleted');
  assert.equal(stateStore.get('123'), null);
});

test('a failed update does not create a duplicate while the item still exists', async () => {
  const stateStore = createStateStore({
    123: { itemId: 'item-1', draftIssueId: 'draft-1' },
  });
  let createCalls = 0;
  const githubClient = {
    updateDraftIssue: async () => {
      const error = new Error('temporary GitHub failure');
      error.retryable = true;
      throw error;
    },
    findItemByShopifyId: async () => ({ itemId: 'item-1', draftIssueId: 'draft-1' }),
    createDraftIssue: async () => {
      createCalls++;
    },
  };
  const engine = createSyncEngine({ githubClient, stateStore });

  await assert.rejects(engine.upsertProduct({ id: 123, title: 'Product' }), {
    message: 'temporary GitHub failure',
  });
  assert.equal(createCalls, 0);
  assert.equal(stateStore.get('123').itemId, 'item-1');
});

test('a stale cache entry is recreated only after the project item is absent', async () => {
  const stateStore = createStateStore({
    123: { itemId: 'deleted-item', draftIssueId: 'deleted-draft' },
  });
  let createCalls = 0;
  const githubClient = {
    updateDraftIssue: async () => {
      throw new Error('not found');
    },
    findItemByShopifyId: async () => null,
    createDraftIssue: async () => {
      createCalls++;
      return { itemId: 'new-item', draftIssueId: 'new-draft' };
    },
    setShopifyIdField: async () => {},
  };
  const engine = createSyncEngine({ githubClient, stateStore });

  const result = await engine.upsertProduct({ id: 123, title: 'Product' });

  assert.equal(result.action, 'created');
  assert.equal(createCalls, 1);
  assert.equal(stateStore.get('123').itemId, 'new-item');
});

test('concurrent events for one product are processed in order without duplicate creation', async () => {
  const stateStore = createStateStore();
  let createCalls = 0;
  const githubClient = {
    findItemByShopifyId: async () => null,
    createDraftIssue: async () => {
      createCalls++;
      await new Promise((resolve) => setTimeout(resolve, 10));
      return { itemId: 'item-1', draftIssueId: 'draft-1' };
    },
    setShopifyIdField: async () => {},
    updateDraftIssue: async () => {},
  };
  const engine = createSyncEngine({ githubClient, stateStore });

  await Promise.all([
    engine.upsertProduct({ id: 123, title: 'First update' }),
    engine.upsertProduct({ id: 123, title: 'Second update' }),
  ]);

  assert.equal(createCalls, 1);
});
