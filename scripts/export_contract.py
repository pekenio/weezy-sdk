"""Run with the backend virtualenv and PYTHONPATH=weezy-api-python/api."""
import importlib
import json
from pathlib import Path
from fastapi import FastAPI
from fastapi.routing import APIRoute

root = Path(__file__).resolve().parents[1]
backend = root.parent / 'weezy-api-python/api/backend/app/client/api/v1'
app = FastAPI()
module = importlib.import_module('backend.app.client.api.v1.sms')
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
# L'API developpeur renvoie les montants en points decimaux (1 point = 1 EUR) avec unit="point",
# alors que ces schemas internes sont en milli-points entiers : on ajuste le contrat public.
schemas = schema['components']['schemas']
price = "Price in points (1 point = 1 EUR, up to 3 decimals)"
amount = "Amount in points (1 point = 1 EUR, up to 3 decimals)"
unit = {"const": "point", "default": "point", "title": "Unit", "type": "string",
        "description": "Monetary unit of the amounts in this object: always \"point\" (1 point = 1 EUR)."}
for field in ('unit_price', 'cost'):
    schemas['SmsMessageOut']['properties'][field].update(type='number', description=price)
for field in ('amount_reserved', 'amount_refunded'):
    schemas['SmsBatchOut']['properties'][field].update(type='number', description=amount)
wallet = schemas['WalletOut']['properties']
for field in ('balance', 'total_topped_up', 'total_spent'):
    wallet[field].update(type='number', description=amount)
wallet['low_balance_threshold']['anyOf'][0]['type'] = 'number'
wallet['low_balance_threshold']['description'] = amount
for name in ('SmsMessageOut', 'SmsBatchOut', 'WalletOut'):
    schemas[name]['properties']['unit'] = dict(unit)
    if 'unit' not in schemas[name]['required']:
        schemas[name]['required'].append('unit')
# Keep only schemas reachable from SMS operations and explicit response contracts.
needed = {'SmsMessageOut', 'SmsBulkSendOut', 'WalletOut'}
def collect(value):
    if isinstance(value, dict):
        if '$ref' in value:
            needed.add(value['$ref'].rsplit('/', 1)[-1])
        for item in value.values(): collect(item)
    elif isinstance(value, list):
        for item in value: collect(item)
collect(schema['paths'])
visited = set()
while needed - visited:
    name = sorted(needed - visited)[0]
    visited.add(name)
    collect(schemas[name])
schema['components']['schemas'] = {name: value for name, value in schemas.items() if name in needed}
(root / 'openapi.json').write_text(json.dumps(schema, ensure_ascii=False, indent=2) + '\n')
print(f'Exported {len(schema["paths"])} public paths')
