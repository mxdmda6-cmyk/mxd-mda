import { logger } from './logger.js';
import { buildItemBody } from './shopify-client.js';

export function createSyncEngine({ githubClient, stateStore }) {
  async function upsertProduct(product) {
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
        logger.warn('Update failed (item may have been removed from the board); recreating', {
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

  async function deleteProduct(shopifyId) {
    const key = String(shopifyId);
    const entry = stateStore.get(key);
    if (!entry) {
      logger.warn('Delete requested for a product with no known project item, skipping', {
        shopifyId: key,
      });
      return { action: 'skipped' };
    }
    await githubClient.deleteItem(entry.itemId);
    stateStore.remove(key);
    logger.info('Deleted project item', { shopifyId: key, itemId: entry.itemId });
    return { action: 'deleted', ...entry };
  }

  return { upsertProduct, deleteProduct };
}
