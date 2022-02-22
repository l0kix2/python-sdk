# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cdn/v1/provider_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/cdn/v1/provider_service.proto\x12\x13yandex.cloud.cdn.v1\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"_\n\x17\x41\x63tivateProviderRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12#\n\rprovider_type\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\";\n\x18\x41\x63tivateProviderMetadata\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"@\n\x1dListActivatedProvidersRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"3\n\x1eListActivatedProvidersResponse\x12\x11\n\tproviders\x18\x01 \x03(\t2\xe1\x02\n\x0fProviderService\x12\xb7\x01\n\x08\x41\x63tivate\x12,.yandex.cloud.cdn.v1.ActivateProviderRequest\x1a!.yandex.cloud.operation.Operation\"Z\x82\xd3\xe4\x93\x02\x1f\"\x1a/cdn/v1/providers:activate:\x01*\xb2\xd2*1\n\x18\x41\x63tivateProviderMetadata\x12\x15google.protobuf.Empty\x12\x93\x01\n\rListActivated\x12\x32.yandex.cloud.cdn.v1.ListActivatedProvidersRequest\x1a\x33.yandex.cloud.cdn.v1.ListActivatedProvidersResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/cdn/v1/providersBV\n\x17yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdnb\x06proto3')



_ACTIVATEPROVIDERREQUEST = DESCRIPTOR.message_types_by_name['ActivateProviderRequest']
_ACTIVATEPROVIDERMETADATA = DESCRIPTOR.message_types_by_name['ActivateProviderMetadata']
_LISTACTIVATEDPROVIDERSREQUEST = DESCRIPTOR.message_types_by_name['ListActivatedProvidersRequest']
_LISTACTIVATEDPROVIDERSRESPONSE = DESCRIPTOR.message_types_by_name['ListActivatedProvidersResponse']
ActivateProviderRequest = _reflection.GeneratedProtocolMessageType('ActivateProviderRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATEPROVIDERREQUEST,
  '__module__' : 'yandex.cloud.cdn.v1.provider_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.ActivateProviderRequest)
  })
_sym_db.RegisterMessage(ActivateProviderRequest)

ActivateProviderMetadata = _reflection.GeneratedProtocolMessageType('ActivateProviderMetadata', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATEPROVIDERMETADATA,
  '__module__' : 'yandex.cloud.cdn.v1.provider_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.ActivateProviderMetadata)
  })
_sym_db.RegisterMessage(ActivateProviderMetadata)

ListActivatedProvidersRequest = _reflection.GeneratedProtocolMessageType('ListActivatedProvidersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTACTIVATEDPROVIDERSREQUEST,
  '__module__' : 'yandex.cloud.cdn.v1.provider_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.ListActivatedProvidersRequest)
  })
_sym_db.RegisterMessage(ListActivatedProvidersRequest)

ListActivatedProvidersResponse = _reflection.GeneratedProtocolMessageType('ListActivatedProvidersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTACTIVATEDPROVIDERSRESPONSE,
  '__module__' : 'yandex.cloud.cdn.v1.provider_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.ListActivatedProvidersResponse)
  })
_sym_db.RegisterMessage(ListActivatedProvidersResponse)

_PROVIDERSERVICE = DESCRIPTOR.services_by_name['ProviderService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdn'
  _ACTIVATEPROVIDERREQUEST.fields_by_name['folder_id']._options = None
  _ACTIVATEPROVIDERREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _ACTIVATEPROVIDERREQUEST.fields_by_name['provider_type']._options = None
  _ACTIVATEPROVIDERREQUEST.fields_by_name['provider_type']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _ACTIVATEPROVIDERMETADATA.fields_by_name['folder_id']._options = None
  _ACTIVATEPROVIDERMETADATA.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTACTIVATEDPROVIDERSREQUEST.fields_by_name['folder_id']._options = None
  _LISTACTIVATEDPROVIDERSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _PROVIDERSERVICE.methods_by_name['Activate']._options = None
  _PROVIDERSERVICE.methods_by_name['Activate']._serialized_options = b'\202\323\344\223\002\037\"\032/cdn/v1/providers:activate:\001*\262\322*1\n\030ActivateProviderMetadata\022\025google.protobuf.Empty'
  _PROVIDERSERVICE.methods_by_name['ListActivated']._options = None
  _PROVIDERSERVICE.methods_by_name['ListActivated']._serialized_options = b'\202\323\344\223\002\023\022\021/cdn/v1/providers'
  _ACTIVATEPROVIDERREQUEST._serialized_start=202
  _ACTIVATEPROVIDERREQUEST._serialized_end=297
  _ACTIVATEPROVIDERMETADATA._serialized_start=299
  _ACTIVATEPROVIDERMETADATA._serialized_end=358
  _LISTACTIVATEDPROVIDERSREQUEST._serialized_start=360
  _LISTACTIVATEDPROVIDERSREQUEST._serialized_end=424
  _LISTACTIVATEDPROVIDERSRESPONSE._serialized_start=426
  _LISTACTIVATEDPROVIDERSRESPONSE._serialized_end=477
  _PROVIDERSERVICE._serialized_start=480
  _PROVIDERSERVICE._serialized_end=833
# @@protoc_insertion_point(module_scope)
