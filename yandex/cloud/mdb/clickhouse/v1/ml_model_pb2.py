# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/clickhouse/v1/ml_model.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/mdb/clickhouse/v1/ml_model.proto\x12\x1eyandex.cloud.mdb.clickhouse.v1\"s\n\x07MlModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncluster_id\x18\x02 \x01(\t\x12\x39\n\x04type\x18\x03 \x01(\x0e\x32+.yandex.cloud.mdb.clickhouse.v1.MlModelType\x12\x0b\n\x03uri\x18\x04 \x01(\t*H\n\x0bMlModelType\x12\x1d\n\x19ML_MODEL_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16ML_MODEL_TYPE_CATBOOST\x10\x01\x42s\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouseb\x06proto3')

_MLMODELTYPE = DESCRIPTOR.enum_types_by_name['MlModelType']
MlModelType = enum_type_wrapper.EnumTypeWrapper(_MLMODELTYPE)
ML_MODEL_TYPE_UNSPECIFIED = 0
ML_MODEL_TYPE_CATBOOST = 1


_MLMODEL = DESCRIPTOR.message_types_by_name['MlModel']
MlModel = _reflection.GeneratedProtocolMessageType('MlModel', (_message.Message,), {
  'DESCRIPTOR' : _MLMODEL,
  '__module__' : 'yandex.cloud.mdb.clickhouse.v1.ml_model_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.clickhouse.v1.MlModel)
  })
_sym_db.RegisterMessage(MlModel)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"yandex.cloud.api.mdb.clickhouse.v1ZMgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/clickhouse/v1;clickhouse'
  _MLMODELTYPE._serialized_start=198
  _MLMODELTYPE._serialized_end=270
  _MLMODEL._serialized_start=81
  _MLMODEL._serialized_end=196
# @@protoc_insertion_point(module_scope)
