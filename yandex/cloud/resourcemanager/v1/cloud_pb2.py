# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/resourcemanager/v1/cloud.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+yandex/cloud/resourcemanager/v1/cloud.proto\x12\x1fyandex.cloud.resourcemanager.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf2\x01\n\x05\x43loud\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x17\n\x0forganization_id\x18\x06 \x01(\t\x12\x42\n\x06labels\x18\x07 \x03(\x0b\x32\x32.yandex.cloud.resourcemanager.v1.Cloud.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42z\n#yandex.cloud.api.resourcemanager.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/resourcemanager/v1;resourcemanagerb\x06proto3')



_CLOUD = DESCRIPTOR.message_types_by_name['Cloud']
_CLOUD_LABELSENTRY = _CLOUD.nested_types_by_name['LabelsEntry']
Cloud = _reflection.GeneratedProtocolMessageType('Cloud', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLOUD_LABELSENTRY,
    '__module__' : 'yandex.cloud.resourcemanager.v1.cloud_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.resourcemanager.v1.Cloud.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CLOUD,
  '__module__' : 'yandex.cloud.resourcemanager.v1.cloud_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.resourcemanager.v1.Cloud)
  })
_sym_db.RegisterMessage(Cloud)
_sym_db.RegisterMessage(Cloud.LabelsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#yandex.cloud.api.resourcemanager.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/resourcemanager/v1;resourcemanager'
  _CLOUD_LABELSENTRY._options = None
  _CLOUD_LABELSENTRY._serialized_options = b'8\001'
  _CLOUD._serialized_start=114
  _CLOUD._serialized_end=356
  _CLOUD_LABELSENTRY._serialized_start=311
  _CLOUD_LABELSENTRY._serialized_end=356
# @@protoc_insertion_point(module_scope)
