# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/cdn/v1/origin_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.cdn.v1 import origin_pb2 as yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/cdn/v1/origin_service.proto',
  package='yandex.cloud.cdn.v1',
  syntax='proto3',
  serialized_options=b'\n\027yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdn',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(yandex/cloud/cdn/v1/origin_service.proto\x12\x13yandex.cloud.cdn.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a yandex/cloud/api/operation.proto\x1a yandex/cloud/cdn/v1/origin.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"N\n\x10GetOriginRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x19\n\torigin_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\"V\n\x12ListOriginsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1f\n\x0forigin_group_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\"C\n\x13ListOriginsResponse\x12,\n\x07origins\x18\x01 \x03(\x0b\x32\x1b.yandex.cloud.cdn.v1.Origin\"\xfd\x01\n\x13\x43reateOriginRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1f\n\x0forigin_group_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x12\x1c\n\x06source\x18\x03 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12+\n\x07\x65nabled\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06\x62\x61\x63kup\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12-\n\x04meta\x18\x06 \x01(\x0b\x32\x1f.yandex.cloud.cdn.v1.OriginMeta\"R\n\x14\x43reateOriginMetadata\x12\x19\n\torigin_id\x18\x01 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x12\x1f\n\x0forigin_group_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\"\xb1\x01\n\x13UpdateOriginRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x19\n\torigin_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12\x0e\n\x06\x62\x61\x63kup\x18\x05 \x01(\x08\x12-\n\x04meta\x18\x06 \x01(\x0b\x32\x1f.yandex.cloud.cdn.v1.OriginMeta\"R\n\x14UpdateOriginMetadata\x12\x19\n\torigin_id\x18\x01 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\x12\x1f\n\x0forigin_group_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\"Q\n\x13\x44\x65leteOriginRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x19\n\torigin_id\x18\x02 \x01(\x03\x42\x06\xfa\xc7\x31\x02>0\"1\n\x14\x44\x65leteOriginMetadata\x12\x19\n\torigin_id\x18\x01 \x01(\x03\x42\x06\xfa\xc7\x31\x02>02\xd9\x05\n\rOriginService\x12n\n\x03Get\x12%.yandex.cloud.cdn.v1.GetOriginRequest\x1a\x1b.yandex.cloud.cdn.v1.Origin\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cdn/v1/origins/{origin_id}\x12r\n\x04List\x12\'.yandex.cloud.cdn.v1.ListOriginsRequest\x1a(.yandex.cloud.cdn.v1.ListOriginsResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/cdn/v1/origins\x12\x93\x01\n\x06\x43reate\x12(.yandex.cloud.cdn.v1.CreateOriginRequest\x1a!.yandex.cloud.operation.Operation\"<\x82\xd3\xe4\x93\x02\x14\"\x0f/cdn/v1/origins:\x01*\xb2\xd2*\x1e\n\x14\x43reateOriginMetadata\x12\x06Origin\x12\x9f\x01\n\x06Update\x12(.yandex.cloud.cdn.v1.UpdateOriginRequest\x1a!.yandex.cloud.operation.Operation\"H\x82\xd3\xe4\x93\x02 2\x1b/cdn/v1/origins/{origin_id}:\x01*\xb2\xd2*\x1e\n\x14UpdateOriginMetadata\x12\x06Origin\x12\xab\x01\n\x06\x44\x65lete\x12(.yandex.cloud.cdn.v1.DeleteOriginRequest\x1a!.yandex.cloud.operation.Operation\"T\x82\xd3\xe4\x93\x02\x1d*\x1b/cdn/v1/origins/{origin_id}\xb2\xd2*-\n\x14\x44\x65leteOriginMetadata\x12\x15google.protobuf.EmptyBV\n\x17yandex.cloud.api.cdn.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/cdn/v1;cdnb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,yandex_dot_cloud_dot_api_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__pb2.DESCRIPTOR,yandex_dot_cloud_dot_operation_dot_operation__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])




_GETORIGINREQUEST = _descriptor.Descriptor(
  name='GetOriginRequest',
  full_name='yandex.cloud.cdn.v1.GetOriginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.cdn.v1.GetOriginRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin_id', full_name='yandex.cloud.cdn.v1.GetOriginRequest.origin_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\002>0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=266,
  serialized_end=344,
)


_LISTORIGINSREQUEST = _descriptor.Descriptor(
  name='ListOriginsRequest',
  full_name='yandex.cloud.cdn.v1.ListOriginsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.cdn.v1.ListOriginsRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin_group_id', full_name='yandex.cloud.cdn.v1.ListOriginsRequest.origin_group_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\002>0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=346,
  serialized_end=432,
)


_LISTORIGINSRESPONSE = _descriptor.Descriptor(
  name='ListOriginsResponse',
  full_name='yandex.cloud.cdn.v1.ListOriginsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='origins', full_name='yandex.cloud.cdn.v1.ListOriginsResponse.origins', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=434,
  serialized_end=501,
)


_CREATEORIGINREQUEST = _descriptor.Descriptor(
  name='CreateOriginRequest',
  full_name='yandex.cloud.cdn.v1.CreateOriginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.cdn.v1.CreateOriginRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin_group_id', full_name='yandex.cloud.cdn.v1.CreateOriginRequest.origin_group_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\002>0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='yandex.cloud.cdn.v1.CreateOriginRequest.source', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='yandex.cloud.cdn.v1.CreateOriginRequest.enabled', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backup', full_name='yandex.cloud.cdn.v1.CreateOriginRequest.backup', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='yandex.cloud.cdn.v1.CreateOriginRequest.meta', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=504,
  serialized_end=757,
)


_CREATEORIGINMETADATA = _descriptor.Descriptor(
  name='CreateOriginMetadata',
  full_name='yandex.cloud.cdn.v1.CreateOriginMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin_id', full_name='yandex.cloud.cdn.v1.CreateOriginMetadata.origin_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\002>0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin_group_id', full_name='yandex.cloud.cdn.v1.CreateOriginMetadata.origin_group_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\002>0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=759,
  serialized_end=841,
)


_UPDATEORIGINREQUEST = _descriptor.Descriptor(
  name='UpdateOriginRequest',
  full_name='yandex.cloud.cdn.v1.UpdateOriginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.cdn.v1.UpdateOriginRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin_id', full_name='yandex.cloud.cdn.v1.UpdateOriginRequest.origin_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\002>0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='yandex.cloud.cdn.v1.UpdateOriginRequest.source', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='yandex.cloud.cdn.v1.UpdateOriginRequest.enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backup', full_name='yandex.cloud.cdn.v1.UpdateOriginRequest.backup', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='yandex.cloud.cdn.v1.UpdateOriginRequest.meta', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=844,
  serialized_end=1021,
)


_UPDATEORIGINMETADATA = _descriptor.Descriptor(
  name='UpdateOriginMetadata',
  full_name='yandex.cloud.cdn.v1.UpdateOriginMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin_id', full_name='yandex.cloud.cdn.v1.UpdateOriginMetadata.origin_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\002>0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin_group_id', full_name='yandex.cloud.cdn.v1.UpdateOriginMetadata.origin_group_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\002>0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1023,
  serialized_end=1105,
)


_DELETEORIGINREQUEST = _descriptor.Descriptor(
  name='DeleteOriginRequest',
  full_name='yandex.cloud.cdn.v1.DeleteOriginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.cdn.v1.DeleteOriginRequest.folder_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\350\3071\001\212\3101\004<=50', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='origin_id', full_name='yandex.cloud.cdn.v1.DeleteOriginRequest.origin_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\002>0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1107,
  serialized_end=1188,
)


_DELETEORIGINMETADATA = _descriptor.Descriptor(
  name='DeleteOriginMetadata',
  full_name='yandex.cloud.cdn.v1.DeleteOriginMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin_id', full_name='yandex.cloud.cdn.v1.DeleteOriginMetadata.origin_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372\3071\002>0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1190,
  serialized_end=1239,
)

_LISTORIGINSRESPONSE.fields_by_name['origins'].message_type = yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__pb2._ORIGIN
_CREATEORIGINREQUEST.fields_by_name['enabled'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CREATEORIGINREQUEST.fields_by_name['backup'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CREATEORIGINREQUEST.fields_by_name['meta'].message_type = yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__pb2._ORIGINMETA
_UPDATEORIGINREQUEST.fields_by_name['meta'].message_type = yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__pb2._ORIGINMETA
DESCRIPTOR.message_types_by_name['GetOriginRequest'] = _GETORIGINREQUEST
DESCRIPTOR.message_types_by_name['ListOriginsRequest'] = _LISTORIGINSREQUEST
DESCRIPTOR.message_types_by_name['ListOriginsResponse'] = _LISTORIGINSRESPONSE
DESCRIPTOR.message_types_by_name['CreateOriginRequest'] = _CREATEORIGINREQUEST
DESCRIPTOR.message_types_by_name['CreateOriginMetadata'] = _CREATEORIGINMETADATA
DESCRIPTOR.message_types_by_name['UpdateOriginRequest'] = _UPDATEORIGINREQUEST
DESCRIPTOR.message_types_by_name['UpdateOriginMetadata'] = _UPDATEORIGINMETADATA
DESCRIPTOR.message_types_by_name['DeleteOriginRequest'] = _DELETEORIGINREQUEST
DESCRIPTOR.message_types_by_name['DeleteOriginMetadata'] = _DELETEORIGINMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetOriginRequest = _reflection.GeneratedProtocolMessageType('GetOriginRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORIGINREQUEST,
  '__module__' : 'yandex.cloud.cdn.v1.origin_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.GetOriginRequest)
  })
_sym_db.RegisterMessage(GetOriginRequest)

ListOriginsRequest = _reflection.GeneratedProtocolMessageType('ListOriginsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTORIGINSREQUEST,
  '__module__' : 'yandex.cloud.cdn.v1.origin_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.ListOriginsRequest)
  })
_sym_db.RegisterMessage(ListOriginsRequest)

ListOriginsResponse = _reflection.GeneratedProtocolMessageType('ListOriginsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTORIGINSRESPONSE,
  '__module__' : 'yandex.cloud.cdn.v1.origin_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.ListOriginsResponse)
  })
_sym_db.RegisterMessage(ListOriginsResponse)

CreateOriginRequest = _reflection.GeneratedProtocolMessageType('CreateOriginRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORIGINREQUEST,
  '__module__' : 'yandex.cloud.cdn.v1.origin_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.CreateOriginRequest)
  })
_sym_db.RegisterMessage(CreateOriginRequest)

CreateOriginMetadata = _reflection.GeneratedProtocolMessageType('CreateOriginMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORIGINMETADATA,
  '__module__' : 'yandex.cloud.cdn.v1.origin_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.CreateOriginMetadata)
  })
_sym_db.RegisterMessage(CreateOriginMetadata)

UpdateOriginRequest = _reflection.GeneratedProtocolMessageType('UpdateOriginRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEORIGINREQUEST,
  '__module__' : 'yandex.cloud.cdn.v1.origin_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.UpdateOriginRequest)
  })
_sym_db.RegisterMessage(UpdateOriginRequest)

UpdateOriginMetadata = _reflection.GeneratedProtocolMessageType('UpdateOriginMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEORIGINMETADATA,
  '__module__' : 'yandex.cloud.cdn.v1.origin_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.UpdateOriginMetadata)
  })
_sym_db.RegisterMessage(UpdateOriginMetadata)

DeleteOriginRequest = _reflection.GeneratedProtocolMessageType('DeleteOriginRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEORIGINREQUEST,
  '__module__' : 'yandex.cloud.cdn.v1.origin_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.DeleteOriginRequest)
  })
_sym_db.RegisterMessage(DeleteOriginRequest)

DeleteOriginMetadata = _reflection.GeneratedProtocolMessageType('DeleteOriginMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEORIGINMETADATA,
  '__module__' : 'yandex.cloud.cdn.v1.origin_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.cdn.v1.DeleteOriginMetadata)
  })
_sym_db.RegisterMessage(DeleteOriginMetadata)


DESCRIPTOR._options = None
_GETORIGINREQUEST.fields_by_name['folder_id']._options = None
_GETORIGINREQUEST.fields_by_name['origin_id']._options = None
_LISTORIGINSREQUEST.fields_by_name['folder_id']._options = None
_LISTORIGINSREQUEST.fields_by_name['origin_group_id']._options = None
_CREATEORIGINREQUEST.fields_by_name['folder_id']._options = None
_CREATEORIGINREQUEST.fields_by_name['origin_group_id']._options = None
_CREATEORIGINREQUEST.fields_by_name['source']._options = None
_CREATEORIGINMETADATA.fields_by_name['origin_id']._options = None
_CREATEORIGINMETADATA.fields_by_name['origin_group_id']._options = None
_UPDATEORIGINREQUEST.fields_by_name['folder_id']._options = None
_UPDATEORIGINREQUEST.fields_by_name['origin_id']._options = None
_UPDATEORIGINMETADATA.fields_by_name['origin_id']._options = None
_UPDATEORIGINMETADATA.fields_by_name['origin_group_id']._options = None
_DELETEORIGINREQUEST.fields_by_name['folder_id']._options = None
_DELETEORIGINREQUEST.fields_by_name['origin_id']._options = None
_DELETEORIGINMETADATA.fields_by_name['origin_id']._options = None

_ORIGINSERVICE = _descriptor.ServiceDescriptor(
  name='OriginService',
  full_name='yandex.cloud.cdn.v1.OriginService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1242,
  serialized_end=1971,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='yandex.cloud.cdn.v1.OriginService.Get',
    index=0,
    containing_service=None,
    input_type=_GETORIGINREQUEST,
    output_type=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__pb2._ORIGIN,
    serialized_options=b'\202\323\344\223\002\035\022\033/cdn/v1/origins/{origin_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='yandex.cloud.cdn.v1.OriginService.List',
    index=1,
    containing_service=None,
    input_type=_LISTORIGINSREQUEST,
    output_type=_LISTORIGINSRESPONSE,
    serialized_options=b'\202\323\344\223\002\021\022\017/cdn/v1/origins',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='yandex.cloud.cdn.v1.OriginService.Create',
    index=2,
    containing_service=None,
    input_type=_CREATEORIGINREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\024\"\017/cdn/v1/origins:\001*\262\322*\036\n\024CreateOriginMetadata\022\006Origin',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='yandex.cloud.cdn.v1.OriginService.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATEORIGINREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002 2\033/cdn/v1/origins/{origin_id}:\001*\262\322*\036\n\024UpdateOriginMetadata\022\006Origin',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='yandex.cloud.cdn.v1.OriginService.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETEORIGINREQUEST,
    output_type=yandex_dot_cloud_dot_operation_dot_operation__pb2._OPERATION,
    serialized_options=b'\202\323\344\223\002\035*\033/cdn/v1/origins/{origin_id}\262\322*-\n\024DeleteOriginMetadata\022\025google.protobuf.Empty',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORIGINSERVICE)

DESCRIPTOR.services_by_name['OriginService'] = _ORIGINSERVICE

# @@protoc_insertion_point(module_scope)
