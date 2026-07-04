#!/usr/bin/env node
import http from 'node:http';
import { env, requireEnv } from './lib/env.js';
import { logger } from './lib/logger.js';
import { verifyShopifyHmac } from './lib/webhook-verify.js';
import { createTaskQueue } from './lib/queue.js';
import { createGithubProjectsClient } from './lib/github-projects.js';
import { createStateStore } from './lib/state-store.js';
import { createSyncEngine } from './lib/sync-engine.js';

const MAX_BODY_BYTES = 5 * 1024 * 1024;

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

  const queue = createTaskQueue({
    concurrency: 3,
    maxRetries: 5,
    isRetryable: (err) => err.retryable === true,
  });

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

    if (!verifyShopifyHmac(rawBody, hmacHeader, env.SHOPIFY_WEBHOOK_SECRET)) {
      logger.warn('Rejected webhook: HMAC verification failed', { shopDomain, topic });
      res.writeHead(401);
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

    // Ack immediately - Shopify retries/times out around 5s. GitHub sync runs after the response.
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ received: true }));

    queue
      .enqueue(() =>
        topic === 'products/delete'
          ? syncEngine.deleteProduct(product.id)
          : syncEngine.upsertProduct(product)
      )
      .catch((err) => {
        logger.error('Sync task failed permanently after retries', {
          shopifyProductId: product?.id,
          topic,
          error: err.message,
        });
      });
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
