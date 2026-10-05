import test from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { Weezy, WeezyError } from '../dist/esm/index.js';
const credentials = { clientId: 'fixture', clientSecret: 'test-only' };
const json = (data, status = 200) => new Response(JSON.stringify(data), { status, headers: { 'content-type': 'application/json', 'x-request-id': 'request-test' } });

test('SMS sends Basic authentication and returns unwrapped message', async () => {
  const client = new Weezy({ ...credentials, fetch: async (url, options) => {
    assert.equal(url, 'https://api.weezy.app/client/api/v1/sms/send');
    assert.equal(options.headers.Authorization, 'Basic ' + Buffer.from('fixture:test-only').toString('base64'));
    assert.equal(options.redirect, 'error');
    assert.deepEqual(JSON.parse(options.body), { to: '+2250700000000', body: 'Bonjour', sender_name: 'WEEZY' });
    return json({ code: 200, msg: 'ok', data: { x_id: 'message-test' } });
  } });
  assert.equal((await client.sms.send({ to: '+2250700000000', body: 'Bonjour', sender_name: 'WEEZY' })).x_id, 'message-test');
});
test('WhatsApp preserves provider response and encodes instance IDs', async () => {
  const client = new Weezy({ ...credentials, fetch: async (url) => {
    assert.match(url, /\/session%2Fa\/messages\/text$/);
    return json({ status: true, message: 'sent', provider_field: 4 });
  } });
  assert.deepEqual(await client.whatsapp('session/a').messages.sendTextMessage({ phone: '2250700000000', message: 'Bonjour' }), { status: true, message: 'sent', provider_field: 4 });
});
test('GET path parameters encoded; query parameters serialized', async () => {
  const urls = [];
  const client = new Weezy({ ...credentials, baseUrl: 'http://localhost:8000/client/api/v1/', fetch: async (url) => { urls.push(url); return json({ code: 200, msg: 'ok', data: {} }); } });
  await client.sms.status({ message_x_id: 'a/b' });
  assert.match(urls[0], /\/sms\/status\/a%2Fb$/);
  assert.throws(() => client.whatsapp('..'), TypeError);
});
test('HTTP errors carry status, details and request ID, without retrying sends', async () => {
  let calls = 0;
  const client = new Weezy({ ...credentials, fetch: async () => { calls++; return json({ code: 429, msg: 'Rate limited' }, 429); } });
  await assert.rejects(client.sms.balance(), error => error instanceof WeezyError && error.status === 429 && error.requestId === 'request-test');
  assert.equal(calls, 1);
});
test('logical errors in HTTP 200 envelopes are rejected', async () => {
  const client = new Weezy({ ...credentials, fetch: async () => json({ code: 403, msg: 'Forbidden' }) });
  await assert.rejects(client.sms.balance(), /Forbidden/);
});
test('malformed JSON and transport errors produce structured errors', async () => {
  const malformed = new Weezy({ ...credentials, fetch: async () => new Response('<html>error</html>', { status: 502 }) });
  await assert.rejects(malformed.sms.balance(), error => error instanceof WeezyError && error.status === 502);
  const offline = new Weezy({ ...credentials, fetch: async () => { throw new TypeError('connection failed'); } });
  await assert.rejects(offline.sms.balance(), error => error instanceof WeezyError && error.status === 0);
});
test('timeout aborts the request', async () => {
  const client = new Weezy({ ...credentials, timeoutMs: 5, fetch: (_, options) => new Promise((resolve, reject) => options.signal.addEventListener('abort', () => reject(new Error('aborted')), { once: true })) });
  await assert.rejects(client.sms.balance(), /timed out/);
});
test('CommonJS entry point exports the client', () => {
  assert.equal(typeof createRequire(import.meta.url)('../dist/cjs/index.js').Weezy, 'function');
});
test('rejects unsafe configuration', () => {
  for (const baseUrl of ['file:///tmp', 'https://key:secret@example.com', 'https://example.com?token=test']) assert.throws(() => new Weezy({ ...credentials, baseUrl }));
  assert.throws(() => new Weezy({ ...credentials, timeoutMs: Infinity }));
});
