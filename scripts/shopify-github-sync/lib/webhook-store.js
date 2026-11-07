import fs from 'node:fs';
import path from 'node:path';

const DEFAULT_QUEUE_PATH = path.resolve(
  process.cwd(),
  'scripts/shopify-github-sync/.state/pending-webhooks.json'
);

export function createWebhookStore(
  filePath = process.env.SYNC_WEBHOOK_QUEUE_FILE_PATH || DEFAULT_QUEUE_PATH
) {
  let events = new Map();

  if (fs.existsSync(filePath)) {
    const stored = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    if (!stored || typeof stored !== 'object' || Array.isArray(stored)) {
      throw new Error(`Invalid webhook queue file: ${filePath}`);
    }
    events = new Map(Object.entries(stored));
  }

  function persist() {
    const dir = path.dirname(filePath);
    fs.mkdirSync(dir, { recursive: true });
    const tmpPath = `${filePath}.tmp`;
    fs.writeFileSync(tmpPath, JSON.stringify(Object.fromEntries(events), null, 2));
    fs.renameSync(tmpPath, filePath);
  }

  return {
    add(event) {
      if (events.has(event.id)) return false;
      events.set(event.id, event);
      try {
        persist();
      } catch (err) {
        events.delete(event.id);
        throw err;
      }
      return true;
    },
    getAll() {
      return [...events.values()];
    },
    remove(id) {
      const event = events.get(id);
      if (!events.delete(id)) return;
      try {
        persist();
      } catch (err) {
        events.set(id, event);
        throw err;
      }
    },
  };
}
