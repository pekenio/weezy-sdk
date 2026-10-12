# @weezy-app/sdk

Typed Weezy SMS client for Node.js 20+.

## Install

```sh
npm install @weezy-app/sdk
```

## Develop locally

```sh
cd weezy-sdk/typescript
npm ci
npm run build
# From your own application:
npm install /absolute/path/to/weezy-sdk/typescript
```

## SMS

```ts
import { Weezy, WeezyError } from '@weezy-app/sdk';

const client = new Weezy({
  clientId: process.env.WEEZY_CLIENT_ID!,
  clientSecret: process.env.WEEZY_CLIENT_SECRET!,
  timeoutMs: 30_000,
});

const wallet = await client.sms.balance();
console.log(`Balance: ${wallet.balance} points`); // 1 point = 1 XOF (FCFA)
const message = await client.sms.send({
  to: '+2250700000000', body: 'Bonjour !', sender_name: 'DEFAULT', sandbox: true,
});
console.log(`Cost: ${message.cost} points`);
const status = await client.sms.status({ message_x_id: message.x_id });

```

SMS amounts (`balance`, `cost`, `unit_price`, `amount_reserved`, ...) are numbers in **points** (1 point = 1 XOF (FCFA), up to 3 decimals), with `unit: 'point'` on the object.

Set `sandbox: true` in the request body to simulate an SMS without contacting a provider, debiting balance or consuming the free allowance. Omit it or use `false` for a real, normally billed send. Authentication, active country and sender rules still apply.

CommonJS is supported: `const { Weezy } = require('@weezy-app/sdk')`.

SMS methods: `balance()`, `senders()`, `send(body)`, `sendBulk(body)`, `status(params)`, `optOuts(body)`, `createOtp(body)`, `verifyOtp(body, {challenge_id})`.

See [the reference](API.md) for all SMS methods.

```ts
try {
  await client.sms.balance();
} catch (error) {
  if (error instanceof WeezyError) {
    console.error(error.status, error.message, error.requestId);
    // error.details contains the API response. Treat it as application data.
  } else throw error;
}
```

Transport/configuration options: `baseUrl` (full client API prefix), `timeoutMs`, and an injectable `fetch`. No automatic retries. Do not embed developer credentials in browser code.

## Sandbox and DEFAULT sender

`DEFAULT` selects the platform sender enabled by the administrator for the destination country. It remains available after free test segments are exhausted; real sends are billed normally. Sandbox is a per-request flag on send, bulk send and OTP creation, not a separate base URL or credential. Simulated messages have `source: "sandbox"`. Managed sandbox OTP uses `123456`; check both `verified` and `sandbox` and never authorize a real session with a sandbox result.

Version 0.4.0 includes sandbox request types and managed OTP methods.
