"""Generated public API types."""
from typing import Any, Dict, List, Literal, Union, TypedDict, Required, NotRequired

HTTPValidationError = TypedDict('HTTPValidationError', {'detail': NotRequired[List['ValidationError']]})
ResponseModel = TypedDict('ResponseModel', {'code': NotRequired[int], 'msg': NotRequired[str], 'data': NotRequired[Union[Any, None]]})
SmsBulkSendIn = TypedDict('SmsBulkSendIn', {'recipients': Required[List[str]], 'body': Required[str], 'sender_name': Required[str], 'name': NotRequired[Union[str, None]]})
SmsOptOutIn = TypedDict('SmsOptOutIn', {'phones': Required[List[str]], 'reason': NotRequired[Union[str, None]], 'source': NotRequired[Literal['manual', 'import', 'reply']]})
SmsSendIn = TypedDict('SmsSendIn', {'test_mode': NotRequired[bool], 'to': Required[str], 'body': Required[str], 'sender_name': Required[str]})
ValidationError = TypedDict('ValidationError', {'loc': Required[List[Union[str, int]]], 'msg': Required[str], 'type': Required[str]})
SmsMessageOut = TypedDict('SmsMessageOut', {'x_id': Required[str], 'to': Required[str], 'body': Required[str], 'sender_name': Required[str], 'country_code': Required[str], 'encoding': Required[str], 'segments': Required[int], 'unit_price': Required[float], 'cost': Required[float], 'status': Required[str], 'error': NotRequired[Union[str, None]], 'refunded': NotRequired[bool], 'batch_x_id': NotRequired[Union[str, None]], 'source': Required[str], 'created_time': Required[str], 'sent_at': NotRequired[Union[str, None]], 'delivered_at': NotRequired[Union[str, None]], 'unit': Required[Literal['point']]})
SmsBatchOut = TypedDict('SmsBatchOut', {'x_id': Required[str], 'name': Required[str], 'body': Required[str], 'sender_name': Required[str], 'source': Required[str], 'status': Required[str], 'total_recipients': Required[int], 'sent_count': Required[int], 'failed_count': Required[int], 'amount_reserved': Required[float], 'amount_refunded': Required[float], 'created_time': Required[str], 'completed_at': NotRequired[Union[str, None]], 'unit': Required[Literal['point']]})
SmsBulkSendOut = TypedDict('SmsBulkSendOut', {'batch': Required['SmsBatchOut'], 'invalid_recipients': NotRequired[List[str]]})
WalletOut = TypedDict('WalletOut', {'currency': Required[str], 'balance': Required[float], 'total_topped_up': Required[float], 'total_spent': Required[float], 'display_currency': NotRequired[Union[str, None]], 'low_balance_threshold': NotRequired[Union[float, None]], 'unit': Required[Literal['point']]})
