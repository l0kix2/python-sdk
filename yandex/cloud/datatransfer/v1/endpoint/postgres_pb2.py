# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datatransfer/v1/endpoint/postgres.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.datatransfer.v1.endpoint import common_pb2 as yandex_dot_cloud_dot_datatransfer_dot_v1_dot_endpoint_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4yandex/cloud/datatransfer/v1/endpoint/postgres.proto\x12%yandex.cloud.datatransfer.v1.endpoint\x1a\x32yandex/cloud/datatransfer/v1/endpoint/common.proto\"\x81\n\n\x1ePostgresObjectTransferSettings\x12L\n\x08sequence\x18\x01 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12U\n\x11sequence_owned_by\x18\x02 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12I\n\x05table\x18\x03 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12O\n\x0bprimary_key\x18\x04 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12Q\n\rfk_constraint\x18\x05 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12R\n\x0e\x64\x65\x66\x61ult_values\x18\x06 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12N\n\nconstraint\x18\x07 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12I\n\x05index\x18\x08 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12H\n\x04view\x18\t \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12L\n\x08\x66unction\x18\n \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12K\n\x07trigger\x18\x0b \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12H\n\x04type\x18\x0c \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12H\n\x04rule\x18\r \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12M\n\tcollation\x18\x0e \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12J\n\x06policy\x18\x0f \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\x12H\n\x04\x63\x61st\x18\x10 \x01(\x0e\x32:.yandex.cloud.datatransfer.v1.endpoint.ObjectTransferStage\"\x85\x01\n\x11OnPremisePostgres\x12\r\n\x05hosts\x18\x05 \x03(\t\x12\x0c\n\x04port\x18\x02 \x01(\x03\x12@\n\x08tls_mode\x18\x06 \x01(\x0b\x32..yandex.cloud.datatransfer.v1.endpoint.TLSMode\x12\x11\n\tsubnet_id\x18\x04 \x01(\t\"\x8c\x01\n\x12PostgresConnection\x12\x18\n\x0emdb_cluster_id\x18\x01 \x01(\tH\x00\x12N\n\non_premise\x18\x02 \x01(\x0b\x32\x38.yandex.cloud.datatransfer.v1.endpoint.OnPremisePostgresH\x00\x42\x0c\n\nconnection\"\x8e\x03\n\x0ePostgresSource\x12M\n\nconnection\x18\x01 \x01(\x0b\x32\x39.yandex.cloud.datatransfer.v1.endpoint.PostgresConnection\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12?\n\x08password\x18\x04 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.Secret\x12\x16\n\x0einclude_tables\x18\x05 \x03(\t\x12\x16\n\x0e\x65xclude_tables\x18\x06 \x03(\t\x12\x1b\n\x13slot_byte_lag_limit\x18\x08 \x01(\x03\x12\x16\n\x0eservice_schema\x18\t \x01(\t\x12g\n\x18object_transfer_settings\x18\r \x01(\x0b\x32\x45.yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings\"\x8e\x02\n\x0ePostgresTarget\x12M\n\nconnection\x18\x01 \x01(\x0b\x32\x39.yandex.cloud.datatransfer.v1.endpoint.PostgresConnection\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12?\n\x08password\x18\x04 \x01(\x0b\x32-.yandex.cloud.datatransfer.v1.endpoint.Secret\x12L\n\x0e\x63leanup_policy\x18\x05 \x01(\x0e\x32\x34.yandex.cloud.datatransfer.v1.endpoint.CleanupPolicyB\xa7\x01\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\xaa\x02%Yandex.Cloud.Datatransfer.V1.EndPointb\x06proto3')



_POSTGRESOBJECTTRANSFERSETTINGS = DESCRIPTOR.message_types_by_name['PostgresObjectTransferSettings']
_ONPREMISEPOSTGRES = DESCRIPTOR.message_types_by_name['OnPremisePostgres']
_POSTGRESCONNECTION = DESCRIPTOR.message_types_by_name['PostgresConnection']
_POSTGRESSOURCE = DESCRIPTOR.message_types_by_name['PostgresSource']
_POSTGRESTARGET = DESCRIPTOR.message_types_by_name['PostgresTarget']
PostgresObjectTransferSettings = _reflection.GeneratedProtocolMessageType('PostgresObjectTransferSettings', (_message.Message,), {
  'DESCRIPTOR' : _POSTGRESOBJECTTRANSFERSETTINGS,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.postgres_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.PostgresObjectTransferSettings)
  })
_sym_db.RegisterMessage(PostgresObjectTransferSettings)

OnPremisePostgres = _reflection.GeneratedProtocolMessageType('OnPremisePostgres', (_message.Message,), {
  'DESCRIPTOR' : _ONPREMISEPOSTGRES,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.postgres_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.OnPremisePostgres)
  })
_sym_db.RegisterMessage(OnPremisePostgres)

PostgresConnection = _reflection.GeneratedProtocolMessageType('PostgresConnection', (_message.Message,), {
  'DESCRIPTOR' : _POSTGRESCONNECTION,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.postgres_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.PostgresConnection)
  })
_sym_db.RegisterMessage(PostgresConnection)

PostgresSource = _reflection.GeneratedProtocolMessageType('PostgresSource', (_message.Message,), {
  'DESCRIPTOR' : _POSTGRESSOURCE,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.postgres_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.PostgresSource)
  })
_sym_db.RegisterMessage(PostgresSource)

PostgresTarget = _reflection.GeneratedProtocolMessageType('PostgresTarget', (_message.Message,), {
  'DESCRIPTOR' : _POSTGRESTARGET,
  '__module__' : 'yandex.cloud.datatransfer.v1.endpoint.postgres_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.datatransfer.v1.endpoint.PostgresTarget)
  })
_sym_db.RegisterMessage(PostgresTarget)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)yandex.cloud.api.datatransfer.v1.endpointZRgithub.com/yandex-cloud/go-genproto/yandex/cloud/datatransfer/v1/endpoint;endpoint\252\002%Yandex.Cloud.Datatransfer.V1.EndPoint'
  _POSTGRESOBJECTTRANSFERSETTINGS._serialized_start=148
  _POSTGRESOBJECTTRANSFERSETTINGS._serialized_end=1429
  _ONPREMISEPOSTGRES._serialized_start=1432
  _ONPREMISEPOSTGRES._serialized_end=1565
  _POSTGRESCONNECTION._serialized_start=1568
  _POSTGRESCONNECTION._serialized_end=1708
  _POSTGRESSOURCE._serialized_start=1711
  _POSTGRESSOURCE._serialized_end=2109
  _POSTGRESTARGET._serialized_start=2112
  _POSTGRESTARGET._serialized_end=2382
# @@protoc_insertion_point(module_scope)
