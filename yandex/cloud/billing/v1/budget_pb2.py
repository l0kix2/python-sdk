# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/billing/v1/budget.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$yandex/cloud/billing/v1/budget.proto\x12\x17yandex.cloud.billing.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\x86\x03\n\x06\x42udget\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1a\n\x12\x62illing_account_id\x18\x04 \x01(\t\x12\x35\n\x06status\x18\x05 \x01(\x0e\x32%.yandex.cloud.billing.v1.BudgetStatus\x12>\n\x0b\x63ost_budget\x18\x06 \x01(\x0b\x32\'.yandex.cloud.billing.v1.CostBudgetSpecH\x00\x12\x44\n\x0e\x65xpense_budget\x18\x07 \x01(\x0b\x32*.yandex.cloud.billing.v1.ExpenseBudgetSpecH\x00\x12\x44\n\x0e\x62\x61lance_budget\x18\x08 \x01(\x0b\x32*.yandex.cloud.billing.v1.BalanceBudgetSpecH\x00\x42\x13\n\x0b\x62udget_spec\x12\x04\xc0\xc1\x31\x01\"\xc2\x02\n\x0e\x43ostBudgetSpec\x12\x0e\n\x06\x61mount\x18\x01 \x01(\t\x12%\n\x1dnotification_user_account_ids\x18\x02 \x03(\t\x12?\n\x0fthreshold_rules\x18\x03 \x03(\x0b\x32&.yandex.cloud.billing.v1.ThresholdRule\x12:\n\x06\x66ilter\x18\x04 \x01(\x0b\x32*.yandex.cloud.billing.v1.ConsumptionFilter\x12@\n\x0creset_period\x18\x05 \x01(\x0e\x32(.yandex.cloud.billing.v1.ResetPeriodTypeH\x00\x12\x14\n\nstart_date\x18\x06 \x01(\tH\x00\x12\x10\n\x08\x65nd_date\x18\x07 \x01(\tB\x12\n\nstart_type\x12\x04\xc0\xc1\x31\x01\"\xc5\x02\n\x11\x45xpenseBudgetSpec\x12\x0e\n\x06\x61mount\x18\x01 \x01(\t\x12%\n\x1dnotification_user_account_ids\x18\x02 \x03(\t\x12?\n\x0fthreshold_rules\x18\x03 \x03(\x0b\x32&.yandex.cloud.billing.v1.ThresholdRule\x12:\n\x06\x66ilter\x18\x04 \x01(\x0b\x32*.yandex.cloud.billing.v1.ConsumptionFilter\x12@\n\x0creset_period\x18\x05 \x01(\x0e\x32(.yandex.cloud.billing.v1.ResetPeriodTypeH\x00\x12\x14\n\nstart_date\x18\x06 \x01(\tH\x00\x12\x10\n\x08\x65nd_date\x18\x07 \x01(\tB\x12\n\nstart_type\x12\x04\xc0\xc1\x31\x01\"\xb1\x01\n\x11\x42\x61lanceBudgetSpec\x12\x0e\n\x06\x61mount\x18\x01 \x01(\t\x12%\n\x1dnotification_user_account_ids\x18\x02 \x03(\t\x12?\n\x0fthreshold_rules\x18\x03 \x03(\x0b\x32&.yandex.cloud.billing.v1.ThresholdRule\x12\x12\n\nstart_date\x18\x04 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x05 \x01(\t\"\x7f\n\x11\x43onsumptionFilter\x12\x13\n\x0bservice_ids\x18\x01 \x03(\t\x12U\n\x15\x63loud_folders_filters\x18\x02 \x03(\x0b\x32\x36.yandex.cloud.billing.v1.CloudFoldersConsumptionFilter\"E\n\x1d\x43loudFoldersConsumptionFilter\x12\x10\n\x08\x63loud_id\x18\x01 \x01(\t\x12\x12\n\nfolder_ids\x18\x02 \x03(\t\"|\n\rThresholdRule\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.yandex.cloud.billing.v1.ThresholdType\x12\x0e\n\x06\x61mount\x18\x02 \x01(\t\x12%\n\x1dnotification_user_account_ids\x18\x03 \x03(\t*U\n\x0c\x42udgetStatus\x12\x1d\n\x19\x42UDGET_STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08\x46INISHED\x10\x03*\\\n\x0fResetPeriodType\x12!\n\x1dRESET_PERIOD_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07MONTHLY\x10\x01\x12\x0b\n\x07QUARTER\x10\x02\x12\x0c\n\x08\x41NNUALLY\x10\x03*H\n\rThresholdType\x12\x1e\n\x1aTHRESHOLD_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PERCENT\x10\x01\x12\n\n\x06\x41MOUNT\x10\x02\x42\x62\n\x1byandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billingb\x06proto3')

_BUDGETSTATUS = DESCRIPTOR.enum_types_by_name['BudgetStatus']
BudgetStatus = enum_type_wrapper.EnumTypeWrapper(_BUDGETSTATUS)
_RESETPERIODTYPE = DESCRIPTOR.enum_types_by_name['ResetPeriodType']
ResetPeriodType = enum_type_wrapper.EnumTypeWrapper(_RESETPERIODTYPE)
_THRESHOLDTYPE = DESCRIPTOR.enum_types_by_name['ThresholdType']
ThresholdType = enum_type_wrapper.EnumTypeWrapper(_THRESHOLDTYPE)
BUDGET_STATUS_UNSPECIFIED = 0
CREATING = 1
ACTIVE = 2
FINISHED = 3
RESET_PERIOD_TYPE_UNSPECIFIED = 0
MONTHLY = 1
QUARTER = 2
ANNUALLY = 3
THRESHOLD_TYPE_UNSPECIFIED = 0
PERCENT = 1
AMOUNT = 2


_BUDGET = DESCRIPTOR.message_types_by_name['Budget']
_COSTBUDGETSPEC = DESCRIPTOR.message_types_by_name['CostBudgetSpec']
_EXPENSEBUDGETSPEC = DESCRIPTOR.message_types_by_name['ExpenseBudgetSpec']
_BALANCEBUDGETSPEC = DESCRIPTOR.message_types_by_name['BalanceBudgetSpec']
_CONSUMPTIONFILTER = DESCRIPTOR.message_types_by_name['ConsumptionFilter']
_CLOUDFOLDERSCONSUMPTIONFILTER = DESCRIPTOR.message_types_by_name['CloudFoldersConsumptionFilter']
_THRESHOLDRULE = DESCRIPTOR.message_types_by_name['ThresholdRule']
Budget = _reflection.GeneratedProtocolMessageType('Budget', (_message.Message,), {
  'DESCRIPTOR' : _BUDGET,
  '__module__' : 'yandex.cloud.billing.v1.budget_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.Budget)
  })
_sym_db.RegisterMessage(Budget)

CostBudgetSpec = _reflection.GeneratedProtocolMessageType('CostBudgetSpec', (_message.Message,), {
  'DESCRIPTOR' : _COSTBUDGETSPEC,
  '__module__' : 'yandex.cloud.billing.v1.budget_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.CostBudgetSpec)
  })
_sym_db.RegisterMessage(CostBudgetSpec)

ExpenseBudgetSpec = _reflection.GeneratedProtocolMessageType('ExpenseBudgetSpec', (_message.Message,), {
  'DESCRIPTOR' : _EXPENSEBUDGETSPEC,
  '__module__' : 'yandex.cloud.billing.v1.budget_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.ExpenseBudgetSpec)
  })
_sym_db.RegisterMessage(ExpenseBudgetSpec)

BalanceBudgetSpec = _reflection.GeneratedProtocolMessageType('BalanceBudgetSpec', (_message.Message,), {
  'DESCRIPTOR' : _BALANCEBUDGETSPEC,
  '__module__' : 'yandex.cloud.billing.v1.budget_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.BalanceBudgetSpec)
  })
_sym_db.RegisterMessage(BalanceBudgetSpec)

ConsumptionFilter = _reflection.GeneratedProtocolMessageType('ConsumptionFilter', (_message.Message,), {
  'DESCRIPTOR' : _CONSUMPTIONFILTER,
  '__module__' : 'yandex.cloud.billing.v1.budget_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.ConsumptionFilter)
  })
_sym_db.RegisterMessage(ConsumptionFilter)

CloudFoldersConsumptionFilter = _reflection.GeneratedProtocolMessageType('CloudFoldersConsumptionFilter', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDFOLDERSCONSUMPTIONFILTER,
  '__module__' : 'yandex.cloud.billing.v1.budget_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.CloudFoldersConsumptionFilter)
  })
_sym_db.RegisterMessage(CloudFoldersConsumptionFilter)

ThresholdRule = _reflection.GeneratedProtocolMessageType('ThresholdRule', (_message.Message,), {
  'DESCRIPTOR' : _THRESHOLDRULE,
  '__module__' : 'yandex.cloud.billing.v1.budget_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.ThresholdRule)
  })
_sym_db.RegisterMessage(ThresholdRule)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033yandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billing'
  _BUDGET.oneofs_by_name['budget_spec']._options = None
  _BUDGET.oneofs_by_name['budget_spec']._serialized_options = b'\300\3011\001'
  _COSTBUDGETSPEC.oneofs_by_name['start_type']._options = None
  _COSTBUDGETSPEC.oneofs_by_name['start_type']._serialized_options = b'\300\3011\001'
  _EXPENSEBUDGETSPEC.oneofs_by_name['start_type']._options = None
  _EXPENSEBUDGETSPEC.oneofs_by_name['start_type']._serialized_options = b'\300\3011\001'
  _BUDGETSTATUS._serialized_start=1681
  _BUDGETSTATUS._serialized_end=1766
  _RESETPERIODTYPE._serialized_start=1768
  _RESETPERIODTYPE._serialized_end=1860
  _THRESHOLDTYPE._serialized_start=1862
  _THRESHOLDTYPE._serialized_end=1934
  _BUDGET._serialized_start=130
  _BUDGET._serialized_end=520
  _COSTBUDGETSPEC._serialized_start=523
  _COSTBUDGETSPEC._serialized_end=845
  _EXPENSEBUDGETSPEC._serialized_start=848
  _EXPENSEBUDGETSPEC._serialized_end=1173
  _BALANCEBUDGETSPEC._serialized_start=1176
  _BALANCEBUDGETSPEC._serialized_end=1353
  _CONSUMPTIONFILTER._serialized_start=1355
  _CONSUMPTIONFILTER._serialized_end=1482
  _CLOUDFOLDERSCONSUMPTIONFILTER._serialized_start=1484
  _CLOUDFOLDERSCONSUMPTIONFILTER._serialized_end=1553
  _THRESHOLDRULE._serialized_start=1555
  _THRESHOLDRULE._serialized_end=1679
# @@protoc_insertion_point(module_scope)
