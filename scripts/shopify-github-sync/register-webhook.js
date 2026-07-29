#!/usr/bin/env node
import { env, requireEnv } from './lib/env.js';
import { logger } from './lib/logger.js';

const TOPICS = ['products/create', 'products/update', 'products/delete'];

function baseUrl() {
  return `https://${env.SHOPIFY_STORE_DOMAIN}/admin/api/${env.SHOPIFY_API_VERSION}`;
}

function authHeaders() {
  return {
    'X-Shopify-Access-Token': env.SHOPIFY_ADMIN_API_TOKEN,
    'Content-Type': 'application/json',
  };
}

async function listExistingWebhooks() {
  const res = await fetch(`${baseUrl()}/webhooks.json`, { headers: authHeaders() });
  if (!res.ok) throw new Error(`Failed to list webhooks: HTTP ${res.status}`);
  const data = await res.json();
  return data.webhooks;
}

async function createWebhook(topic, address) {
  const res = await fetch(`${baseUrl()}/webhooks.json`, {
    method: 'POST',
    headers: authHeaders(),
    body: JSON.stringify({ webhook: { topic, address, format: 'json' } }),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Failed to create webhook for ${topic}: HTTP ${res.status} - ${text}`);
  }
  return res.json();
}

async function main() {
  requireEnv(['PUBLIC_WEBHOOK_URL']);

  const targetAddress = `${env.PUBLIC_WEBHOOK_URL}/webhooks/shopify/products`;
  const existing = await listExistingWebhooks();

  for (const topic of TOPICS) {
    const already = existing.find((w) => w.topic === topic && w.address === targetAddress);
    if (already) {
      logger.info('Webhook already registered, skipping', { topic, address: targetAddress });
      continue;
    }
    try {
      const created = await createWebhook(topic, targetAddress);
      logger.info('Registered webhook', { topic, id: created.webhook.id, address: targetAddress });
    } catch (err) {
      logger.error('Failed to register webhook', { topic, error: err.message });
    }
  }
}

main().catch((err) => {
  logger.error('Fatal error registering webhooks', { error: err.message });
  process.exit(1);
});
