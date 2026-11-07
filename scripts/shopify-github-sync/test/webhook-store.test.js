import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { createWebhookStore } from '../lib/webhook-store.js';

test('webhook events persist across store instances and are deduplicated', (t) => {
  const directory = fs.mkdtempSync(path.join(os.tmpdir(), 'shopify-webhook-store-'));
  t.after(() => fs.rmSync(directory, { recursive: true, force: true }));
  const filePath = path.join(directory, 'pending.json');
  const event = {
    id: 'webhook-1',
    topic: 'products/update',
    product: { id: 123, title: 'Product' },
  };

  const firstStore = createWebhookStore(filePath);
  assert.equal(firstStore.add(event), true);

  const restoredStore = createWebhookStore(filePath);
  assert.deepEqual(restoredStore.getAll(), [event]);
  assert.equal(restoredStore.add(event), false);
  restoredStore.remove(event.id);
  assert.deepEqual(createWebhookStore(filePath).getAll(), []);
});
