// Generated.
import type * as T from "./types.js";
export interface SmsAPI {
  /** Remaining wallet balance */
  balance(): Promise<T.WalletOut>;
  /** Sender IDs available for sending */
  senders(): Promise<{ [key: string]: unknown }>;
  /** Send one SMS */
  send(body: T.SmsSendIn): Promise<T.SmsMessageOut>;
  /** Send the same SMS to many recipients */
  sendBulk(body: T.SmsBulkSendIn): Promise<T.SmsBulkSendOut>;
  /** Get the delivery status of one SMS */
  status(params: { message_x_id: string }): Promise<T.SmsMessageOut>;
  /** Unsubscribe numbers (excluded from all future sends) */
  optOuts(body: T.SmsOptOutIn): Promise<{ [key: string]: unknown }>;
}
export const operations = {
  "sms": {
    "balance": {
      "method": "GET",
      "path": "/sms/balance",
      "body": false,
      "params": [],
      "unwrap": true
    },
    "senders": {
      "method": "GET",
      "path": "/sms/senders",
      "body": false,
      "params": [],
      "unwrap": true
    },
    "send": {
      "method": "POST",
      "path": "/sms/send",
      "body": true,
      "params": [],
      "unwrap": true
    },
    "sendBulk": {
      "method": "POST",
      "path": "/sms/send-bulk",
      "body": true,
      "params": [],
      "unwrap": true
    },
    "status": {
      "method": "GET",
      "path": "/sms/status/{message_x_id}",
      "body": false,
      "params": [
        {
          "name": "message_x_id",
          "in": "path"
        }
      ],
      "unwrap": true
    },
    "optOuts": {
      "method": "POST",
      "path": "/sms/opt-outs",
      "body": true,
      "params": [],
      "unwrap": true
    }
  }
} as const;
