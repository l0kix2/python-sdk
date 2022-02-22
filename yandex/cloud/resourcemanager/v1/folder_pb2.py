# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/resourcemanager/v1/folder.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,yandex/cloud/resourcemanager/v1/folder.proto\x12\x1fyandex.cloud.resourcemanager.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xff\x02\n\x06\x46older\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x63loud_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x43\n\x06labels\x18\x06 \x03(\x0b\x32\x33.yandex.cloud.resourcemanager.v1.Folder.LabelsEntry\x12>\n\x06status\x18\x07 \x01(\x0e\x32..yandex.cloud.resourcemanager.v1.Folder.Status\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"P\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0c\n\x08\x44\x45LETING\x10\x02\x12\x14\n\x10PENDING_DELETION\x10\x03\x42z\n#yandex.cloud.api.resourcemanager.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/resourcemanager/v1;resourcemanagerb\x06proto3')



_FOLDER = DESCRIPTOR.message_types_by_name['Folder']
_FOLDER_LABELSENTRY = _FOLDER.nested_types_by_name['LabelsEntry']
_FOLDER_STATUS = _FOLDER.enum_types_by_name['Status']
Folder = _reflection.GeneratedProtocolMessageType('Folder', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FOLDER_LABELSENTRY,
    '__module__' : 'yandex.cloud.resourcemanager.v1.folder_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.resourcemanager.v1.Folder.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _FOLDER,
  '__module__' : 'yandex.cloud.resourcemanager.v1.folder_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.resourcemanager.v1.Folder)
  })
_sym_db.RegisterMessage(Folder)
_sym_db.RegisterMessage(Folder.LabelsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#yandex.cloud.api.resourcemanager.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/resourcemanager/v1;resourcemanager'
  _FOLDER_LABELSENTRY._options = None
  _FOLDER_LABELSENTRY._serialized_options = b'8\001'
  _FOLDER._serialized_start=115
  _FOLDER._serialized_end=498
  _FOLDER_LABELSENTRY._serialized_start=371
  _FOLDER_LABELSENTRY._serialized_end=416
  _FOLDER_STATUS._serialized_start=418
  _FOLDER_STATUS._serialized_end=498
# @@protoc_insertion_point(module_scope)
