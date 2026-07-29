import fs from 'node:fs';
import path from 'node:path';
import { logger } from './logger.js';

const DEFAULT_STATE_PATH = path.resolve(
  process.cwd(),
  'scripts/shopify-github-sync/.state/product-item-map.json'
);

export function createStateStore(filePath = process.env.SYNC_STATE_FILE_PATH || DEFAULT_STATE_PATH) {
  let map = {};

  function load() {
    try {
      if (fs.existsSync(filePath)) {
        map = JSON.parse(fs.readFileSync(filePath, 'utf8'));
      }
    } catch (err) {
      logger.warn('Could not read sync state file, starting with an empty map', {
        filePath,
        error: err.message,
      });
      map = {};
    }
  }

  // Written synchronously on every set/remove for simplicity and crash-safety at
  // expected webhook volumes; batch writes if this becomes a throughput bottleneck.
  function persist() {
    const dir = path.dirname(filePath);
    fs.mkdirSync(dir, { recursive: true });
    const tmpPath = `${filePath}.tmp`;
    fs.writeFileSync(tmpPath, JSON.stringify(map, null, 2));
    fs.renameSync(tmpPath, filePath);
  }

  load();

  return {
    get(shopifyId) {
      return map[String(shopifyId)] ?? null;
    },
    set(shopifyId, entry) {
      map[String(shopifyId)] = { ...entry, updatedAt: new Date().toISOString() };
      persist();
    },
    remove(shopifyId) {
      delete map[String(shopifyId)];
      persist();
    },
  };
}
