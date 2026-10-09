# Changelog

## 0.3.0

**Breaking:** SDKs now exclusively expose the six public SMS operations. Legacy non-SMS resources, types and examples are no longer included. SMS authentication, amounts and error handling are unchanged.

## 0.2.1

- Surface string `detail` messages from FastAPI HTTP errors in both SDKs, preserving status, response details and request ID without retries.
- Regenerate and verify the public contract; dashboard OAuth and account access management remain outside the SDK.

## 0.2.0

**Breaking:** SMS monetary amounts are now **points** (1 point = 1 EUR), returned as JSON numbers with up to 3 decimals, instead of integer EUR cents.

- `WalletOut.balance`, `total_topped_up`, `total_spent` and `low_balance_threshold`, `SmsMessageOut.unit_price` and `cost`, `SmsBatchOut.amount_reserved` and `amount_refunded` are now `number` (TypeScript) / `float` (Python). SMS webhook amounts (`cost`, `refunded`) follow the same unit.
- These objects now include `unit: "point"`.
- Migration: stop dividing by 100. A former value of `500` (cents) is now `5.0` (points). Compare amounts with a tolerance or round to 3 decimals instead of using integer equality.

## 0.1.0

- JavaScript/TypeScript support for Node.js 20+, ESM and CommonJS.
- Python 3.11+ synchronous and asynchronous clients with typed contracts.
- Basic authentication, configurable timeout and structured request errors.
- Generated API reference, examples, MIT licence and release workflows.
