from typing import Any
import httpx
from ._transport import WeezyError, decode, segment, validate
from .resources import SmsAPI, AsyncSmsAPI, WhatsAppAPI, AsyncWhatsAppAPI

DEFAULT_BASE_URL = "https://api.weezy.app/client/api/v1"


class Weezy:
    def __init__(self, *, client_id: str, client_secret: str, base_url: str = DEFAULT_BASE_URL,
                 timeout: float = 30, transport: httpx.BaseTransport | None = None):
        self._base_url = validate(client_id, client_secret, base_url, timeout)
        self._http = httpx.Client(auth=(client_id, client_secret), timeout=timeout, transport=transport,
                                  headers={"Accept": "application/json"}, follow_redirects=False)
        self.sms = SmsAPI(self)

    def whatsapp(self, instance_id: str) -> WhatsAppAPI:
        segment(instance_id)
        return WhatsAppAPI(self, instance_id)

    def request(self, method: str, path: str, *, body: Any = None, query: dict | None = None, unwrap: bool = False) -> Any:
        try:
            response = self._http.request(method, self._base_url + path, json=body,
                                          params={k: v for k, v in (query or {}).items() if v is not None})
        except httpx.TimeoutException:
            raise WeezyError("Request timed out") from None
        except httpx.HTTPError:
            raise WeezyError("Network request failed") from None
        return decode(response, unwrap=unwrap)

    def close(self) -> None:
        self._http.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


class AsyncWeezy:
    def __init__(self, *, client_id: str, client_secret: str, base_url: str = DEFAULT_BASE_URL,
                 timeout: float = 30, transport: httpx.AsyncBaseTransport | None = None):
        self._base_url = validate(client_id, client_secret, base_url, timeout)
        self._http = httpx.AsyncClient(auth=(client_id, client_secret), timeout=timeout, transport=transport,
                                       headers={"Accept": "application/json"}, follow_redirects=False)
        self.sms = AsyncSmsAPI(self)

    def whatsapp(self, instance_id: str) -> AsyncWhatsAppAPI:
        segment(instance_id)
        return AsyncWhatsAppAPI(self, instance_id)

    async def request(self, method: str, path: str, *, body: Any = None, query: dict | None = None, unwrap: bool = False) -> Any:
        try:
            response = await self._http.request(method, self._base_url + path, json=body,
                                                params={k: v for k, v in (query or {}).items() if v is not None})
        except httpx.TimeoutException:
            raise WeezyError("Request timed out") from None
        except httpx.HTTPError:
            raise WeezyError("Network request failed") from None
        return decode(response, unwrap=unwrap)

    async def aclose(self) -> None:
        await self._http.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.aclose()
