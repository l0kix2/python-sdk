# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/billing/v1/billing_account.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/billing/v1/billing_account.proto',
  package='yandex.cloud.billing.v1',
  syntax='proto3',
  serialized_options=b'\n\033yandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billing',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-yandex/cloud/billing/v1/billing_account.proto\x12\x17yandex.cloud.billing.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa3\x01\n\x0e\x42illingAccount\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0c\x63ountry_code\x18\x04 \x01(\t\x12\x10\n\x08\x63urrency\x18\x05 \x01(\t\x12\x0e\n\x06\x61\x63tive\x18\x06 \x01(\x08\x12\x0f\n\x07\x62\x61lance\x18\x07 \x01(\tBb\n\x1byandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billingb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_BILLINGACCOUNT = _descriptor.Descriptor(
  name='BillingAccount',
  full_name='yandex.cloud.billing.v1.BillingAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.billing.v1.BillingAccount.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.billing.v1.BillingAccount.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.billing.v1.BillingAccount.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='yandex.cloud.billing.v1.BillingAccount.country_code', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currency', full_name='yandex.cloud.billing.v1.BillingAccount.currency', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='active', full_name='yandex.cloud.billing.v1.BillingAccount.active', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='balance', full_name='yandex.cloud.billing.v1.BillingAccount.balance', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=271,
)

_BILLINGACCOUNT.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['BillingAccount'] = _BILLINGACCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BillingAccount = _reflection.GeneratedProtocolMessageType('BillingAccount', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGACCOUNT,
  '__module__' : 'yandex.cloud.billing.v1.billing_account_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.BillingAccount)
  })
_sym_db.RegisterMessage(BillingAccount)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
