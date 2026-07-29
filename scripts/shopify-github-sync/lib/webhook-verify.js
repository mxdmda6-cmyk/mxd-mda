import crypto from 'node:crypto';

export function verifyShopifyHmac(rawBody, hmacHeader, secret) {
  if (!hmacHeader || !secret) return false;

  const digest = crypto.createHmac('sha256', secret).update(rawBody).digest('base64');
  const expected = Buffer.from(digest);
  const provided = Buffer.from(hmacHeader);

  if (expected.length !== provided.length) return false;
  return crypto.timingSafeEqual(expected, provided);
}
