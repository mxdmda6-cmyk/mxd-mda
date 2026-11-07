import fs from 'node:fs';
import path from 'node:path';

// Minimal .env loader so the script has no runtime dependency on `dotenv`.
// Real process.env values (e.g. from a shell or CI secrets) always win over the file.
function loadDotEnvFile(filePath) {
  if (!fs.existsSync(filePath)) return;
  const contents = fs.readFileSync(filePath, 'utf8');
  for (const rawLine of contents.split('\n')) {
    const line = rawLine.trim();
    if (!line || line.startsWith('#')) continue;
    const eqIndex = line.indexOf('=');
    if (eqIndex === -1) continue;
    const key = line.slice(0, eqIndex).trim();
    let value = line.slice(eqIndex + 1).trim();
    const isQuoted =
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"));
    if (isQuoted) {
      value = value.slice(1, -1);
    }
    if (!(key in process.env)) {
      process.env[key] = value;
    }
  }
}

loadDotEnvFile(path.resolve(process.cwd(), '.env'));

export const env = process.env;

const BASE_REQUIRED_VARS = [
  'SHOPIFY_STORE_DOMAIN',
  'SHOPIFY_ADMIN_API_TOKEN',
  'SHOPIFY_API_VERSION',
  'GITHUB_TOKEN',
  'GITHUB_PROJECT_OWNER',
  'GITHUB_PROJECT_NUMBER',
];

export function requireEnv(extraVars = []) {
  const missing = [...BASE_REQUIRED_VARS, ...extraVars].filter((key) => !env[key]);
  if (missing.length > 0) {
    throw new Error(`Missing required environment variables: ${missing.join(', ')}`);
  }
}
