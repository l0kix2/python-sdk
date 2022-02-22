# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mysql/v1alpha/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/mdb/mysql/v1alpha/user.proto\x12\x1eyandex.cloud.mdb.mysql.v1alpha\x1a\x1dyandex/cloud/validation.proto\"i\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12?\n\x0bpermissions\x18\x03 \x03(\x0b\x32*.yandex.cloud.mdb.mysql.v1alpha.Permission\"\xa4\x03\n\nPermission\x12\x15\n\rdatabase_name\x18\x01 \x01(\t\x12L\n\x05roles\x18\x02 \x03(\x0e\x32\x34.yandex.cloud.mdb.mysql.v1alpha.Permission.PrivilegeB\x07\x82\xc8\x31\x03>=1\"\xb0\x02\n\tPrivilege\x12\x19\n\x15PRIVILEGE_UNSPECIFIED\x10\x00\x12\x12\n\x0e\x41LL_PRIVILEGES\x10\x01\x12\t\n\x05\x41LTER\x10\x02\x12\x11\n\rALTER_ROUTINE\x10\x03\x12\n\n\x06\x43REATE\x10\x04\x12\x12\n\x0e\x43REATE_ROUTINE\x10\x05\x12\x1b\n\x17\x43REATE_TEMPORARY_TABLES\x10\x06\x12\x0f\n\x0b\x43REATE_VIEW\x10\x07\x12\n\n\x06\x44\x45LETE\x10\x08\x12\x08\n\x04\x44ROP\x10\t\x12\t\n\x05\x45VENT\x10\n\x12\x0b\n\x07\x45XECUTE\x10\x0b\x12\t\n\x05INDEX\x10\x0c\x12\n\n\x06INSERT\x10\r\x12\x0f\n\x0bLOCK_TABLES\x10\x0e\x12\n\n\x06SELECT\x10\x0f\x12\r\n\tSHOW_VIEW\x10\x10\x12\x0b\n\x07TRIGGER\x10\x11\x12\n\n\x06UPDATE\x10\x12\"\x99\x01\n\x08UserSpec\x12+\n\x04name\x18\x01 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=32\xf2\xc7\x31\r[a-zA-Z0-9_]*\x12\x1f\n\x08password\x18\x02 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x38-128\x12?\n\x0bpermissions\x18\x03 \x03(\x0b\x32*.yandex.cloud.mdb.mysql.v1alpha.PermissionBn\n\"yandex.cloud.api.mdb.mysql.v1alphaZHgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1alpha;mysqlb\x06proto3')



_USER = DESCRIPTOR.message_types_by_name['User']
_PERMISSION = DESCRIPTOR.message_types_by_name['Permission']
_USERSPEC = DESCRIPTOR.message_types_by_name['UserSpec']
_PERMISSION_PRIVILEGE = _PERMISSION.enum_types_by_name['Privilege']
User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'yandex.cloud.mdb.mysql.v1alpha.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1alpha.User)
  })
_sym_db.RegisterMessage(User)

Permission = _reflection.GeneratedProtocolMessageType('Permission', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSION,
  '__module__' : 'yandex.cloud.mdb.mysql.v1alpha.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1alpha.Permission)
  })
_sym_db.RegisterMessage(Permission)

UserSpec = _reflection.GeneratedProtocolMessageType('UserSpec', (_message.Message,), {
  'DESCRIPTOR' : _USERSPEC,
  '__module__' : 'yandex.cloud.mdb.mysql.v1alpha.user_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1alpha.UserSpec)
  })
_sym_db.RegisterMessage(UserSpec)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"yandex.cloud.api.mdb.mysql.v1alphaZHgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1alpha;mysql'
  _PERMISSION.fields_by_name['roles']._options = None
  _PERMISSION.fields_by_name['roles']._serialized_options = b'\202\3101\003>=1'
  _USERSPEC.fields_by_name['name']._options = None
  _USERSPEC.fields_by_name['name']._serialized_options = b'\350\3071\001\212\3101\004<=32\362\3071\r[a-zA-Z0-9_]*'
  _USERSPEC.fields_by_name['password']._options = None
  _USERSPEC.fields_by_name['password']._serialized_options = b'\350\3071\001\212\3101\0058-128'
  _USER._serialized_start=108
  _USER._serialized_end=213
  _PERMISSION._serialized_start=216
  _PERMISSION._serialized_end=636
  _PERMISSION_PRIVILEGE._serialized_start=332
  _PERMISSION_PRIVILEGE._serialized_end=636
  _USERSPEC._serialized_start=639
  _USERSPEC._serialized_end=792
# @@protoc_insertion_point(module_scope)
