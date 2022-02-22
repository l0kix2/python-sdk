# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mysql/v1/cluster.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.mysql.v1.config import mysql5_7_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_config_dot_mysql5__7__pb2
from yandex.cloud.mdb.mysql.v1.config import mysql8_0_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_config_dot_mysql8__0__pb2
from yandex.cloud.mdb.mysql.v1 import maintenance_pb2 as yandex_dot_cloud_dot_mdb_dot_mysql_dot_v1_dot_maintenance__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'yandex/cloud/mdb/mysql/v1/cluster.proto\x12\x19yandex.cloud.mdb.mysql.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/type/timeofday.proto\x1a\x1dyandex/cloud/validation.proto\x1a/yandex/cloud/mdb/mysql/v1/config/mysql5_7.proto\x1a/yandex/cloud/mdb/mysql/v1/config/mysql8_0.proto\x1a+yandex/cloud/mdb/mysql/v1/maintenance.proto\"\x84\x08\n\x07\x43luster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x06labels\x18\x06 \x03(\x0b\x32..yandex.cloud.mdb.mysql.v1.Cluster.LabelsEntry\x12\x43\n\x0b\x65nvironment\x18\x07 \x01(\x0e\x32..yandex.cloud.mdb.mysql.v1.Cluster.Environment\x12\x39\n\nmonitoring\x18\x08 \x03(\x0b\x32%.yandex.cloud.mdb.mysql.v1.Monitoring\x12\x38\n\x06\x63onfig\x18\t \x01(\x0b\x32(.yandex.cloud.mdb.mysql.v1.ClusterConfig\x12\x12\n\nnetwork_id\x18\n \x01(\t\x12\x39\n\x06health\x18\x0b \x01(\x0e\x32).yandex.cloud.mdb.mysql.v1.Cluster.Health\x12\x39\n\x06status\x18\x0c \x01(\x0e\x32).yandex.cloud.mdb.mysql.v1.Cluster.Status\x12H\n\x12maintenance_window\x18\r \x01(\x0b\x32,.yandex.cloud.mdb.mysql.v1.MaintenanceWindow\x12J\n\x11planned_operation\x18\x0e \x01(\x0b\x32/.yandex.cloud.mdb.mysql.v1.MaintenanceOperation\x12\x1a\n\x12security_group_ids\x18\x0f \x03(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x10 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x0b\x45nvironment\x12\x1b\n\x17\x45NVIRONMENT_UNSPECIFIED\x10\x00\x12\x0e\n\nPRODUCTION\x10\x01\x12\r\n\tPRESTABLE\x10\x02\"?\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"y\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x0c\n\x08STOPPING\x10\x05\x12\x0b\n\x07STOPPED\x10\x06\x12\x0c\n\x08STARTING\x10\x07\"=\n\nMonitoring\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\"\x95\x03\n\rClusterConfig\x12\x0f\n\x07version\x18\x01 \x01(\t\x12`\n\x10mysql_config_5_7\x18\x02 \x01(\x0b\x32\x33.yandex.cloud.mdb.mysql.v1.config.MysqlConfigSet5_7H\x00R\x0fmysqlConfig_5_7\x12`\n\x10mysql_config_8_0\x18\x06 \x01(\x0b\x32\x33.yandex.cloud.mdb.mysql.v1.config.MysqlConfigSet8_0H\x00R\x0fmysqlConfig_8_0\x12\x37\n\tresources\x18\x03 \x01(\x0b\x32$.yandex.cloud.mdb.mysql.v1.Resources\x12\x33\n\x13\x62\x61\x63kup_window_start\x18\x04 \x01(\x0b\x32\x16.google.type.TimeOfDay\x12\x31\n\x06\x61\x63\x63\x65ss\x18\x05 \x01(\x0b\x32!.yandex.cloud.mdb.mysql.v1.AccessB\x0e\n\x0cmysql_config\"\x92\x04\n\x04Host\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\x0f\n\x07zone_id\x18\x03 \x01(\t\x12\x37\n\tresources\x18\x04 \x01(\x0b\x32$.yandex.cloud.mdb.mysql.v1.Resources\x12\x32\n\x04role\x18\x05 \x01(\x0e\x32$.yandex.cloud.mdb.mysql.v1.Host.Role\x12\x36\n\x06health\x18\x06 \x01(\x0e\x32&.yandex.cloud.mdb.mysql.v1.Host.Health\x12\x34\n\x08services\x18\x07 \x03(\x0b\x32\".yandex.cloud.mdb.mysql.v1.Service\x12\x11\n\tsubnet_id\x18\x08 \x01(\t\x12\x18\n\x10\x61ssign_public_ip\x18\t \x01(\x08\x12\x1a\n\x12replication_source\x18\n \x01(\t\x12\"\n\x0f\x62\x61\x63kup_priority\x18\x0b \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x1b\n\x08priority\x18\x0c \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\"1\n\x04Role\x12\x10\n\x0cROLE_UNKNOWN\x10\x00\x12\n\n\x06MASTER\x10\x01\x12\x0b\n\x07REPLICA\x10\x02\"?\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\x12\x0c\n\x08\x44\x45GRADED\x10\x03\"\xd7\x01\n\x07Service\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.yandex.cloud.mdb.mysql.v1.Service.Type\x12\x39\n\x06health\x18\x02 \x01(\x0e\x32).yandex.cloud.mdb.mysql.v1.Service.Health\"\'\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05MYSQL\x10\x01\"1\n\x06Health\x12\x12\n\x0eHEALTH_UNKNOWN\x10\x00\x12\t\n\x05\x41LIVE\x10\x01\x12\x08\n\x04\x44\x45\x41\x44\x10\x02\"P\n\tResources\x12\x1a\n\x12resource_preset_id\x18\x01 \x01(\t\x12\x11\n\tdisk_size\x18\x02 \x01(\x03\x12\x14\n\x0c\x64isk_type_id\x18\x03 \x01(\t\",\n\x06\x41\x63\x63\x65ss\x12\x11\n\tdata_lens\x18\x01 \x01(\x08\x12\x0f\n\x07web_sql\x18\x02 \x01(\x08\"\x8d\x01\n\x16PerformanceDiagnostics\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12/\n\x1asessions_sampling_interval\x18\x02 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x31-86400\x12\x31\n\x1cstatements_sampling_interval\x18\x03 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x31-86400Bd\n\x1dyandex.cloud.api.mdb.mysql.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1;mysqlb\x06proto3')



_CLUSTER = DESCRIPTOR.message_types_by_name['Cluster']
_CLUSTER_LABELSENTRY = _CLUSTER.nested_types_by_name['LabelsEntry']
_MONITORING = DESCRIPTOR.message_types_by_name['Monitoring']
_CLUSTERCONFIG = DESCRIPTOR.message_types_by_name['ClusterConfig']
_HOST = DESCRIPTOR.message_types_by_name['Host']
_SERVICE = DESCRIPTOR.message_types_by_name['Service']
_RESOURCES = DESCRIPTOR.message_types_by_name['Resources']
_ACCESS = DESCRIPTOR.message_types_by_name['Access']
_PERFORMANCEDIAGNOSTICS = DESCRIPTOR.message_types_by_name['PerformanceDiagnostics']
_CLUSTER_ENVIRONMENT = _CLUSTER.enum_types_by_name['Environment']
_CLUSTER_HEALTH = _CLUSTER.enum_types_by_name['Health']
_CLUSTER_STATUS = _CLUSTER.enum_types_by_name['Status']
_HOST_ROLE = _HOST.enum_types_by_name['Role']
_HOST_HEALTH = _HOST.enum_types_by_name['Health']
_SERVICE_TYPE = _SERVICE.enum_types_by_name['Type']
_SERVICE_HEALTH = _SERVICE.enum_types_by_name['Health']
Cluster = _reflection.GeneratedProtocolMessageType('Cluster', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLUSTER_LABELSENTRY,
    '__module__' : 'yandex.cloud.mdb.mysql.v1.cluster_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.Cluster.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CLUSTER,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.Cluster)
  })
_sym_db.RegisterMessage(Cluster)
_sym_db.RegisterMessage(Cluster.LabelsEntry)

Monitoring = _reflection.GeneratedProtocolMessageType('Monitoring', (_message.Message,), {
  'DESCRIPTOR' : _MONITORING,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.Monitoring)
  })
_sym_db.RegisterMessage(Monitoring)

ClusterConfig = _reflection.GeneratedProtocolMessageType('ClusterConfig', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERCONFIG,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.ClusterConfig)
  })
_sym_db.RegisterMessage(ClusterConfig)

Host = _reflection.GeneratedProtocolMessageType('Host', (_message.Message,), {
  'DESCRIPTOR' : _HOST,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.Host)
  })
_sym_db.RegisterMessage(Host)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {
  'DESCRIPTOR' : _SERVICE,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.Service)
  })
_sym_db.RegisterMessage(Service)

Resources = _reflection.GeneratedProtocolMessageType('Resources', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCES,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.Resources)
  })
_sym_db.RegisterMessage(Resources)

Access = _reflection.GeneratedProtocolMessageType('Access', (_message.Message,), {
  'DESCRIPTOR' : _ACCESS,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.Access)
  })
_sym_db.RegisterMessage(Access)

PerformanceDiagnostics = _reflection.GeneratedProtocolMessageType('PerformanceDiagnostics', (_message.Message,), {
  'DESCRIPTOR' : _PERFORMANCEDIAGNOSTICS,
  '__module__' : 'yandex.cloud.mdb.mysql.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mysql.v1.PerformanceDiagnostics)
  })
_sym_db.RegisterMessage(PerformanceDiagnostics)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035yandex.cloud.api.mdb.mysql.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mysql/v1;mysql'
  _CLUSTER_LABELSENTRY._options = None
  _CLUSTER_LABELSENTRY._serialized_options = b'8\001'
  _HOST.fields_by_name['backup_priority']._options = None
  _HOST.fields_by_name['backup_priority']._serialized_options = b'\372\3071\0050-100'
  _HOST.fields_by_name['priority']._options = None
  _HOST.fields_by_name['priority']._serialized_options = b'\372\3071\0050-100'
  _PERFORMANCEDIAGNOSTICS.fields_by_name['sessions_sampling_interval']._options = None
  _PERFORMANCEDIAGNOSTICS.fields_by_name['sessions_sampling_interval']._serialized_options = b'\372\3071\0071-86400'
  _PERFORMANCEDIAGNOSTICS.fields_by_name['statements_sampling_interval']._options = None
  _PERFORMANCEDIAGNOSTICS.fields_by_name['statements_sampling_interval']._serialized_options = b'\372\3071\0071-86400'
  _CLUSTER._serialized_start=307
  _CLUSTER._serialized_end=1335
  _CLUSTER_LABELSENTRY._serialized_start=1027
  _CLUSTER_LABELSENTRY._serialized_end=1072
  _CLUSTER_ENVIRONMENT._serialized_start=1074
  _CLUSTER_ENVIRONMENT._serialized_end=1147
  _CLUSTER_HEALTH._serialized_start=1149
  _CLUSTER_HEALTH._serialized_end=1212
  _CLUSTER_STATUS._serialized_start=1214
  _CLUSTER_STATUS._serialized_end=1335
  _MONITORING._serialized_start=1337
  _MONITORING._serialized_end=1398
  _CLUSTERCONFIG._serialized_start=1401
  _CLUSTERCONFIG._serialized_end=1806
  _HOST._serialized_start=1809
  _HOST._serialized_end=2339
  _HOST_ROLE._serialized_start=2225
  _HOST_ROLE._serialized_end=2274
  _HOST_HEALTH._serialized_start=1149
  _HOST_HEALTH._serialized_end=1212
  _SERVICE._serialized_start=2342
  _SERVICE._serialized_end=2557
  _SERVICE_TYPE._serialized_start=2467
  _SERVICE_TYPE._serialized_end=2506
  _SERVICE_HEALTH._serialized_start=1149
  _SERVICE_HEALTH._serialized_end=1198
  _RESOURCES._serialized_start=2559
  _RESOURCES._serialized_end=2639
  _ACCESS._serialized_start=2641
  _ACCESS._serialized_end=2685
  _PERFORMANCEDIAGNOSTICS._serialized_start=2688
  _PERFORMANCEDIAGNOSTICS._serialized_end=2829
# @@protoc_insertion_point(module_scope)
