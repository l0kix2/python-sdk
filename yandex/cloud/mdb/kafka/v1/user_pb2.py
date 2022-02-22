# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/kafka/v1/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$yandex/cloud/mdb/kafka/v1/user.proto\x12\x19yandex.cloud.mdb.kafka.v1\x1a\x1dyandex/cloud/validation.proto\"d\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12:\n\x0bpermissions\x18\x03 \x03(\x0b\x32%.yandex.cloud.mdb.kafka.v1.Permission\"\x95\x01\n\x08UserSpec\x12,\n\x04name\x18\x01 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x31-256\xf2\xc7\x31\r[a-zA-Z0-9_]*\x12\x1f\n\x08password\x18\x02 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x38-128\x12:\n\x0bpermissions\x18\x03 \x03(\x0b\x32%.yandex.cloud.mdb.kafka.v1.Permission\"\xd6\x01\n\nPermission\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12>\n\x04role\x18\x02 \x01(\x0e\x32\x30.yandex.cloud.mdb.kafka.v1.Permission.AccessRole\"t\n\nAccessRole\x12\x1b\n\x17\x41\x43\x43\x45SS_ROLE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x41\x43\x43\x45SS_ROLE_PRODUCER\x10\x01\x12\x18\n\x14\x41\x43\x43\x45SS_ROLE_CONSUMER\x10\x02\x12\x15\n\x11\x41\x43\x43\x45SS_ROLE_ADMIN\x10\x03\x42\x64\n\x1dyandex.cloud.api.mdb.kafka.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/kafka/v1;kafkab\x06proto3')



_USER = DESCRIPTOR.message_types_by_name['User']
_USERSPEC = DESCRIPTOR.message_types_by_name['UserSpec']
_PERMISSION = DESCRIPTOR.message_types_by_name['Permission']
_PERMISSION_ACCESSROLE = _PERMISSION.enum_types_by_name['AccessRole']
User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'yandex.cloud.mdb.kafka.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.kafka.v1.User)
  })
_sym_db.RegisterMessage(User)

UserSpec = _reflection.GeneratedProtocolMessageType('UserSpec', (_message.Message,), {
  'DESCRIPTOR' : _USERSPEC,
  '__module__' : 'yandex.cloud.mdb.kafka.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.kafka.v1.UserSpec)
  })
_sym_db.RegisterMessage(UserSpec)

Permission = _reflection.GeneratedProtocolMessageType('Permission', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSION,
  '__module__' : 'yandex.cloud.mdb.kafka.v1.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.kafka.v1.Permission)
  })
_sym_db.RegisterMessage(Permission)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035yandex.cloud.api.mdb.kafka.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/kafka/v1;kafka'
  _USERSPEC.fields_by_name['name']._options = None
  _USERSPEC.fields_by_name['name']._serialized_options = b'\350\3071\001\212\3101\0051-256\362\3071\r[a-zA-Z0-9_]*'
  _USERSPEC.fields_by_name['password']._options = None
  _USERSPEC.fields_by_name['password']._serialized_options = b'\350\3071\001\212\3101\0058-128'
  _USER._serialized_start=98
  _USER._serialized_end=198
  _USERSPEC._serialized_start=201
  _USERSPEC._serialized_end=350
  _PERMISSION._serialized_start=353
  _PERMISSION._serialized_end=567
  _PERMISSION_ACCESSROLE._serialized_start=451
  _PERMISSION_ACCESSROLE._serialized_end=567
# @@protoc_insertion_point(module_scope)
