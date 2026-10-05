# weezy-sdk

Typed SMS and WhatsApp clients for Python 3.11+.

## Install locally

```sh
pip install /absolute/path/to/weezy-sdk/python
```

## Synchronous client

```python
import os
from weezy import Weezy, WeezyError

with Weezy(
    client_id=os.environ['WEEZY_CLIENT_ID'],
    client_secret=os.environ['WEEZY_CLIENT_SECRET'],
) as client:
    wallet = client.sms.balance()
    message = client.sms.send(body={
        'to': '+2250700000000', 'body': 'Bonjour !', 'sender_name': 'WEEZY',
    })
    status = client.sms.status(message_x_id=message['x_id'])
    result = client.whatsapp(os.environ['WEEZY_INSTANCE_ID']).messages.send_text_message(body={
        'phone': '2250700000000', 'message': 'Bonjour !',
    })
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
        print(await client.sms.balance())

asyncio.run(main())
```

Send methods create real messages with live credentials. Use a dedicated test account and recipient when testing.

SMS methods: `balance()`, `senders()`, `send(body=...)`, `send_bulk(body=...)`, `status(message_x_id=...)`, `opt_outs(body=...)`. All arguments are keyword-only. WhatsApp resource methods match the backend handler names; see [the full reference](API.md).

`WeezyError` exposes `status`, `details` and `request_id`. A timeout or transport failure has status `0`. Close clients with `close()` / `await aclose()` or use the context managers above. Options include `base_url` (full client API prefix), `timeout` in seconds and an injectable `httpx` transport. No automatic retries.

TypedDict request and response contracts are exported from `weezy.types`. They support editor/type-checker assistance; runtime validation remains on the API.
