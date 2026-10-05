# @weezy/sdk

Typed Weezy SMS and WhatsApp client for Node.js 20+.

## Install locally

```sh
cd weezy-sdk/typescript
npm ci
npm run build
# From your own application:
npm install /absolute/path/to/weezy-sdk/typescript
```

## SMS and WhatsApp

```ts
import { Weezy, WeezyError } from '@weezy/sdk';

const client = new Weezy({
  clientId: process.env.WEEZY_CLIENT_ID!,
  clientSecret: process.env.WEEZY_CLIENT_SECRET!,
  timeoutMs: 30_000,
});

const wallet = await client.sms.balance();
const message = await client.sms.send({
  to: '+2250700000000', body: 'Bonjour !', sender_name: 'WEEZY',
});
const status = await client.sms.status({ message_x_id: message.x_id });

const result = await client.whatsapp(process.env.WEEZY_INSTANCE_ID!).messages.sendTextMessage({
  phone: '2250700000000', message: 'Bonjour !',
});
```

These send methods create real messages when used with live credentials. Use a dedicated test account and recipient when testing.

CommonJS is supported: `const { Weezy } = require('@weezy/sdk')`.

SMS methods: `balance()`, `senders()`, `send(body)`, `sendBulk(body)`, `status(params)`, `optOuts(body)`.

WhatsApp exposes `messages`, `contacts`, `groups`, `chats`, `products`, `labels`, `stories`, `community`, `broadcasts`, `presence`, `media` and `misc`. Method names are camelCase forms of the backend handlers; [the reference](API.md) lists all methods. Methods with a JSON body accept it as the first argument, then route/query parameters as the second. Methods without a body accept route/query parameters as the first argument.

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
