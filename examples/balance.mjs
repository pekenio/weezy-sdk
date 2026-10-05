// Install the local TypeScript package in this directory first.
import { Weezy } from '@weezy/sdk';
const client = new Weezy({
  clientId: process.env.WEEZY_CLIENT_ID,
  clientSecret: process.env.WEEZY_CLIENT_SECRET,
  baseUrl: process.env.WEEZY_BASE_URL,
});
console.log(await client.sms.balance());
