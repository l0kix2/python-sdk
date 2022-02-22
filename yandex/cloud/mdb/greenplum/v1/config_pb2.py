# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/greenplum/v1/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*yandex/cloud/mdb/greenplum/v1/config.proto\x12\x1dyandex.cloud.mdb.greenplum.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"P\n\tResources\x12\x1a\n\x12resource_preset_id\x18\x01 \x01(\t\x12\x11\n\tdisk_size\x18\x02 \x01(\x03\x12\x14\n\x0c\x64isk_type_id\x18\x03 \x01(\t\"\x90\x02\n\x16\x43onnectionPoolerConfig\x12L\n\x04mode\x18\x01 \x01(\x0e\x32>.yandex.cloud.mdb.greenplum.v1.ConnectionPoolerConfig.PoolMode\x12)\n\x04size\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x13\x63lient_idle_timeout\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"C\n\x08PoolMode\x12\x19\n\x15POOL_MODE_UNSPECIFIED\x10\x00\x12\x0b\n\x07SESSION\x10\x01\x12\x0f\n\x0bTRANSACTION\x10\x02\"U\n\x16MasterSubclusterConfig\x12;\n\tresources\x18\x01 \x01(\x0b\x32(.yandex.cloud.mdb.greenplum.v1.Resources\"V\n\x17SegmentSubclusterConfig\x12;\n\tresources\x18\x01 \x01(\x0b\x32(.yandex.cloud.mdb.greenplum.v1.Resources\"\xd3\x03\n\x13GreenplumConfig6_17\x12\x34\n\x0fmax_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16max_slot_wal_keep_size\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x42\n\x1dgp_workfile_limit_per_segment\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12@\n\x1bgp_workfile_limit_per_query\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x46\n!gp_workfile_limit_files_per_query\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x19max_prepared_transactions\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x17gp_workfile_compression\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\xd3\x03\n\x13GreenplumConfig6_19\x12\x34\n\x0fmax_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16max_slot_wal_keep_size\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x42\n\x1dgp_workfile_limit_per_segment\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12@\n\x1bgp_workfile_limit_per_query\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x46\n!gp_workfile_limit_files_per_query\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x19max_prepared_transactions\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x17gp_workfile_compression\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x81\x02\n\x16GreenplumConfigSet6_17\x12R\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_17B\x04\xe8\xc7\x31\x01\x12G\n\x0buser_config\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_17\x12J\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_17\"\x81\x02\n\x16GreenplumConfigSet6_19\x12R\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_19B\x04\xe8\xc7\x31\x01\x12G\n\x0buser_config\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_19\x12J\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_19\"\x8d\x02\n\x19\x43onnectionPoolerConfigSet\x12U\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.ConnectionPoolerConfigB\x04\xe8\xc7\x31\x01\x12J\n\x0buser_config\x18\x02 \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.ConnectionPoolerConfig\x12M\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.ConnectionPoolerConfigBp\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplumb\x06proto3')



_RESOURCES = DESCRIPTOR.message_types_by_name['Resources']
_CONNECTIONPOOLERCONFIG = DESCRIPTOR.message_types_by_name['ConnectionPoolerConfig']
_MASTERSUBCLUSTERCONFIG = DESCRIPTOR.message_types_by_name['MasterSubclusterConfig']
_SEGMENTSUBCLUSTERCONFIG = DESCRIPTOR.message_types_by_name['SegmentSubclusterConfig']
_GREENPLUMCONFIG6_17 = DESCRIPTOR.message_types_by_name['GreenplumConfig6_17']
_GREENPLUMCONFIG6_19 = DESCRIPTOR.message_types_by_name['GreenplumConfig6_19']
_GREENPLUMCONFIGSET6_17 = DESCRIPTOR.message_types_by_name['GreenplumConfigSet6_17']
_GREENPLUMCONFIGSET6_19 = DESCRIPTOR.message_types_by_name['GreenplumConfigSet6_19']
_CONNECTIONPOOLERCONFIGSET = DESCRIPTOR.message_types_by_name['ConnectionPoolerConfigSet']
_CONNECTIONPOOLERCONFIG_POOLMODE = _CONNECTIONPOOLERCONFIG.enum_types_by_name['PoolMode']
Resources = _reflection.GeneratedProtocolMessageType('Resources', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCES,
  '__module__' : 'yandex.cloud.mdb.greenplum.v1.config_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.Resources)
  })
_sym_db.RegisterMessage(Resources)

ConnectionPoolerConfig = _reflection.GeneratedProtocolMessageType('ConnectionPoolerConfig', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONPOOLERCONFIG,
  '__module__' : 'yandex.cloud.mdb.greenplum.v1.config_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.ConnectionPoolerConfig)
  })
_sym_db.RegisterMessage(ConnectionPoolerConfig)

MasterSubclusterConfig = _reflection.GeneratedProtocolMessageType('MasterSubclusterConfig', (_message.Message,), {
  'DESCRIPTOR' : _MASTERSUBCLUSTERCONFIG,
  '__module__' : 'yandex.cloud.mdb.greenplum.v1.config_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.MasterSubclusterConfig)
  })
_sym_db.RegisterMessage(MasterSubclusterConfig)

SegmentSubclusterConfig = _reflection.GeneratedProtocolMessageType('SegmentSubclusterConfig', (_message.Message,), {
  'DESCRIPTOR' : _SEGMENTSUBCLUSTERCONFIG,
  '__module__' : 'yandex.cloud.mdb.greenplum.v1.config_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.SegmentSubclusterConfig)
  })
_sym_db.RegisterMessage(SegmentSubclusterConfig)

GreenplumConfig6_17 = _reflection.GeneratedProtocolMessageType('GreenplumConfig6_17', (_message.Message,), {
  'DESCRIPTOR' : _GREENPLUMCONFIG6_17,
  '__module__' : 'yandex.cloud.mdb.greenplum.v1.config_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_17)
  })
_sym_db.RegisterMessage(GreenplumConfig6_17)

GreenplumConfig6_19 = _reflection.GeneratedProtocolMessageType('GreenplumConfig6_19', (_message.Message,), {
  'DESCRIPTOR' : _GREENPLUMCONFIG6_19,
  '__module__' : 'yandex.cloud.mdb.greenplum.v1.config_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_19)
  })
_sym_db.RegisterMessage(GreenplumConfig6_19)

GreenplumConfigSet6_17 = _reflection.GeneratedProtocolMessageType('GreenplumConfigSet6_17', (_message.Message,), {
  'DESCRIPTOR' : _GREENPLUMCONFIGSET6_17,
  '__module__' : 'yandex.cloud.mdb.greenplum.v1.config_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.GreenplumConfigSet6_17)
  })
_sym_db.RegisterMessage(GreenplumConfigSet6_17)

GreenplumConfigSet6_19 = _reflection.GeneratedProtocolMessageType('GreenplumConfigSet6_19', (_message.Message,), {
  'DESCRIPTOR' : _GREENPLUMCONFIGSET6_19,
  '__module__' : 'yandex.cloud.mdb.greenplum.v1.config_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.GreenplumConfigSet6_19)
  })
_sym_db.RegisterMessage(GreenplumConfigSet6_19)

ConnectionPoolerConfigSet = _reflection.GeneratedProtocolMessageType('ConnectionPoolerConfigSet', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONPOOLERCONFIGSET,
  '__module__' : 'yandex.cloud.mdb.greenplum.v1.config_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.greenplum.v1.ConnectionPoolerConfigSet)
  })
_sym_db.RegisterMessage(ConnectionPoolerConfigSet)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplum'
  _GREENPLUMCONFIGSET6_17.fields_by_name['effective_config']._options = None
  _GREENPLUMCONFIGSET6_17.fields_by_name['effective_config']._serialized_options = b'\350\3071\001'
  _GREENPLUMCONFIGSET6_19.fields_by_name['effective_config']._options = None
  _GREENPLUMCONFIGSET6_19.fields_by_name['effective_config']._serialized_options = b'\350\3071\001'
  _CONNECTIONPOOLERCONFIGSET.fields_by_name['effective_config']._options = None
  _CONNECTIONPOOLERCONFIGSET.fields_by_name['effective_config']._serialized_options = b'\350\3071\001'
  _RESOURCES._serialized_start=140
  _RESOURCES._serialized_end=220
  _CONNECTIONPOOLERCONFIG._serialized_start=223
  _CONNECTIONPOOLERCONFIG._serialized_end=495
  _CONNECTIONPOOLERCONFIG_POOLMODE._serialized_start=428
  _CONNECTIONPOOLERCONFIG_POOLMODE._serialized_end=495
  _MASTERSUBCLUSTERCONFIG._serialized_start=497
  _MASTERSUBCLUSTERCONFIG._serialized_end=582
  _SEGMENTSUBCLUSTERCONFIG._serialized_start=584
  _SEGMENTSUBCLUSTERCONFIG._serialized_end=670
  _GREENPLUMCONFIG6_17._serialized_start=673
  _GREENPLUMCONFIG6_17._serialized_end=1140
  _GREENPLUMCONFIG6_19._serialized_start=1143
  _GREENPLUMCONFIG6_19._serialized_end=1610
  _GREENPLUMCONFIGSET6_17._serialized_start=1613
  _GREENPLUMCONFIGSET6_17._serialized_end=1870
  _GREENPLUMCONFIGSET6_19._serialized_start=1873
  _GREENPLUMCONFIGSET6_19._serialized_end=2130
  _CONNECTIONPOOLERCONFIGSET._serialized_start=2133
  _CONNECTIONPOOLERCONFIGSET._serialized_end=2402
# @@protoc_insertion_point(module_scope)
