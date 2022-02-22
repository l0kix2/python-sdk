# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/containerregistry/v1/lifecycle_policy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8yandex/cloud/containerregistry/v1/lifecycle_policy.proto\x12!yandex.cloud.containerregistry.v1\x1a\x1dyandex/cloud/validation.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcf\x02\n\x0fLifecyclePolicy\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rrepository_id\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12I\n\x06status\x18\x05 \x01(\x0e\x32\x39.yandex.cloud.containerregistry.v1.LifecyclePolicy.Status\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12?\n\x05rules\x18\x07 \x03(\x0b\x32\x30.yandex.cloud.containerregistry.v1.LifecycleRule\":\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"\xbc\x01\n\rLifecycleRule\x12\x1e\n\x0b\x64\x65scription\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12;\n\rexpire_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05>=24h\x12\x1d\n\ntag_regexp\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x10\n\x08untagged\x18\x04 \x01(\x08\x12\x1d\n\x0cretained_top\x18\x05 \x01(\x03\x42\x07\xfa\xc7\x31\x03>=0B\x80\x01\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistryb\x06proto3')



_LIFECYCLEPOLICY = DESCRIPTOR.message_types_by_name['LifecyclePolicy']
_LIFECYCLERULE = DESCRIPTOR.message_types_by_name['LifecycleRule']
_LIFECYCLEPOLICY_STATUS = _LIFECYCLEPOLICY.enum_types_by_name['Status']
LifecyclePolicy = _reflection.GeneratedProtocolMessageType('LifecyclePolicy', (_message.Message,), {
  'DESCRIPTOR' : _LIFECYCLEPOLICY,
  '__module__' : 'yandex.cloud.containerregistry.v1.lifecycle_policy_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.LifecyclePolicy)
  })
_sym_db.RegisterMessage(LifecyclePolicy)

LifecycleRule = _reflection.GeneratedProtocolMessageType('LifecycleRule', (_message.Message,), {
  'DESCRIPTOR' : _LIFECYCLERULE,
  '__module__' : 'yandex.cloud.containerregistry.v1.lifecycle_policy_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.LifecycleRule)
  })
_sym_db.RegisterMessage(LifecycleRule)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistry'
  _LIFECYCLERULE.fields_by_name['description']._options = None
  _LIFECYCLERULE.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _LIFECYCLERULE.fields_by_name['expire_period']._options = None
  _LIFECYCLERULE.fields_by_name['expire_period']._serialized_options = b'\372\3071\005>=24h'
  _LIFECYCLERULE.fields_by_name['tag_regexp']._options = None
  _LIFECYCLERULE.fields_by_name['tag_regexp']._serialized_options = b'\212\3101\005<=256'
  _LIFECYCLERULE.fields_by_name['retained_top']._options = None
  _LIFECYCLERULE.fields_by_name['retained_top']._serialized_options = b'\372\3071\003>=0'
  _LIFECYCLEPOLICY._serialized_start=192
  _LIFECYCLEPOLICY._serialized_end=527
  _LIFECYCLEPOLICY_STATUS._serialized_start=469
  _LIFECYCLEPOLICY_STATUS._serialized_end=527
  _LIFECYCLERULE._serialized_start=530
  _LIFECYCLERULE._serialized_end=718
# @@protoc_insertion_point(module_scope)
