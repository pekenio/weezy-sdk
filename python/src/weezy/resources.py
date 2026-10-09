"""Generated resource methods."""
from __future__ import annotations
from typing import Any, Dict, List, Literal, Union
from ._transport import segment
from .types import *

class SmsAPI:
    def __init__(self, client):
        self._client = client

    def balance(self) -> 'WalletOut':
        """Remaining wallet balance."""
        return self._client.request('GET', f'/sms/balance', body=None, query={}, unwrap=True)

    def senders(self) -> Dict[str, Any]:
        """Sender IDs available for sending."""
        return self._client.request('GET', f'/sms/senders', body=None, query={}, unwrap=True)

    def send(self, *, body: 'SmsSendIn') -> 'SmsMessageOut':
        """Send one SMS."""
        return self._client.request('POST', f'/sms/send', body=body, query={}, unwrap=True)

    def send_bulk(self, *, body: 'SmsBulkSendIn') -> 'SmsBulkSendOut':
        """Send the same SMS to many recipients."""
        return self._client.request('POST', f'/sms/send-bulk', body=body, query={}, unwrap=True)

    def status(self, *, message_x_id: str) -> 'SmsMessageOut':
        """Get the delivery status of one SMS."""
        return self._client.request('GET', f'/sms/status/{segment(message_x_id)}', body=None, query={}, unwrap=True)

    def opt_outs(self, *, body: 'SmsOptOutIn') -> Dict[str, Any]:
        """Unsubscribe numbers (excluded from all future sends)."""
        return self._client.request('POST', f'/sms/opt-outs', body=body, query={}, unwrap=True)

class AsyncSmsAPI:
    def __init__(self, client):
        self._client = client

    async def balance(self) -> 'WalletOut':
        """Remaining wallet balance."""
        return await self._client.request('GET', f'/sms/balance', body=None, query={}, unwrap=True)

    async def senders(self) -> Dict[str, Any]:
        """Sender IDs available for sending."""
        return await self._client.request('GET', f'/sms/senders', body=None, query={}, unwrap=True)

    async def send(self, *, body: 'SmsSendIn') -> 'SmsMessageOut':
        """Send one SMS."""
        return await self._client.request('POST', f'/sms/send', body=body, query={}, unwrap=True)

    async def send_bulk(self, *, body: 'SmsBulkSendIn') -> 'SmsBulkSendOut':
        """Send the same SMS to many recipients."""
        return await self._client.request('POST', f'/sms/send-bulk', body=body, query={}, unwrap=True)

    async def status(self, *, message_x_id: str) -> 'SmsMessageOut':
        """Get the delivery status of one SMS."""
        return await self._client.request('GET', f'/sms/status/{segment(message_x_id)}', body=None, query={}, unwrap=True)

    async def opt_outs(self, *, body: 'SmsOptOutIn') -> Dict[str, Any]:
        """Unsubscribe numbers (excluded from all future sends)."""
        return await self._client.request('POST', f'/sms/opt-outs', body=body, query={}, unwrap=True)
