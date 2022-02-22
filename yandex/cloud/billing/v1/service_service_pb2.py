# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/billing/v1/service_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.billing.v1 import service_pb2 as yandex_dot_cloud_dot_billing_dot_v1_dot_service__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/billing/v1/service_service.proto\x12\x17yandex.cloud.billing.v1\x1a\x1cgoogle/api/annotations.proto\x1a%yandex/cloud/billing/v1/service.proto\x1a\x1dyandex/cloud/validation.proto\"-\n\x11GetServiceRequest\x12\x18\n\x02id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"o\n\x13ListServicesRequest\x12\x1a\n\x06\x66ilter\x18\x01 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"c\n\x14ListServicesResponse\x12\x32\n\x08services\x18\x01 \x03(\x0b\x32 .yandex.cloud.billing.v1.Service\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x8c\x02\n\x0eServiceService\x12v\n\x03Get\x12*.yandex.cloud.billing.v1.GetServiceRequest\x1a .yandex.cloud.billing.v1.Service\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/billing/v1/services/{id}\x12\x81\x01\n\x04List\x12,.yandex.cloud.billing.v1.ListServicesRequest\x1a-.yandex.cloud.billing.v1.ListServicesResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/billing/v1/servicesBb\n\x1byandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billingb\x06proto3')



_GETSERVICEREQUEST = DESCRIPTOR.message_types_by_name['GetServiceRequest']
_LISTSERVICESREQUEST = DESCRIPTOR.message_types_by_name['ListServicesRequest']
_LISTSERVICESRESPONSE = DESCRIPTOR.message_types_by_name['ListServicesResponse']
GetServiceRequest = _reflection.GeneratedProtocolMessageType('GetServiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVICEREQUEST,
  '__module__' : 'yandex.cloud.billing.v1.service_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.GetServiceRequest)
  })
_sym_db.RegisterMessage(GetServiceRequest)

ListServicesRequest = _reflection.GeneratedProtocolMessageType('ListServicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTSERVICESREQUEST,
  '__module__' : 'yandex.cloud.billing.v1.service_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.ListServicesRequest)
  })
_sym_db.RegisterMessage(ListServicesRequest)

ListServicesResponse = _reflection.GeneratedProtocolMessageType('ListServicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSERVICESRESPONSE,
  '__module__' : 'yandex.cloud.billing.v1.service_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.billing.v1.ListServicesResponse)
  })
_sym_db.RegisterMessage(ListServicesResponse)

_SERVICESERVICE = DESCRIPTOR.services_by_name['ServiceService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033yandex.cloud.api.billing.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/billing/v1;billing'
  _GETSERVICEREQUEST.fields_by_name['id']._options = None
  _GETSERVICEREQUEST.fields_by_name['id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTSERVICESREQUEST.fields_by_name['filter']._options = None
  _LISTSERVICESREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTSERVICESREQUEST.fields_by_name['page_size']._options = None
  _LISTSERVICESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTSERVICESREQUEST.fields_by_name['page_token']._options = None
  _LISTSERVICESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _SERVICESERVICE.methods_by_name['Get']._options = None
  _SERVICESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\033\022\031/billing/v1/services/{id}'
  _SERVICESERVICE.methods_by_name['List']._options = None
  _SERVICESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\026\022\024/billing/v1/services'
  _GETSERVICEREQUEST._serialized_start=174
  _GETSERVICEREQUEST._serialized_end=219
  _LISTSERVICESREQUEST._serialized_start=221
  _LISTSERVICESREQUEST._serialized_end=332
  _LISTSERVICESRESPONSE._serialized_start=334
  _LISTSERVICESRESPONSE._serialized_end=433
  _SERVICESERVICE._serialized_start=436
  _SERVICESERVICE._serialized_end=704
# @@protoc_insertion_point(module_scope)
