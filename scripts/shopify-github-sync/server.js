#!/usr/bin/env node
import http from 'node:http';
import { env, requireEnv } from './lib/env.js';
import { logger } from './lib/logger.js';
import { verifyShopifyHmac } from './lib/webhook-verify.js';
import { createTaskQueue } from './lib/queue.js';
import { createGithubProjectsClient } from './lib/github-projects.js';
import { createStateStore } from './lib/state-store.js';
import { createSyncEngine } from './lib/sync-engine.js';
import { createWebhookStore } from './lib/webhook-store.js';

const MAX_BODY_BYTES = 5 * 1024 * 1024;
const PRODUCT_TOPICS = new Set(['products/create', 'products/update', 'products/delete']);

function assertEnabled() {
  if (env.ENABLE_SHOPIFY_GITHUB_SYNC !== 'true') {
    logger.error(
      'ENABLE_SHOPIFY_GITHUB_SYNC is not "true" - refusing to start the live listener. ' +
        'Set it in .env once you are ready to run real-time sync.'
    );
    process.exit(1);
  }
}

function collectRawBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let size = 0;
    req.on('data', (chunk) => {
      size += chunk.length;
      if (size > MAX_BODY_BYTES) {
        req.destroy();
        reject(new Error('Payload too large'));
        return;
      }
      chunks.push(chunk);
    });
    req.on('end', () => resolve(Buffer.concat(chunks)));
    req.on('error', reject);
  });
}

async function main() {
  requireEnv(['SHOPIFY_WEBHOOK_SECRET']);
  assertEnabled();

  const githubClient = createGithubProjectsClient();
  const stateStore = createStateStore();
  const syncEngine = createSyncEngine({ githubClient, stateStore });
  const webhookStore = createWebhookStore();

  const queue = createTaskQueue({
    concurrency: 3,
    maxRetries: 5,
    isRetryable: (err) => err.retryable === true,
  });

  function enqueueWebhook(event) {
    queue
      .enqueue(async () => {
        if (event.topic === 'products/delete') {
          await syncEngine.deleteProduct(event.product.id);
        } else {
          await syncEngine.upsertProduct(event.product);
        }
        webhookStore.remove(event.id);
      })
      .catch((err) => {
        logger.error('Webhook processing failed; the event remains persisted for replay', {
          shopifyProductId: event.product.id,
          topic: event.topic,
          webhookId: event.id,
          error: err.message,
        });
      });
  }

  for (const event of webhookStore.getAll()) {
    enqueueWebhook(event);
  }

  const server = http.createServer(async (req, res) => {
    if (req.method === 'GET' && req.url === '/healthz') {
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ status: 'ok' }));
      return;
    }

    if (req.method !== 'POST' || req.url !== '/webhooks/shopify/products') {
      res.writeHead(404);
      res.end();
      return;
    }

    let rawBody;
    try {
      rawBody = await collectRawBody(req);
    } catch (err) {
      logger.error('Failed to read webhook body', { error: err.message });
      res.writeHead(413);
      res.end();
      return;
    }

    const hmacHeader = req.headers['x-shopify-hmac-sha256'];
    const topic = req.headers['x-shopify-topic'];
    const shopDomain = req.headers['x-shopify-shop-domain'];
    const webhookId = req.headers['x-shopify-webhook-id'];

    if (!verifyShopifyHmac(rawBody, hmacHeader, env.SHOPIFY_WEBHOOK_SECRET)) {
      logger.warn('Rejected webhook: HMAC verification failed', { shopDomain, topic });
      res.writeHead(401);
      res.end();
      return;
    }

    if (
      typeof shopDomain !== 'string' ||
      shopDomain.toLowerCase() !== env.SHOPIFY_STORE_DOMAIN.toLowerCase()
    ) {
      logger.warn('Rejected webhook: shop domain does not match configured store', {
        shopDomain,
        topic,
      });
      res.writeHead(401);
      res.end();
      return;
    }

    if (
      typeof topic !== 'string' ||
      !PRODUCT_TOPICS.has(topic) ||
      typeof webhookId !== 'string' ||
      webhookId.length === 0
    ) {
      logger.warn('Rejected webhook: missing or unsupported Shopify webhook headers', {
        topic,
      });
      res.writeHead(400);
      res.end();
      return;
    }

    let product;
    try {
      product = JSON.parse(rawBody.toString('utf8'));
    } catch (err) {
      logger.error('Rejected webhook: invalid JSON', { error: err.message });
      res.writeHead(400);
      res.end();
      return;
    }

    if (
      !product ||
      typeof product !== 'object' ||
      !/^\d+$/.test(String(product.id ?? ''))
    ) {
      logger.warn('Rejected webhook: payload has no valid product ID', { topic, webhookId });
      res.writeHead(400);
      res.end();
      return;
    }

    try {
      const added = webhookStore.add({ id: webhookId, topic, product });
      if (added) enqueueWebhook({ id: webhookId, topic, product });
    } catch (err) {
      logger.error('Failed to persist webhook before acknowledging it', {
        topic,
        webhookId,
        error: err.message,
      });
      res.writeHead(500);
      res.end();
      return;
    }

    // Persist before acknowledging so a process restart can replay accepted events.
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ received: true }));
  });

  const port = Number(env.SYNC_SERVER_PORT) || 3000;
  server.listen(port, () => {
    logger.info(`Shopify -> GitHub Projects webhook listener started on port ${port}`);
  });
}

main().catch((err) => {
  logger.error('Fatal startup error', { error: err.message });
  process.exit(1);
});
