import json
import unittest
import httpx
from weezy import Weezy, AsyncWeezy, WeezyError

OPTIONS = dict(client_id="fixture", client_secret="test-only")

class ClientTest(unittest.TestCase):
    def test_sms_auth_body_and_unwrapped_result(self):
        def handler(request):
            self.assertEqual(request.url.path, "/client/api/v1/sms/send")
            self.assertEqual(request.headers['authorization'], 'Basic Zml4dHVyZTp0ZXN0LW9ubHk=')
            self.assertEqual(json.loads(request.content)['sender_name'], "WEEZY")
            return httpx.Response(200, json={"code": 200, "msg": "ok", "data": {"x_id": "fixture"}})
        with Weezy(**OPTIONS, transport=httpx.MockTransport(handler)) as client:
            self.assertEqual(client.sms.send(body={"to": "+2250700000000", "body": "Bonjour", "sender_name": "WEEZY"})['x_id'], "fixture")

    def test_http_errors_are_not_retried(self):
        calls = []
        def handler(request):
            calls.append(request)
            return httpx.Response(429, headers={"x-request-id": "fixture-request"}, json={"msg": "Rate limited"})
        with Weezy(**OPTIONS, transport=httpx.MockTransport(handler)) as client:
            with self.assertRaises(WeezyError) as caught: client.sms.balance()
        self.assertEqual(caught.exception.status, 429)
        self.assertEqual(caught.exception.request_id, "fixture-request")
        self.assertEqual(len(calls), 1)

    def test_missing_resource_detail_without_retry(self):
        calls = []
        def handler(request):
            calls.append(request)
            return httpx.Response(404, headers={"x-request-id": "disabled-test"}, json={"detail": "Resource unavailable"})
        with Weezy(**OPTIONS, transport=httpx.MockTransport(handler)) as client:
            with self.assertRaisesRegex(WeezyError, "Resource unavailable") as caught:
                client.sms.status(message_x_id="missing")
        self.assertEqual(caught.exception.status, 404)
        self.assertEqual(caught.exception.request_id, "disabled-test")
        self.assertEqual(len(calls), 1)

    def test_sms_only_public_resources(self):
        with Weezy(**OPTIONS) as client:
            resources = [name for name in vars(client) if not name.startswith("_")]
            self.assertEqual(resources, ["sms"])
            methods = [name for name in vars(type(client.sms)) if not name.startswith("_")]
            self.assertEqual(sorted(methods), ["balance", "opt_outs", "send", "send_bulk", "senders", "status"])

    def test_timeout(self):
        def handler(request): raise httpx.ReadTimeout("timeout", request=request)
        with Weezy(**OPTIONS, transport=httpx.MockTransport(handler)) as client:
            with self.assertRaisesRegex(WeezyError, "timed out"): client.sms.balance()

    def test_invalid_json_and_logical_errors(self):
        for response in (httpx.Response(502, text="<html>"), httpx.Response(200, json={"code": 403, "msg": "Forbidden"})):
            with Weezy(**OPTIONS, transport=httpx.MockTransport(lambda request: response)) as client:
                with self.assertRaises(WeezyError): client.sms.balance()

    def test_redirect_does_not_forward_credentials(self):
        calls = []
        def handler(request):
            calls.append(request)
            return httpx.Response(302, headers={"location": "https://other.example"}, json={})
        with Weezy(**OPTIONS, transport=httpx.MockTransport(handler)) as client:
            with self.assertRaises(WeezyError): client.sms.balance()
        self.assertEqual(len(calls), 1)

    def test_invalid_configuration_and_path(self):
        for url in ("file:///tmp", "https://key:secret@example.com", "https://example.com?q=test"):
            with self.assertRaises(ValueError): Weezy(**OPTIONS, base_url=url)
        with Weezy(**OPTIONS) as client:
            with self.assertRaises(ValueError): client.sms.status(message_x_id="..")

class AsyncClientTest(unittest.IsolatedAsyncioTestCase):
    async def test_async_sms(self):
        async def handler(request):
            if request.url.path.endswith('/sms/balance'): return httpx.Response(200, json={"code": 200, "msg": "ok", "data": {"currency": "EUR", "balance": 5.0, "total_topped_up": 10.0, "total_spent": 4.973, "unit": "point"}})
            return httpx.Response(200, json={"status": True})
        async with AsyncWeezy(**OPTIONS, transport=httpx.MockTransport(handler)) as client:
            wallet = await client.sms.balance()
            self.assertEqual(wallet["balance"], 5.0)
            self.assertEqual(wallet["total_spent"], 4.973)
            self.assertEqual(wallet["unit"], "point")
