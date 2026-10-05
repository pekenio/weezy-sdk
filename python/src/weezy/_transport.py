from typing import Any
from urllib.parse import quote, urlsplit
import httpx


class WeezyError(Exception):
    def __init__(self, message: str, *, status: int = 0, details: Any = None, request_id: str | None = None):
        super().__init__(message)
        self.status = status
        self.details = details
        self.request_id = request_id


def segment(value: Any) -> str:
    if value is None or str(value) in ("", ".", ".."):
        raise ValueError("A valid path parameter is required")
    return quote(str(value), safe="")


def validate(client_id: str, client_secret: str, base_url: str, timeout: float) -> str:
    if not client_id or not client_secret or ":" in client_id:
        raise ValueError("Valid client_id and client_secret are required")
    url = urlsplit(base_url)
    if url.scheme not in ("https", "http") or not url.netloc or url.username or url.password or url.query or url.fragment:
        raise ValueError("Invalid base_url")
    if not timeout > 0 or timeout == float("inf"):
        raise ValueError("timeout must be finite and positive")
    return base_url.rstrip("/")


def decode(response: httpx.Response, *, unwrap: bool) -> Any:
    if response.status_code == 204:
        return None
    try:
        data = response.json()
    except ValueError:
        raise WeezyError("API returned a non-JSON response", status=response.status_code, details=response.text,
                         request_id=response.headers.get("x-request-id")) from None
    envelope = isinstance(data, dict) and isinstance(data.get("code"), int) and "msg" in data
    if response.is_error or response.is_redirect or (unwrap and envelope and data['code'] >= 400):
        raise WeezyError(data.get("msg", f"API request failed ({response.status_code})") if isinstance(data, dict) else f"API request failed ({response.status_code})",
                         status=response.status_code, details=data, request_id=response.headers.get("x-request-id"))
    return data.get("data") if unwrap and envelope else data
