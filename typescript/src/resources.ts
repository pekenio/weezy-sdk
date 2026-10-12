// Generated.
import type * as T from "./types.js";
export interface SmsAPI {
  /** Remaining wallet balance */
  balance(): Promise<T.WalletOut>;
  /** Sender IDs available for sending */
  senders(): Promise<{ [key: string]: unknown }>;
  /** Queue one SMS for asynchronous delivery */
  send(body: T.SmsSendIn): Promise<T.SmsMessageOut>;
  /** Queue SMS for asynchronous delivery */
  sendBulk(body: T.SmsBulkSendIn): Promise<T.SmsBulkSendOut>;
  /** Get the delivery status of one SMS */
  status(params: { message_x_id: string }): Promise<T.SmsMessageOut>;
  /** Unsubscribe numbers (excluded from all future sends) */
  optOuts(body: T.SmsOptOutIn): Promise<{ [key: string]: unknown }>;
  /** Create a managed OTP challenge; real sends are billed normally */
  createOtp(body: T.SmsOtpCreateIn): Promise<{ [key: string]: unknown }>;
  /** Verify a one-use OTP code */
  verifyOtp(body: T.SmsOtpVerifyIn, params: { challenge_id: string }): Promise<{ [key: string]: unknown }>;
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
    },
    "createOtp": {
      "method": "POST",
      "path": "/sms/otp",
      "body": true,
      "params": [],
      "unwrap": true
    },
    "verifyOtp": {
      "method": "POST",
      "path": "/sms/otp/{challenge_id}/verify",
      "body": true,
      "params": [
        {
          "name": "challenge_id",
          "in": "path"
        }
      ],
      "unwrap": true
    }
  }
} as const;
