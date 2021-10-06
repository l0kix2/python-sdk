# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/billing/v1/billing_account_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.billing.v1 import billing_account_pb2 as yandex_dot_cloud_dot_billing_dot_v1_dot_billing__account__pb2
from yandex.cloud.billing.v1 import billable_object_pb2 as yandex_dot_cloud_dot_billing_dot_v1_dot_billable__object__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/billing/v1/billing_account_service.proto',
  package='yandex.cloud.billing.v1',
  syntax='proto3',
  serialized_options=b'\n\033yandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billing',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5yandex/cloud/billing/v1/billing_account_service.proto\x12\x17yandex.cloud.billing.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/access/access.proto\x1a-yandex/cloud/billing/v1/billing_account.proto\x1a-yandex/cloud/billing/v1/billable_object.proto\x1a&yandex/cloud/operation/operation.proto\x1a yandex/cloud/api/operation.proto\x1a\x1dyandex/cloud/validation.proto\"4\n\x18GetBillingAccountRequest\x12\x18\n\x02id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"Z\n\x1aListBillingAccountsRequest\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"y\n\x1bListBillingAccountsResponse\x12\x41\n\x10\x62illing_accounts\x18\x01 \x03(\x0b\x32\'.yandex.cloud.billing.v1.BillingAccount\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x8b\x01\n!ListBillableObjectBindingsRequest\x12(\n\x12\x62illing_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"\x8f\x01\n\"ListBillableObjectBindingsResponse\x12P\n\x18\x62illable_object_bindings\x18\x01 \x03(\x0b\x32..yandex.cloud.billing.v1.BillableObjectBinding\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x87\x01\n\x19\x42indBillableObjectRequest\x12(\n\x12\x62illing_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12@\n\x0f\x62illable_object\x18\x02 \x01(\x0b\x32\'.yandex.cloud.billing.v1.BillableObject\"8\n\x1a\x42indBillableObjectMetadata\x12\x1a\n\x12\x62illable_object_id\x18\x01 \x01(\t2\xd9\t\n\x15\x42illingAccountService\x12\x8b\x01\n\x03Get\x12\x31.yandex.cloud.billing.v1.GetBillingAccountRequest\x1a\'.yandex.cloud.billing.v1.BillingAccount\"(\x82\xd3\xe4\x93\x02\"\x12 /billing/v1/billingAccounts/{id}\x12\x96\x01\n\x04List\x12\x33.yandex.cloud.billing.v1.ListBillingAccountsRequest\x1a\x34.yandex.cloud.billing.v1.ListBillingAccountsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/billing/v1/billingAccounts\x12\xe6\x01\n\x1aListBillableObjectBindings\x12:.yandex.cloud.billing.v1.ListBillableObjectBindingsRequest\x1a;.yandex.cloud.billing.v1.ListBillableObjectBindingsResponse\"O\x82\xd3\xe4\x93\x02I\x12G/billing/v1/billingAccounts/{billing_account_id}/billableObjectBindings\x12\xf7\x01\n\x12\x42indBillableObject\x12\x32.yandex.cloud.billing.v1.BindBillableObjectRequest\x1a!.yandex.cloud.operation.Operation\"\x89\x01\x82\xd3\xe4\x93\x02L\"G/billing/v1/billingAccounts/{billing_account_id}/billableObjectBindings:\x01*\xb2\xd2*3\n\x1a\x42indBillableObjectMetadata\x12\x15\x42illableObjectBinding\x12\xbb\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"D\x82\xd3\xe4\x93\x02>\x12</billing/v1/billingAccounts/{resource_id}:listAccessBindings\x12\xf7\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x89\x01\x82\xd3\xe4\x93\x02\x43\x32>/billing/v1/billingAccounts/{resource_id}:updateAccessBindings:\x01*\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.EmptyBb\n\x1byandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billingb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,yandex_dot_cloud_dot_access_dot_access__pb2.DESCRIPTOR,yandex_dot_cloud_dot_billing_dot_v1_dot_billing__account__pb2.DESCRIPTOR,yandex_dot_cloud_dot_billing_dot_v1_dot_billable__object__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETBILLINGACCOUNTREQUEST = _descriptor.Descriptor(
  name='GetBillingAccountRequest',
  full_name='yandex.cloud.billing.v1.GetBillingAccountRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.billing.v1.GetBillingAccountRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=345,
  serialized_end=397,
)


_LISTBILLINGACCOUNTSREQUEST = _descriptor.Descriptor(
  name='ListBillingAccountsRequest',
  full_name='yandex.cloud.billing.v1.ListBillingAccountsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.billing.v1.ListBillingAccountsRequest.page_size', index=0,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\006<=1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.billing.v1.ListBillingAccountsRequest.page_token', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=399,
  serialized_end=489,
)


_LISTBILLINGACCOUNTSRESPONSE = _descriptor.Descriptor(
  name='ListBillingAccountsResponse',
  full_name='yandex.cloud.billing.v1.ListBillingAccountsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='billing_accounts', full_name='yandex.cloud.billing.v1.ListBillingAccountsResponse.billing_accounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.billing.v1.ListBillingAccountsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=491,
  serialized_end=612,
)


_LISTBILLABLEOBJECTBINDINGSREQUEST = _descriptor.Descriptor(
  name='ListBillableObjectBindingsRequest',
  full_name='yandex.cloud.billing.v1.ListBillableObjectBindingsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='billing_account_id', full_name='yandex.cloud.billing.v1.ListBillableObjectBindingsRequest.billing_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='yandex.cloud.billing.v1.ListBillableObjectBindingsRequest.page_size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\006<=1000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='yandex.cloud.billing.v1.ListBillableObjectBindingsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3101\005<=100', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=615,
  serialized_end=754,
)


_LISTBILLABLEOBJECTBINDINGSRESPONSE = _descriptor.Descriptor(
  name='ListBillableObjectBindingsResponse',
  full_name='yandex.cloud.billing.v1.ListBillableObjectBindingsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='billable_object_bindings', full_name='yandex.cloud.billing.v1.ListBillableObjectBindingsResponse.billable_object_bindings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='yandex.cloud.billing.v1.ListBillableObjectBindingsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=757,
  serialized_end=900,
)


_BINDBILLABLEOBJECTREQUEST = _descriptor.Descriptor(
  name='BindBillableObjectRequest',
  full_name='yandex.cloud.billing.v1.BindBillableObjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='billing_account_id', full_name='yandex.cloud.billing.v1.BindBillableObjectRequest.billing_account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='billable_object', full_name='yandex.cloud.billing.v1.BindBillableObjectRequest.billable_object', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=903,
  serialized_end=1038,
)


_BINDBILLABLEOBJECTMETADATA = _descriptor.Descriptor(
  name='BindBillableObjectMetadata',
  full_name='yandex.cloud.billing.v1.BindBillableObjectMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='billable_object_id', full_name='yandex.cloud.billing.v1.BindBillableObjectMetadata.billable_object_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=1040,
  serialized_end=1096,
)

_LISTBILLINGACCOUNTSRESPONSE.fields_by_name['billing_accounts'].message_type = yandex_dot_cloud_dot_billing_dot_v1_dot_billing__account__pb2._BILLINGACCOUNT
_LISTBILLABLEOBJECTBINDINGSRESPONSE.fields_by_name['billable_object_bindings'].message_type = yandex_dot_cloud_dot_billing_dot_v1_dot_billable__object__pb2._BILLABLEOBJECTBINDING
_BINDBILLABLEOBJECTREQUEST.fields_by_name['billable_object'].message_type = yandex_dot_cloud_dot_billing_dot_v1_dot_billable__object__pb2._BILLABLEOBJECT
DESCRIPTOR.message_types_by_name['GetBillingAccountRequest'] = _GETBILLINGACCOUNTREQUEST
DESCRIPTOR.message_types_by_name['ListBillingAccountsRequest'] = _LISTBILLINGACCOUNTSREQUEST
DESCRIPTOR.message_types_by_name['ListBillingAccountsResponse'] = _LISTBILLINGACCOUNTSRESPONSE
DESCRIPTOR.message_types_by_name['ListBillableObjectBindingsRequest'] = _LISTBILLABLEOBJECTBINDINGSREQUEST
DESCRIPTOR.message_types_by_name['ListBillableObjectBindingsResponse'] = _LISTBILLABLEOBJECTBINDINGSRESPONSE
DESCRIPTOR.message_types_by_name['BindBillableObjectRequest'] = _BINDBILLABLEOBJECTREQUEST
DESCRIPTOR.message_types_by_name['BindBillableObjectMetadata'] = _BINDBILLABLEOBJECTMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetBillingAccountRequest = _reflection.GeneratedProtocolMessageType('GetBillingAccountRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBILLINGACCOUNTREQUEST,
  '__module__' : 'yandex.cloud.billing.v1.billing_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.GetBillingAccountRequest)
  })
_sym_db.RegisterMessage(GetBillingAccountRequest)

ListBillingAccountsRequest = _reflection.GeneratedProtocolMessageType('ListBillingAccountsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBILLINGACCOUNTSREQUEST,
  '__module__' : 'yandex.cloud.billing.v1.billing_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.ListBillingAccountsRequest)
  })
_sym_db.RegisterMessage(ListBillingAccountsRequest)

ListBillingAccountsResponse = _reflection.GeneratedProtocolMessageType('ListBillingAccountsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBILLINGACCOUNTSRESPONSE,
  '__module__' : 'yandex.cloud.billing.v1.billing_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.ListBillingAccountsResponse)
  })
_sym_db.RegisterMessage(ListBillingAccountsResponse)

ListBillableObjectBindingsRequest = _reflection.GeneratedProtocolMessageType('ListBillableObjectBindingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBILLABLEOBJECTBINDINGSREQUEST,
  '__module__' : 'yandex.cloud.billing.v1.billing_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.ListBillableObjectBindingsRequest)
  })
_sym_db.RegisterMessage(ListBillableObjectBindingsRequest)

ListBillableObjectBindingsResponse = _reflection.GeneratedProtocolMessageType('ListBillableObjectBindingsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBILLABLEOBJECTBINDINGSRESPONSE,
  '__module__' : 'yandex.cloud.billing.v1.billing_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.ListBillableObjectBindingsResponse)
  })
_sym_db.RegisterMessage(ListBillableObjectBindingsResponse)

BindBillableObjectRequest = _reflection.GeneratedProtocolMessageType('BindBillableObjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _BINDBILLABLEOBJECTREQUEST,
  '__module__' : 'yandex.cloud.billing.v1.billing_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.BindBillableObjectRequest)
  })
_sym_db.RegisterMessage(BindBillableObjectRequest)

BindBillableObjectMetadata = _reflection.GeneratedProtocolMessageType('BindBillableObjectMetadata', (_message.Message,), {
  'DESCRIPTOR' : _BINDBILLABLEOBJECTMETADATA,
  '__module__' : 'yandex.cloud.billing.v1.billing_account_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.BindBillableObjectMetadata)
  })
_sym_db.RegisterMessage(BindBillableObjectMetadata)


DESCRIPTOR._options = None
_GETBILLINGACCOUNTREQUEST.fields_by_name['id']._options = None
_LISTBILLINGACCOUNTSREQUEST.fields_by_name['page_size']._options = None
_LISTBILLINGACCOUNTSREQUEST.fields_by_name['page_token']._options = None
_LISTBILLABLEOBJECTBINDINGSREQUEST.fields_by_name['billing_account_id']._options = None
_LISTBILLABLEOBJECTBINDINGSREQUEST.fields_by_name['page_size']._options = None
_LISTBILLABLEOBJECTBINDINGSREQUEST.fields_by_name['page_token']._options = None
_BINDBILLABLEOBJECTREQUEST.fields_by_name['billing_account_id']._options = None

_BILLINGACCOUNTSERVICE = _descriptor.ServiceDescriptor(
  name='BillingAccountService',
  full_name='yandex.cloud.billing.v1.BillingAccountService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1099,
  serialized_end=2340,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.billing.v1.BillingAccountService.Get',
    index=0,
    containing_service=None,
    input_type=_GETBILLINGACCOUNTREQUEST,
    output_type=yandex_dot_cloud_dot_billing_dot_v1_dot_billing__account__pb2._BILLINGACCOUNT,
    serialized_options=b'\202\323\344\223\002\"\022 /billing/v1/billingAccounts/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.billing.v1.BillingAccountService.List',
    index=1,
    containing_service=None,
    input_type=_LISTBILLINGACCOUNTSREQUEST,
    output_type=_LISTBILLINGACCOUNTSRESPONSE,
    serialized_options=b'\202\323\344\223\002\035\022\033/billing/v1/billingAccounts',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListBillableObjectBindings',
    full_name='yandex.cloud.billing.v1.BillingAccountService.ListBillableObjectBindings',
    index=2,
    containing_service=None,
    input_type=_LISTBILLABLEOBJECTBINDINGSREQUEST,
    output_type=_LISTBILLABLEOBJECTBINDINGSRESPONSE,
    serialized_options=b'\202\323\344\223\002I\022G/billing/v1/billingAccounts/{billing_account_id}/billableObjectBindings',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BindBillableObject',
    full_name='yandex.cloud.billing.v1.BillingAccountService.BindBillableObject',
    index=3,
    containing_service=None,
    input_type=_BINDBILLABLEOBJECTREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002L\"G/billing/v1/billingAccounts/{billing_account_id}/billableObjectBindings:\001*\262\322*3\n\032BindBillableObjectMetadata\022\025BillableObjectBinding',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListAccessBindings',
    full_name='yandex.cloud.billing.v1.BillingAccountService.ListAccessBindings',
    index=4,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._LISTACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_access_dot_access__pb2._LISTACCESSBINDINGSRESPONSE,
    serialized_options=b'\202\323\344\223\002>\022</billing/v1/billingAccounts/{resource_id}:listAccessBindings',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAccessBindings',
    full_name='yandex.cloud.billing.v1.BillingAccountService.UpdateAccessBindings',
    index=5,
    containing_service=None,
    input_type=yandex_dot_cloud_dot_access_dot_access__pb2._UPDATEACCESSBINDINGSREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002C2>/billing/v1/billingAccounts/{resource_id}:updateAccessBindings:\001*\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BILLINGACCOUNTSERVICE)

DESCRIPTOR.services_by_name['BillingAccountService'] = _BILLINGACCOUNTSERVICE

# @@protoc_insertion_point(module_scope)
