"""Run with the backend virtualenv and PYTHONPATH=weezy-api-python/api."""
import importlib
import json
from pathlib import Path
from fastapi import FastAPI
from fastapi.routing import APIRoute

root = Path(__file__).resolve().parents[1]
backend = root.parent / 'weezy-api-python/api/backend/app/client/api/v1'
app = FastAPI()
for file in sorted(backend.glob('*.py')):
    if file.stem in {'__init__', 'webhooks'}:
        continue
    module = importlib.import_module(f'backend.app.client.api.v1.{file.stem}')
    app.include_router(module.router)
schema = app.openapi()
for route in app.routes:
    if isinstance(route, APIRoute) and route.path in schema['paths']:
        for method in route.methods:
            schema['paths'][route.path][method.lower()]['x-sdk-method'] = route.endpoint.__name__
# Include precise data contracts for the SMS envelope responses.
from backend.app.user.schema.sms import SmsMessageOut, SmsBulkSendOut
from backend.app.user.schema.wallet import WalletOut
for model in (SmsMessageOut, SmsBulkSendOut, WalletOut):
    result = model.model_json_schema(ref_template='#/components/schemas/{model}')
    schema['components']['schemas'].update(result.pop('$defs', {}))
    schema['components']['schemas'][model.__name__] = result
(root / 'openapi.json').write_text(json.dumps(schema, ensure_ascii=False, indent=2) + '\n')
print(f'Exported {len(schema["paths"])} public paths')
