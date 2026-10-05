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
        print(await client.sms.balance())

if __name__ == '__main__':
    asyncio.run(main())
