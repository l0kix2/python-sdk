# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/elasticsearch/v1/backup_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.elasticsearch.v1 import backup_pb2 as yandex_dot_cloud_dot_mdb_dot_elasticsearch_dot_v1_dot_backup__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6yandex/cloud/mdb/elasticsearch/v1/backup_service.proto\x12!yandex.cloud.mdb.elasticsearch.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dyandex/cloud/validation.proto\x1a.yandex/cloud/mdb/elasticsearch/v1/backup.proto\"+\n\x10GetBackupRequest\x12\x17\n\tbackup_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"s\n\x12ListBackupsRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"j\n\x13ListBackupsResponse\x12:\n\x07\x62\x61\x63kups\x18\x01 \x03(\x0b\x32).yandex.cloud.mdb.elasticsearch.v1.Backup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xd1\x02\n\rBackupService\x12\x9c\x01\n\x03Get\x12\x33.yandex.cloud.mdb.elasticsearch.v1.GetBackupRequest\x1a).yandex.cloud.mdb.elasticsearch.v1.Backup\"5\x82\xd3\xe4\x93\x02/\x12-/managed-elasticsearch/v1/backups/{backup_id}\x12\xa0\x01\n\x04List\x12\x35.yandex.cloud.mdb.elasticsearch.v1.ListBackupsRequest\x1a\x36.yandex.cloud.mdb.elasticsearch.v1.ListBackupsResponse\")\x82\xd3\xe4\x93\x02#\x12!/managed-elasticsearch/v1/backupsB|\n%yandex.cloud.api.mdb.elasticsearch.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/elasticsearch/v1;elasticsearchb\x06proto3')



_GETBACKUPREQUEST = DESCRIPTOR.message_types_by_name['GetBackupRequest']
_LISTBACKUPSREQUEST = DESCRIPTOR.message_types_by_name['ListBackupsRequest']
_LISTBACKUPSRESPONSE = DESCRIPTOR.message_types_by_name['ListBackupsResponse']
GetBackupRequest = _reflection.GeneratedProtocolMessageType('GetBackupRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBACKUPREQUEST,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.backup_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.GetBackupRequest)
  })
_sym_db.RegisterMessage(GetBackupRequest)

ListBackupsRequest = _reflection.GeneratedProtocolMessageType('ListBackupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBACKUPSREQUEST,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.backup_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.ListBackupsRequest)
  })
_sym_db.RegisterMessage(ListBackupsRequest)

ListBackupsResponse = _reflection.GeneratedProtocolMessageType('ListBackupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBACKUPSRESPONSE,
  '__module__' : 'yandex.cloud.mdb.elasticsearch.v1.backup_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.elasticsearch.v1.ListBackupsResponse)
  })
_sym_db.RegisterMessage(ListBackupsResponse)

_BACKUPSERVICE = DESCRIPTOR.services_by_name['BackupService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%yandex.cloud.api.mdb.elasticsearch.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/elasticsearch/v1;elasticsearch'
  _GETBACKUPREQUEST.fields_by_name['backup_id']._options = None
  _GETBACKUPREQUEST.fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _LISTBACKUPSREQUEST.fields_by_name['folder_id']._options = None
  _LISTBACKUPSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTBACKUPSREQUEST.fields_by_name['page_size']._options = None
  _LISTBACKUPSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTBACKUPSREQUEST.fields_by_name['page_token']._options = None
  _LISTBACKUPSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _BACKUPSERVICE.methods_by_name['Get']._options = None
  _BACKUPSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002/\022-/managed-elasticsearch/v1/backups/{backup_id}'
  _BACKUPSERVICE.methods_by_name['List']._options = None
  _BACKUPSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002#\022!/managed-elasticsearch/v1/backups'
  _GETBACKUPREQUEST._serialized_start=202
  _GETBACKUPREQUEST._serialized_end=245
  _LISTBACKUPSREQUEST._serialized_start=247
  _LISTBACKUPSREQUEST._serialized_end=362
  _LISTBACKUPSRESPONSE._serialized_start=364
  _LISTBACKUPSRESPONSE._serialized_end=470
  _BACKUPSERVICE._serialized_start=473
  _BACKUPSERVICE._serialized_end=810
# @@protoc_insertion_point(module_scope)
