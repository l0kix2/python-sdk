# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mongodb/v1/user_service.proto
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
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.mdb.mongodb.v1 import user_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.yandex/cloud/mdb/mongodb/v1/user_service.proto\x12\x1byandex.cloud.mdb.mongodb.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1dyandex/cloud/validation.proto\x1a&yandex/cloud/operation/operation.proto\x1a&yandex/cloud/mdb/mongodb/v1/user.proto\x1a yandex/cloud/api/operation.proto\"d\n\x0eGetUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\r[a-zA-Z0-9_]*\"r\n\x10ListUsersRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"^\n\x11ListUsersResponse\x12\x30\n\x05users\x18\x01 \x03(\x0b\x32!.yandex.cloud.mdb.mongodb.v1.User\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"o\n\x11\x43reateUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x38\n\tuser_spec\x18\x02 \x01(\x0b\x32%.yandex.cloud.mdb.mongodb.v1.UserSpec\";\n\x12\x43reateUserMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xf3\x01\n\x11UpdateUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\r[a-zA-Z0-9_]*\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1b\n\x08password\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05\x38-128\x12<\n\x0bpermissions\x18\x05 \x03(\x0b\x32\'.yandex.cloud.mdb.mongodb.v1.Permission\";\n\x12UpdateUserMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"g\n\x11\x44\x65leteUserRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\r[a-zA-Z0-9_]*\";\n\x12\x44\x65leteUserMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xb3\x01\n\x1aGrantUserPermissionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\r[a-zA-Z0-9_]*\x12\x41\n\npermission\x18\x03 \x01(\x0b\x32\'.yandex.cloud.mdb.mongodb.v1.PermissionB\x04\xe8\xc7\x31\x01\"D\n\x1bGrantUserPermissionMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xa8\x01\n\x1bRevokeUserPermissionRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x30\n\tuser_name\x18\x02 \x01(\tB\x1d\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\r[a-zA-Z0-9_]*\x12\x35\n\rdatabase_name\x18\x03 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\"E\n\x1cRevokeUserPermissionMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t2\xfb\n\n\x0bUserService\x12\x9a\x01\n\x03Get\x12+.yandex.cloud.mdb.mongodb.v1.GetUserRequest\x1a!.yandex.cloud.mdb.mongodb.v1.User\"C\x82\xd3\xe4\x93\x02=\x12;/managed-mongodb/v1/clusters/{cluster_id}/users/{user_name}\x12\x9e\x01\n\x04List\x12-.yandex.cloud.mdb.mongodb.v1.ListUsersRequest\x1a..yandex.cloud.mdb.mongodb.v1.ListUsersResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//managed-mongodb/v1/clusters/{cluster_id}/users\x12\xb5\x01\n\x06\x43reate\x12..yandex.cloud.mdb.mongodb.v1.CreateUserRequest\x1a!.yandex.cloud.operation.Operation\"X\x82\xd3\xe4\x93\x02\x34\"//managed-mongodb/v1/clusters/{cluster_id}/users:\x01*\xb2\xd2*\x1a\n\x12\x43reateUserMetadata\x12\x04User\x12\xc1\x01\n\x06Update\x12..yandex.cloud.mdb.mongodb.v1.UpdateUserRequest\x1a!.yandex.cloud.operation.Operation\"d\x82\xd3\xe4\x93\x02@2;/managed-mongodb/v1/clusters/{cluster_id}/users/{user_name}:\x01*\xb2\xd2*\x1a\n\x12UpdateUserMetadata\x12\x04User\x12\xcf\x01\n\x06\x44\x65lete\x12..yandex.cloud.mdb.mongodb.v1.DeleteUserRequest\x1a!.yandex.cloud.operation.Operation\"r\x82\xd3\xe4\x93\x02=*;/managed-mongodb/v1/clusters/{cluster_id}/users/{user_name}\xb2\xd2*+\n\x12\x44\x65leteUserMetadata\x12\x15google.protobuf.Empty\x12\xec\x01\n\x0fGrantPermission\x12\x37.yandex.cloud.mdb.mongodb.v1.GrantUserPermissionRequest\x1a!.yandex.cloud.operation.Operation\"}\x82\xd3\xe4\x93\x02P\"K/managed-mongodb/v1/clusters/{cluster_id}/users/{user_name}:grantPermission:\x01*\xb2\xd2*#\n\x1bGrantUserPermissionMetadata\x12\x04User\x12\xf0\x01\n\x10RevokePermission\x12\x38.yandex.cloud.mdb.mongodb.v1.RevokeUserPermissionRequest\x1a!.yandex.cloud.operation.Operation\"\x7f\x82\xd3\xe4\x93\x02Q\"L/managed-mongodb/v1/clusters/{cluster_id}/users/{user_name}:revokePermission:\x01*\xb2\xd2*$\n\x1cRevokeUserPermissionMetadata\x12\x04UserBj\n\x1fyandex.cloud.api.mdb.mongodb.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1;mongodbb\x06proto3')



_GETUSERREQUEST = DESCRIPTOR.message_types_by_name['GetUserRequest']
_LISTUSERSREQUEST = DESCRIPTOR.message_types_by_name['ListUsersRequest']
_LISTUSERSRESPONSE = DESCRIPTOR.message_types_by_name['ListUsersResponse']
_CREATEUSERREQUEST = DESCRIPTOR.message_types_by_name['CreateUserRequest']
_CREATEUSERMETADATA = DESCRIPTOR.message_types_by_name['CreateUserMetadata']
_UPDATEUSERREQUEST = DESCRIPTOR.message_types_by_name['UpdateUserRequest']
_UPDATEUSERMETADATA = DESCRIPTOR.message_types_by_name['UpdateUserMetadata']
_DELETEUSERREQUEST = DESCRIPTOR.message_types_by_name['DeleteUserRequest']
_DELETEUSERMETADATA = DESCRIPTOR.message_types_by_name['DeleteUserMetadata']
_GRANTUSERPERMISSIONREQUEST = DESCRIPTOR.message_types_by_name['GrantUserPermissionRequest']
_GRANTUSERPERMISSIONMETADATA = DESCRIPTOR.message_types_by_name['GrantUserPermissionMetadata']
_REVOKEUSERPERMISSIONREQUEST = DESCRIPTOR.message_types_by_name['RevokeUserPermissionRequest']
_REVOKEUSERPERMISSIONMETADATA = DESCRIPTOR.message_types_by_name['RevokeUserPermissionMetadata']
GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

ListUsersRequest = _reflection.GeneratedProtocolMessageType('ListUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERSREQUEST,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.ListUsersRequest)
  })
_sym_db.RegisterMessage(ListUsersRequest)

ListUsersResponse = _reflection.GeneratedProtocolMessageType('ListUsersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSERSRESPONSE,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.ListUsersResponse)
  })
_sym_db.RegisterMessage(ListUsersResponse)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

CreateUserMetadata = _reflection.GeneratedProtocolMessageType('CreateUserMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERMETADATA,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.CreateUserMetadata)
  })
_sym_db.RegisterMessage(CreateUserMetadata)

UpdateUserRequest = _reflection.GeneratedProtocolMessageType('UpdateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERREQUEST,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.UpdateUserRequest)
  })
_sym_db.RegisterMessage(UpdateUserRequest)

UpdateUserMetadata = _reflection.GeneratedProtocolMessageType('UpdateUserMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERMETADATA,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.UpdateUserMetadata)
  })
_sym_db.RegisterMessage(UpdateUserMetadata)

DeleteUserRequest = _reflection.GeneratedProtocolMessageType('DeleteUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERREQUEST,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.DeleteUserRequest)
  })
_sym_db.RegisterMessage(DeleteUserRequest)

DeleteUserMetadata = _reflection.GeneratedProtocolMessageType('DeleteUserMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERMETADATA,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.DeleteUserMetadata)
  })
_sym_db.RegisterMessage(DeleteUserMetadata)

GrantUserPermissionRequest = _reflection.GeneratedProtocolMessageType('GrantUserPermissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GRANTUSERPERMISSIONREQUEST,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.GrantUserPermissionRequest)
  })
_sym_db.RegisterMessage(GrantUserPermissionRequest)

GrantUserPermissionMetadata = _reflection.GeneratedProtocolMessageType('GrantUserPermissionMetadata', (_message.Message,), {
  'DESCRIPTOR' : _GRANTUSERPERMISSIONMETADATA,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.GrantUserPermissionMetadata)
  })
_sym_db.RegisterMessage(GrantUserPermissionMetadata)

RevokeUserPermissionRequest = _reflection.GeneratedProtocolMessageType('RevokeUserPermissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVOKEUSERPERMISSIONREQUEST,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.RevokeUserPermissionRequest)
  })
_sym_db.RegisterMessage(RevokeUserPermissionRequest)

RevokeUserPermissionMetadata = _reflection.GeneratedProtocolMessageType('RevokeUserPermissionMetadata', (_message.Message,), {
  'DESCRIPTOR' : _REVOKEUSERPERMISSIONMETADATA,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.user_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.RevokeUserPermissionMetadata)
  })
_sym_db.RegisterMessage(RevokeUserPermissionMetadata)

_USERSERVICE = DESCRIPTOR.services_by_name['UserService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037yandex.cloud.api.mdb.mongodb.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1;mongodb'
  _GETUSERREQUEST.fields_by_name['cluster_id']._options = None
  _GETUSERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _GETUSERREQUEST.fields_by_name['user_name']._options = None
  _GETUSERREQUEST.fields_by_name['user_name']._serialized_options = b'\350\3071\001\212\3101\004<=63\362\3071\r[a-zA-Z0-9_]*'
  _LISTUSERSREQUEST.fields_by_name['cluster_id']._options = None
  _LISTUSERSREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTUSERSREQUEST.fields_by_name['page_size']._options = None
  _LISTUSERSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTUSERSREQUEST.fields_by_name['page_token']._options = None
  _LISTUSERSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _CREATEUSERREQUEST.fields_by_name['cluster_id']._options = None
  _CREATEUSERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEUSERREQUEST.fields_by_name['cluster_id']._options = None
  _UPDATEUSERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEUSERREQUEST.fields_by_name['user_name']._options = None
  _UPDATEUSERREQUEST.fields_by_name['user_name']._serialized_options = b'\350\3071\001\212\3101\004<=63\362\3071\r[a-zA-Z0-9_]*'
  _UPDATEUSERREQUEST.fields_by_name['password']._options = None
  _UPDATEUSERREQUEST.fields_by_name['password']._serialized_options = b'\212\3101\0058-128'
  _DELETEUSERREQUEST.fields_by_name['cluster_id']._options = None
  _DELETEUSERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEUSERREQUEST.fields_by_name['user_name']._options = None
  _DELETEUSERREQUEST.fields_by_name['user_name']._serialized_options = b'\350\3071\001\212\3101\004<=63\362\3071\r[a-zA-Z0-9_]*'
  _GRANTUSERPERMISSIONREQUEST.fields_by_name['cluster_id']._options = None
  _GRANTUSERPERMISSIONREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _GRANTUSERPERMISSIONREQUEST.fields_by_name['user_name']._options = None
  _GRANTUSERPERMISSIONREQUEST.fields_by_name['user_name']._serialized_options = b'\350\3071\001\212\3101\004<=63\362\3071\r[a-zA-Z0-9_]*'
  _GRANTUSERPERMISSIONREQUEST.fields_by_name['permission']._options = None
  _GRANTUSERPERMISSIONREQUEST.fields_by_name['permission']._serialized_options = b'\350\3071\001'
  _REVOKEUSERPERMISSIONREQUEST.fields_by_name['cluster_id']._options = None
  _REVOKEUSERPERMISSIONREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _REVOKEUSERPERMISSIONREQUEST.fields_by_name['user_name']._options = None
  _REVOKEUSERPERMISSIONREQUEST.fields_by_name['user_name']._serialized_options = b'\350\3071\001\212\3101\004<=63\362\3071\r[a-zA-Z0-9_]*'
  _REVOKEUSERPERMISSIONREQUEST.fields_by_name['database_name']._options = None
  _REVOKEUSERPERMISSIONREQUEST.fields_by_name['database_name']._serialized_options = b'\350\3071\001\212\3101\004<=63\362\3071\016[a-zA-Z0-9_-]*'
  _USERSERVICE.methods_by_name['Get']._options = None
  _USERSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002=\022;/managed-mongodb/v1/clusters/{cluster_id}/users/{user_name}'
  _USERSERVICE.methods_by_name['List']._options = None
  _USERSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\0021\022//managed-mongodb/v1/clusters/{cluster_id}/users'
  _USERSERVICE.methods_by_name['Create']._options = None
  _USERSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\0024\"//managed-mongodb/v1/clusters/{cluster_id}/users:\001*\262\322*\032\n\022CreateUserMetadata\022\004User'
  _USERSERVICE.methods_by_name['Update']._options = None
  _USERSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002@2;/managed-mongodb/v1/clusters/{cluster_id}/users/{user_name}:\001*\262\322*\032\n\022UpdateUserMetadata\022\004User'
  _USERSERVICE.methods_by_name['Delete']._options = None
  _USERSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002=*;/managed-mongodb/v1/clusters/{cluster_id}/users/{user_name}\262\322*+\n\022DeleteUserMetadata\022\025google.protobuf.Empty'
  _USERSERVICE.methods_by_name['GrantPermission']._options = None
  _USERSERVICE.methods_by_name['GrantPermission']._serialized_options = b'\202\323\344\223\002P\"K/managed-mongodb/v1/clusters/{cluster_id}/users/{user_name}:grantPermission:\001*\262\322*#\n\033GrantUserPermissionMetadata\022\004User'
  _USERSERVICE.methods_by_name['RevokePermission']._options = None
  _USERSERVICE.methods_by_name['RevokePermission']._serialized_options = b'\202\323\344\223\002Q\"L/managed-mongodb/v1/clusters/{cluster_id}/users/{user_name}:revokePermission:\001*\262\322*$\n\034RevokeUserPermissionMetadata\022\004User'
  _GETUSERREQUEST._serialized_start=288
  _GETUSERREQUEST._serialized_end=388
  _LISTUSERSREQUEST._serialized_start=390
  _LISTUSERSREQUEST._serialized_end=504
  _LISTUSERSRESPONSE._serialized_start=506
  _LISTUSERSRESPONSE._serialized_end=600
  _CREATEUSERREQUEST._serialized_start=602
  _CREATEUSERREQUEST._serialized_end=713
  _CREATEUSERMETADATA._serialized_start=715
  _CREATEUSERMETADATA._serialized_end=774
  _UPDATEUSERREQUEST._serialized_start=777
  _UPDATEUSERREQUEST._serialized_end=1020
  _UPDATEUSERMETADATA._serialized_start=1022
  _UPDATEUSERMETADATA._serialized_end=1081
  _DELETEUSERREQUEST._serialized_start=1083
  _DELETEUSERREQUEST._serialized_end=1186
  _DELETEUSERMETADATA._serialized_start=1188
  _DELETEUSERMETADATA._serialized_end=1247
  _GRANTUSERPERMISSIONREQUEST._serialized_start=1250
  _GRANTUSERPERMISSIONREQUEST._serialized_end=1429
  _GRANTUSERPERMISSIONMETADATA._serialized_start=1431
  _GRANTUSERPERMISSIONMETADATA._serialized_end=1499
  _REVOKEUSERPERMISSIONREQUEST._serialized_start=1502
  _REVOKEUSERPERMISSIONREQUEST._serialized_end=1670
  _REVOKEUSERPERMISSIONMETADATA._serialized_start=1672
  _REVOKEUSERPERMISSIONMETADATA._serialized_end=1741
  _USERSERVICE._serialized_start=1744
  _USERSERVICE._serialized_end=3147
# @@protoc_insertion_point(module_scope)
