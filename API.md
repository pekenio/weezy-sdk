# Public API methods

Generated from the backend routes. Base URL: `https://api.weezy.app/client/api/v1`.

## sms

| JavaScript / TypeScript | Python | HTTP | Route |
| --- | --- | --- | --- |
| `sms.balance` | `sms.balance` | GET | `/sms/balance` |
| `sms.senders` | `sms.senders` | GET | `/sms/senders` |
| `sms.send` | `sms.send` | POST | `/sms/send` |
| `sms.sendBulk` | `sms.send_bulk` | POST | `/sms/send-bulk` |
| `sms.status` | `sms.status` | GET | `/sms/status/{message_x_id}` |
| `sms.optOuts` | `sms.opt_outs` | POST | `/sms/opt-outs` |
