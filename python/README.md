# weezy-sdk

Typed SMS clients for Python 3.11+.

## Installation

```sh
pip install weezy-sdk
```

The package is named `weezy-sdk`; import clients from `weezy`.

For local development, install from this repository with `pip install ./python`.

## Synchronous client

```python
import os
from weezy import Weezy, WeezyError

with Weezy(
    client_id=os.environ['WEEZY_CLIENT_ID'],
    client_secret=os.environ['WEEZY_CLIENT_SECRET'],
) as client:
    wallet = client.sms.balance()
    print(f"Balance: {wallet['balance']:.3f} points")  # 1 point = 1 EUR
    message = client.sms.send(body={
        'to': '+2250700000000', 'body': 'Bonjour !', 'sender_name': 'WEEZY',
    })
    print(f"Cost: {message['cost']} points")
    status = client.sms.status(message_x_id=message['x_id'])
```

## Asynchronous client

```python
import asyncio
import os
from weezy import AsyncWeezy

async def main():
    async with AsyncWeezy(
        client_id=os.environ['WEEZY_CLIENT_ID'],
        client_secret=os.environ['WEEZY_CLIENT_SECRET'],
    ) as client:
        wallet = await client.sms.balance()
        print(f"Balance: {wallet['balance']:.3f} points")

asyncio.run(main())
```

Send methods create real messages with live credentials. Use a dedicated test account and recipient when testing.

SMS methods: `balance()`, `senders()`, `send(body=...)`, `send_bulk(body=...)`, `status(message_x_id=...)`, `opt_outs(body=...)`. All arguments are keyword-only. See [the full reference](API.md).

`WeezyError` exposes `status`, `details` and `request_id`. A timeout or transport failure has status `0`. Close clients with `close()` / `await aclose()` or use the context managers above. Options include `base_url` (full client API prefix), `timeout` in seconds and an injectable `httpx` transport. No automatic retries.

SMS amounts (`balance`, `cost`, `unit_price`, `amount_reserved`, ...) are `float` values in **points** (1 point = 1 EUR, up to 3 decimals), with `unit == 'point'` on the object.

TypedDict request and response contracts are exported from `weezy.types`. They support editor/type-checker assistance; runtime validation remains on the API.
