# Weezy SDKs — 0.1.0

SDKs for the **public client API**, covering SMS and WhatsApp. The generated resources cover 126 operations across 124 paths. Dashboard, administration and webhook receiver routes are excluded.

- [JavaScript / TypeScript](typescript/README.md): Node.js 20+, ESM and CommonJS, generated request/result types.
- [Python](python/README.md): Python 3.11+, synchronous `Weezy` and asynchronous `AsyncWeezy`, TypedDict contracts and `py.typed`.
- [API reference](API.md): all resource methods and routes.

These packages are prepared for local installation; **they are not published to npm or PyPI**. Package names and versions are provisional.

## Authentication and transport

Both channels use HTTP Basic authentication with the **client ID and client secret** from Weezy's developer credentials. These SDKs are intended for server-side code. Keep credentials in environment variables.

The default base URL is `https://api.weezy.app/client/api/v1`. For local development use `http://localhost:8000/client/api/v1`. The configured URL must include the full client API prefix.

SMS responses are unwrapped from `{code, msg, data}`. WhatsApp responses preserve the provider payload and extra fields. Monetary amounts are in the currency's minor units (EUR cents). Sending requires the account's available balance or WhatsApp subscription and connected instance, as enforced by the API.

The default timeout is 30 seconds. Requests are **not automatically retried**, including after a timeout: an SMS or WhatsApp send may already have been accepted. Inspect status before deciding whether to resend. HTTP failures, non-JSON responses, timeouts and network failures raise `WeezyError`; input/configuration errors raise the language's normal validation exception. HTTP redirect following is disabled.

Generated types describe the contract; input validation remains on the API. SDKs do not manage WhatsApp instance creation or connection through dashboard routes. Webhook signature verification is not included in this version.

## Regenerate contracts

From the project root, using the backend virtual environment:

```sh
PYTHONPATH=weezy-api-python/api weezy-api-python/api/.venv/bin/python weezy-sdk/scripts/export_contract.py
python3 weezy-sdk/scripts/generate.py
```

Export builds a minimal FastAPI application from the public router modules, without starting the API or touching the database. `openapi.json` is the snapshot. The export includes precise SMS response data contracts in the snapshot. The generator runs with Python’s standard library alone. Review generated diffs whenever routes or schemas change.

## Validate and package

```sh
cd weezy-sdk/typescript
npm ci
npm test
npm pack
```

From the project root:

```sh
PYTHONPATH=weezy-sdk/python/src weezy-api-python/api/.venv/bin/python -m unittest discover -s weezy-sdk/python/tests
weezy-api-python/api/.venv/bin/python -m pip wheel --no-deps ./weezy-sdk/python -w ./weezy-sdk/python/dist
```

Tests use mocked transports: no messages are sent, no balances are debited, and no provider is contacted. Publishing and a live sandbox smoke test remain separate release steps.
