# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/apploadbalancer/v1/target_group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2yandex/cloud/apploadbalancer/v1/target_group.proto\x12\x1fyandex.cloud.apploadbalancer.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xb2\x02\n\x0bTargetGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tfolder_id\x18\x04 \x01(\t\x12H\n\x06labels\x18\x05 \x03(\x0b\x32\x38.yandex.cloud.apploadbalancer.v1.TargetGroup.LabelsEntry\x12\x38\n\x07targets\x18\x06 \x03(\x0b\x32\'.yandex.cloud.apploadbalancer.v1.Target\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"e\n\x06Target\x12\x14\n\nip_address\x18\x01 \x01(\tH\x00\x12\x11\n\tsubnet_id\x18\x03 \x01(\t\x12\x1c\n\x14private_ipv4_address\x18\x04 \x01(\x08\x42\x14\n\x0c\x61\x64\x64ress_type\x12\x04\xc0\xc1\x31\x01\x42z\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancerb\x06proto3')



_TARGETGROUP = DESCRIPTOR.message_types_by_name['TargetGroup']
_TARGETGROUP_LABELSENTRY = _TARGETGROUP.nested_types_by_name['LabelsEntry']
_TARGET = DESCRIPTOR.message_types_by_name['Target']
TargetGroup = _reflection.GeneratedProtocolMessageType('TargetGroup', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TARGETGROUP_LABELSENTRY,
    '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.TargetGroup.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _TARGETGROUP,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.TargetGroup)
  })
_sym_db.RegisterMessage(TargetGroup)
_sym_db.RegisterMessage(TargetGroup.LabelsEntry)

Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {
  'DESCRIPTOR' : _TARGET,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.Target)
  })
_sym_db.RegisterMessage(Target)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancer'
  _TARGETGROUP_LABELSENTRY._options = None
  _TARGETGROUP_LABELSENTRY._serialized_options = b'8\001'
  _TARGET.oneofs_by_name['address_type']._options = None
  _TARGET.oneofs_by_name['address_type']._serialized_options = b'\300\3011\001'
  _TARGETGROUP._serialized_start=152
  _TARGETGROUP._serialized_end=458
  _TARGETGROUP_LABELSENTRY._serialized_start=413
  _TARGETGROUP_LABELSENTRY._serialized_end=458
  _TARGET._serialized_start=460
  _TARGET._serialized_end=561
# @@protoc_insertion_point(module_scope)
