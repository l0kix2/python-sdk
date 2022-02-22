# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/apploadbalancer/v1/http_router_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.apploadbalancer.v1 import http_router_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_http__router__pb2
from yandex.cloud.apploadbalancer.v1 import virtual_host_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_virtual__host__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9yandex/cloud/apploadbalancer/v1/http_router_service.proto\x12\x1fyandex.cloud.apploadbalancer.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x31yandex/cloud/apploadbalancer/v1/http_router.proto\x1a\x32yandex/cloud/apploadbalancer/v1/virtual_host.proto\x1a\x1dyandex/cloud/validation.proto\"4\n\x14GetHttpRouterRequest\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x8b\x01\n\x16ListHttpRoutersRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"u\n\x17ListHttpRoutersResponse\x12\x41\n\x0chttp_routers\x18\x01 \x03(\x0b\x32+.yandex.cloud.apploadbalancer.v1.HttpRouter\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"7\n\x17\x44\x65leteHttpRouterRequest\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"2\n\x18\x44\x65leteHttpRouterMetadata\x12\x16\n\x0ehttp_router_id\x18\x01 \x01(\t\"\xd8\x03\n\x17UpdateHttpRouterRequest\x12\x1c\n\x0ehttp_router_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x34\n\x04name\x18\x03 \x01(\tB&\xf2\xc7\x31\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x9d\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x44.yandex.cloud.apploadbalancer.v1.UpdateHttpRouterRequest.LabelsEntryBG\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x16\x12\x14[a-z][-_./\\@0-9a-z]*\x12\x43\n\rvirtual_hosts\x18\x06 \x03(\x0b\x32,.yandex.cloud.apploadbalancer.v1.VirtualHost\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x07\x10\x08\"2\n\x18UpdateHttpRouterMetadata\x12\x16\n\x0ehttp_router_id\x18\x01 \x01(\t\"\xa2\x03\n\x17\x43reateHttpRouterRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x34\n\x04name\x18\x02 \x01(\tB&\xf2\xc7\x31\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x9d\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x44.yandex.cloud.apploadbalancer.v1.CreateHttpRouterRequest.LabelsEntryBG\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x16\x12\x14[a-z][-_./\\@0-9a-z]*\x12\x43\n\rvirtual_hosts\x18\x05 \x03(\x0b\x32,.yandex.cloud.apploadbalancer.v1.VirtualHost\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\x06\x10\x07\"2\n\x18\x43reateHttpRouterMetadata\x12\x16\n\x0ehttp_router_id\x18\x01 \x01(\t\"\x85\x01\n\x1fListHttpRouterOperationsRequest\x12$\n\x0ehttp_router_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"r\n ListHttpRouterOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x9f\t\n\x11HttpRouterService\x12\xa3\x01\n\x03Get\x12\x35.yandex.cloud.apploadbalancer.v1.GetHttpRouterRequest\x1a+.yandex.cloud.apploadbalancer.v1.HttpRouter\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/apploadbalancer/v1/httpRouters/{http_router_id}\x12\xa2\x01\n\x04List\x12\x37.yandex.cloud.apploadbalancer.v1.ListHttpRoutersRequest\x1a\x38.yandex.cloud.apploadbalancer.v1.ListHttpRoutersResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/apploadbalancer/v1/httpRouters\x12\xbb\x01\n\x06\x43reate\x12\x38.yandex.cloud.apploadbalancer.v1.CreateHttpRouterRequest\x1a!.yandex.cloud.operation.Operation\"T\x82\xd3\xe4\x93\x02$\"\x1f/apploadbalancer/v1/httpRouters:\x01*\xb2\xd2*&\n\x18\x43reateHttpRouterMetadata\x12\nHttpRouter\x12\xcc\x01\n\x06Update\x12\x38.yandex.cloud.apploadbalancer.v1.UpdateHttpRouterRequest\x1a!.yandex.cloud.operation.Operation\"e\x82\xd3\xe4\x93\x02\x35\x32\x30/apploadbalancer/v1/httpRouters/{http_router_id}:\x01*\xb2\xd2*&\n\x18UpdateHttpRouterMetadata\x12\nHttpRouter\x12\xd4\x01\n\x06\x44\x65lete\x12\x38.yandex.cloud.apploadbalancer.v1.DeleteHttpRouterRequest\x1a!.yandex.cloud.operation.Operation\"m\x82\xd3\xe4\x93\x02\x32*0/apploadbalancer/v1/httpRouters/{http_router_id}\xb2\xd2*1\n\x18\x44\x65leteHttpRouterMetadata\x12\x15google.protobuf.Empty\x12\xda\x01\n\x0eListOperations\x12@.yandex.cloud.apploadbalancer.v1.ListHttpRouterOperationsRequest\x1a\x41.yandex.cloud.apploadbalancer.v1.ListHttpRouterOperationsResponse\"C\x82\xd3\xe4\x93\x02=\x12;/apploadbalancer/v1/httpRouters/{http_router_id}/operationsBz\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancerb\x06proto3')



_GETHTTPROUTERREQUEST = DESCRIPTOR.message_types_by_name['GetHttpRouterRequest']
_LISTHTTPROUTERSREQUEST = DESCRIPTOR.message_types_by_name['ListHttpRoutersRequest']
_LISTHTTPROUTERSRESPONSE = DESCRIPTOR.message_types_by_name['ListHttpRoutersResponse']
_DELETEHTTPROUTERREQUEST = DESCRIPTOR.message_types_by_name['DeleteHttpRouterRequest']
_DELETEHTTPROUTERMETADATA = DESCRIPTOR.message_types_by_name['DeleteHttpRouterMetadata']
_UPDATEHTTPROUTERREQUEST = DESCRIPTOR.message_types_by_name['UpdateHttpRouterRequest']
_UPDATEHTTPROUTERREQUEST_LABELSENTRY = _UPDATEHTTPROUTERREQUEST.nested_types_by_name['LabelsEntry']
_UPDATEHTTPROUTERMETADATA = DESCRIPTOR.message_types_by_name['UpdateHttpRouterMetadata']
_CREATEHTTPROUTERREQUEST = DESCRIPTOR.message_types_by_name['CreateHttpRouterRequest']
_CREATEHTTPROUTERREQUEST_LABELSENTRY = _CREATEHTTPROUTERREQUEST.nested_types_by_name['LabelsEntry']
_CREATEHTTPROUTERMETADATA = DESCRIPTOR.message_types_by_name['CreateHttpRouterMetadata']
_LISTHTTPROUTEROPERATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListHttpRouterOperationsRequest']
_LISTHTTPROUTEROPERATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListHttpRouterOperationsResponse']
GetHttpRouterRequest = _reflection.GeneratedProtocolMessageType('GetHttpRouterRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETHTTPROUTERREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.GetHttpRouterRequest)
  })
_sym_db.RegisterMessage(GetHttpRouterRequest)

ListHttpRoutersRequest = _reflection.GeneratedProtocolMessageType('ListHttpRoutersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTHTTPROUTERSREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.ListHttpRoutersRequest)
  })
_sym_db.RegisterMessage(ListHttpRoutersRequest)

ListHttpRoutersResponse = _reflection.GeneratedProtocolMessageType('ListHttpRoutersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTHTTPROUTERSRESPONSE,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.ListHttpRoutersResponse)
  })
_sym_db.RegisterMessage(ListHttpRoutersResponse)

DeleteHttpRouterRequest = _reflection.GeneratedProtocolMessageType('DeleteHttpRouterRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEHTTPROUTERREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.DeleteHttpRouterRequest)
  })
_sym_db.RegisterMessage(DeleteHttpRouterRequest)

DeleteHttpRouterMetadata = _reflection.GeneratedProtocolMessageType('DeleteHttpRouterMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEHTTPROUTERMETADATA,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.DeleteHttpRouterMetadata)
  })
_sym_db.RegisterMessage(DeleteHttpRouterMetadata)

UpdateHttpRouterRequest = _reflection.GeneratedProtocolMessageType('UpdateHttpRouterRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEHTTPROUTERREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.UpdateHttpRouterRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATEHTTPROUTERREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.UpdateHttpRouterRequest)
  })
_sym_db.RegisterMessage(UpdateHttpRouterRequest)
_sym_db.RegisterMessage(UpdateHttpRouterRequest.LabelsEntry)

UpdateHttpRouterMetadata = _reflection.GeneratedProtocolMessageType('UpdateHttpRouterMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEHTTPROUTERMETADATA,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.UpdateHttpRouterMetadata)
  })
_sym_db.RegisterMessage(UpdateHttpRouterMetadata)

CreateHttpRouterRequest = _reflection.GeneratedProtocolMessageType('CreateHttpRouterRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATEHTTPROUTERREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.CreateHttpRouterRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CREATEHTTPROUTERREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.CreateHttpRouterRequest)
  })
_sym_db.RegisterMessage(CreateHttpRouterRequest)
_sym_db.RegisterMessage(CreateHttpRouterRequest.LabelsEntry)

CreateHttpRouterMetadata = _reflection.GeneratedProtocolMessageType('CreateHttpRouterMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEHTTPROUTERMETADATA,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.CreateHttpRouterMetadata)
  })
_sym_db.RegisterMessage(CreateHttpRouterMetadata)

ListHttpRouterOperationsRequest = _reflection.GeneratedProtocolMessageType('ListHttpRouterOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTHTTPROUTEROPERATIONSREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.ListHttpRouterOperationsRequest)
  })
_sym_db.RegisterMessage(ListHttpRouterOperationsRequest)

ListHttpRouterOperationsResponse = _reflection.GeneratedProtocolMessageType('ListHttpRouterOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTHTTPROUTEROPERATIONSRESPONSE,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.http_router_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.ListHttpRouterOperationsResponse)
  })
_sym_db.RegisterMessage(ListHttpRouterOperationsResponse)

_HTTPROUTERSERVICE = DESCRIPTOR.services_by_name['HttpRouterService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancer'
  _GETHTTPROUTERREQUEST.fields_by_name['http_router_id']._options = None
  _GETHTTPROUTERREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _LISTHTTPROUTERSREQUEST.fields_by_name['folder_id']._options = None
  _LISTHTTPROUTERSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _LISTHTTPROUTERSREQUEST.fields_by_name['page_size']._options = None
  _LISTHTTPROUTERSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTHTTPROUTERSREQUEST.fields_by_name['page_token']._options = None
  _LISTHTTPROUTERSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTHTTPROUTERSREQUEST.fields_by_name['filter']._options = None
  _LISTHTTPROUTERSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _DELETEHTTPROUTERREQUEST.fields_by_name['http_router_id']._options = None
  _DELETEHTTPROUTERREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _UPDATEHTTPROUTERREQUEST_LABELSENTRY._options = None
  _UPDATEHTTPROUTERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATEHTTPROUTERREQUEST.fields_by_name['http_router_id']._options = None
  _UPDATEHTTPROUTERREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001'
  _UPDATEHTTPROUTERREQUEST.fields_by_name['name']._options = None
  _UPDATEHTTPROUTERREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?'
  _UPDATEHTTPROUTERREQUEST.fields_by_name['description']._options = None
  _UPDATEHTTPROUTERREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATEHTTPROUTERREQUEST.fields_by_name['labels']._options = None
  _UPDATEHTTPROUTERREQUEST.fields_by_name['labels']._serialized_options = b'\202\3101\004<=64\212\3101\004<=63\362\3071\017[-_./\\@0-9a-z]*\262\3101\006\032\0041-63\262\3101\026\022\024[a-z][-_./\\@0-9a-z]*'
  _CREATEHTTPROUTERREQUEST_LABELSENTRY._options = None
  _CREATEHTTPROUTERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATEHTTPROUTERREQUEST.fields_by_name['folder_id']._options = None
  _CREATEHTTPROUTERREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATEHTTPROUTERREQUEST.fields_by_name['name']._options = None
  _CREATEHTTPROUTERREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?'
  _CREATEHTTPROUTERREQUEST.fields_by_name['description']._options = None
  _CREATEHTTPROUTERREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATEHTTPROUTERREQUEST.fields_by_name['labels']._options = None
  _CREATEHTTPROUTERREQUEST.fields_by_name['labels']._serialized_options = b'\202\3101\004<=64\212\3101\004<=63\362\3071\017[-_./\\@0-9a-z]*\262\3101\006\032\0041-63\262\3101\026\022\024[a-z][-_./\\@0-9a-z]*'
  _LISTHTTPROUTEROPERATIONSREQUEST.fields_by_name['http_router_id']._options = None
  _LISTHTTPROUTEROPERATIONSREQUEST.fields_by_name['http_router_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTHTTPROUTEROPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTHTTPROUTEROPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTHTTPROUTEROPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTHTTPROUTEROPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _HTTPROUTERSERVICE.methods_by_name['Get']._options = None
  _HTTPROUTERSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\0022\0220/apploadbalancer/v1/httpRouters/{http_router_id}'
  _HTTPROUTERSERVICE.methods_by_name['List']._options = None
  _HTTPROUTERSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002!\022\037/apploadbalancer/v1/httpRouters'
  _HTTPROUTERSERVICE.methods_by_name['Create']._options = None
  _HTTPROUTERSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002$\"\037/apploadbalancer/v1/httpRouters:\001*\262\322*&\n\030CreateHttpRouterMetadata\022\nHttpRouter'
  _HTTPROUTERSERVICE.methods_by_name['Update']._options = None
  _HTTPROUTERSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002520/apploadbalancer/v1/httpRouters/{http_router_id}:\001*\262\322*&\n\030UpdateHttpRouterMetadata\022\nHttpRouter'
  _HTTPROUTERSERVICE.methods_by_name['Delete']._options = None
  _HTTPROUTERSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\0022*0/apploadbalancer/v1/httpRouters/{http_router_id}\262\322*1\n\030DeleteHttpRouterMetadata\022\025google.protobuf.Empty'
  _HTTPROUTERSERVICE.methods_by_name['ListOperations']._options = None
  _HTTPROUTERSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002=\022;/apploadbalancer/v1/httpRouters/{http_router_id}/operations'
  _GETHTTPROUTERREQUEST._serialized_start=366
  _GETHTTPROUTERREQUEST._serialized_end=418
  _LISTHTTPROUTERSREQUEST._serialized_start=421
  _LISTHTTPROUTERSREQUEST._serialized_end=560
  _LISTHTTPROUTERSRESPONSE._serialized_start=562
  _LISTHTTPROUTERSRESPONSE._serialized_end=679
  _DELETEHTTPROUTERREQUEST._serialized_start=681
  _DELETEHTTPROUTERREQUEST._serialized_end=736
  _DELETEHTTPROUTERMETADATA._serialized_start=738
  _DELETEHTTPROUTERMETADATA._serialized_end=788
  _UPDATEHTTPROUTERREQUEST._serialized_start=791
  _UPDATEHTTPROUTERREQUEST._serialized_end=1263
  _UPDATEHTTPROUTERREQUEST_LABELSENTRY._serialized_start=1212
  _UPDATEHTTPROUTERREQUEST_LABELSENTRY._serialized_end=1257
  _UPDATEHTTPROUTERMETADATA._serialized_start=1265
  _UPDATEHTTPROUTERMETADATA._serialized_end=1315
  _CREATEHTTPROUTERREQUEST._serialized_start=1318
  _CREATEHTTPROUTERREQUEST._serialized_end=1736
  _CREATEHTTPROUTERREQUEST_LABELSENTRY._serialized_start=1212
  _CREATEHTTPROUTERREQUEST_LABELSENTRY._serialized_end=1257
  _CREATEHTTPROUTERMETADATA._serialized_start=1738
  _CREATEHTTPROUTERMETADATA._serialized_end=1788
  _LISTHTTPROUTEROPERATIONSREQUEST._serialized_start=1791
  _LISTHTTPROUTEROPERATIONSREQUEST._serialized_end=1924
  _LISTHTTPROUTEROPERATIONSRESPONSE._serialized_start=1926
  _LISTHTTPROUTEROPERATIONSRESPONSE._serialized_end=2040
  _HTTPROUTERSERVICE._serialized_start=2043
  _HTTPROUTERSERVICE._serialized_end=3226
# @@protoc_insertion_point(module_scope)
