import { env } from './env.js';

function baseUrl() {
  return `https://${env.SHOPIFY_STORE_DOMAIN}/admin/api/${env.SHOPIFY_API_VERSION}`;
}

function authHeaders() {
  return {
    'X-Shopify-Access-Token': env.SHOPIFY_ADMIN_API_TOKEN,
    'Content-Type': 'application/json',
  };
}

async function shopifyRequest(path, options = {}) {
  const res = await fetch(`${baseUrl()}${path}`, { headers: authHeaders(), ...options });

  if (res.status === 429 || res.status >= 500) {
    const err = new Error(`Shopify API transient error: HTTP ${res.status}`);
    err.retryable = true;
    throw err;
  }

  if (!res.ok) {
    const text = await res.text();
    throw new Error(`Shopify API error: HTTP ${res.status} - ${text}`);
  }

  return { data: await res.json(), headers: res.headers };
}

function parseNextLink(linkHeader) {
  if (!linkHeader) return null;
  for (const part of linkHeader.split(',')) {
    const [urlPart, relPart] = part.split(';').map((s) => s.trim());
    if (relPart === 'rel="next"') {
      return urlPart.slice(1, -1);
    }
  }
  return null;
}

// Shopify's REST product list is cursor-paginated via the Link header, not page numbers.
export async function* fetchAllProducts({ pageSize = 100 } = {}) {
  let path = `/products.json?limit=${pageSize}`;
  while (path) {
    const { data, headers } = await shopifyRequest(path);
    for (const product of data.products) {
      yield product;
    }
    const next = parseNextLink(headers.get('link'));
    path = next ? next.replace(baseUrl(), '') : null;
  }
}

function stripHtml(html) {
  // Loop to a fixed point: a single pass can be reconstructed by crafted
  // input (e.g. "<<script>script>"), which is exactly what CodeQL's
  // "incomplete multi-character sanitization" check flags.
  let previous;
  let current = html;
  do {
    previous = current;
    current = previous.replace(/<[^>]*>/g, '');
  } while (current !== previous);
  return current.trim();
}

export function buildItemBody(product) {
  const price = product.variants?.[0]?.price ?? 'n/a';
  const inventory = product.variants?.reduce((sum, v) => sum + (v.inventory_quantity ?? 0), 0);
  const adminUrl = `https://${env.SHOPIFY_STORE_DOMAIN}/admin/products/${product.id}`;

  return [
    product.body_html ? stripHtml(product.body_html) : '_No description._',
    '',
    `**Status:** ${product.status}`,
    `**Price:** ${price}`,
    `**Inventory:** ${inventory ?? 'n/a'}`,
    `**Shopify Admin:** ${adminUrl}`,
  ].join('\n');
}
