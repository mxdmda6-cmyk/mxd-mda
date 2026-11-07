#!/usr/bin/env node
import { env, requireEnv } from './lib/env.js';
import { logger } from './lib/logger.js';
import { fetchAllProducts } from './lib/shopify-client.js';
import { createGithubProjectsClient } from './lib/github-projects.js';
import { createStateStore } from './lib/state-store.js';
import { createSyncEngine } from './lib/sync-engine.js';

const dryRun = process.argv.includes('--dry-run');
const isBulk = process.argv.includes('--bulk');

function assertEnabled() {
  if (env.ENABLE_SHOPIFY_GITHUB_SYNC !== 'true') {
    logger.error(
      'ENABLE_SHOPIFY_GITHUB_SYNC is not "true" - refusing to run. Set it in .env once you are ready.'
    );
    process.exit(1);
  }
}

async function main() {
  if (!isBulk) {
    logger.error(
      'Refusing to run without --bulk. This entrypoint is reserved for initial catalog ' +
        'import and testing only - it is not meant for recurring/scheduled use. Use ' +
        'server.js for ongoing real-time sync.'
    );
    process.exit(1);
  }

  requireEnv();
  assertEnabled();

  logger.warn('=== BULK IMPORT MODE ===', {
    dryRun,
    note: 'Initial catalog seeding / testing only. Do not schedule this to run repeatedly.',
  });

  const githubClient = createGithubProjectsClient();
  const stateStore = createStateStore();
  const syncEngine = createSyncEngine({ githubClient, stateStore });

  const summary = { total: 0, created: 0, updated: 0, failed: 0 };

  for await (const product of fetchAllProducts()) {
    summary.total++;
    try {
      if (dryRun) {
        logger.info('[dry-run] would upsert product', { shopifyId: product.id, title: product.title });
        continue;
      }
      const result = await syncEngine.upsertProduct(product);
      summary[result.action] = (summary[result.action] ?? 0) + 1;
    } catch (err) {
      summary.failed++;
      logger.error('Failed to sync product during bulk import', {
        shopifyId: product.id,
        title: product.title,
        error: err.message,
      });
    }
  }

  logger.info('Bulk import complete', summary);
  if (summary.failed > 0) process.exit(1);
}

main().catch((err) => {
  logger.error('Fatal bulk import error', { error: err.message });
  process.exit(1);
});
