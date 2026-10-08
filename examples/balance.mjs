// Install the SDK first: npm install @weezy-app/sdk
import { Weezy } from '@weezy-app/sdk';
const client = new Weezy({
  clientId: process.env.WEEZY_CLIENT_ID,
  clientSecret: process.env.WEEZY_CLIENT_SECRET,
  baseUrl: process.env.WEEZY_BASE_URL,
});
const wallet = await client.sms.balance();
// Amounts are in points (1 point = 1 EUR, up to 3 decimals).
console.log(`Balance: ${wallet.balance} ${wallet.unit}s (spent ${wallet.total_spent}, topped up ${wallet.total_topped_up})`);
