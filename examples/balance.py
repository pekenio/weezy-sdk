import asyncio
import os
from weezy import AsyncWeezy

async def main():
    options = {
        'client_id': os.environ['WEEZY_CLIENT_ID'],
        'client_secret': os.environ['WEEZY_CLIENT_SECRET'],
    }
    if os.environ.get('WEEZY_BASE_URL'):
        options['base_url'] = os.environ['WEEZY_BASE_URL']
    async with AsyncWeezy(**options) as client:
        wallet = await client.sms.balance()
        # Amounts are in points (1 point = 1 EUR, up to 3 decimals).
        print(f"Balance: {wallet['balance']} {wallet['unit']}s "
              f"(spent {wallet['total_spent']}, topped up {wallet['total_topped_up']})")

if __name__ == '__main__':
    asyncio.run(main())
