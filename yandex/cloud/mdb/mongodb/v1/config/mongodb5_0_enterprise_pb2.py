# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/mongodb/v1/config/mongodb5_0_enterprise.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>yandex/cloud/mdb/mongodb/v1/config/mongodb5_0_enterprise.proto\x12\"yandex.cloud.mdb.mongodb.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xe0\x0b\n\x1aMongodConfig5_0_enterprise\x12W\n\x07storage\x18\x01 \x01(\x0b\x32\x46.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage\x12n\n\x13operation_profiling\x18\x02 \x01(\x0b\x32Q.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.OperationProfiling\x12S\n\x03net\x18\x03 \x01(\x0b\x32\x46.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Network\x1a\xd1\x06\n\x07Storage\x12\x66\n\x0bwired_tiger\x18\x01 \x01(\x0b\x32Q.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.WiredTiger\x12_\n\x07journal\x18\x02 \x01(\x0b\x32N.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.Journal\x1a\xb0\x04\n\nWiredTiger\x12u\n\rengine_config\x18\x01 \x01(\x0b\x32^.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.WiredTiger.EngineConfig\x12}\n\x11\x63ollection_config\x18\x02 \x01(\x0b\x32\x62.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.WiredTiger.CollectionConfig\x1a\x43\n\x0c\x45ngineConfig\x12\x33\n\rcache_size_gb\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x1a\xe6\x01\n\x10\x43ollectionConfig\x12\x87\x01\n\x10\x62lock_compressor\x18\x01 \x01(\x0e\x32m.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.WiredTiger.CollectionConfig.Compressor\"H\n\nCompressor\x12\x1a\n\x16\x43OMPRESSOR_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\n\n\x06SNAPPY\x10\x02\x12\x08\n\x04ZLIB\x10\x03\x1aJ\n\x07Journal\x12?\n\x0f\x63ommit_interval\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\t\xfa\xc7\x31\x05\x31-500\x1a\xf7\x01\n\x12OperationProfiling\x12\x64\n\x04mode\x18\x01 \x01(\x0e\x32V.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.OperationProfiling.Mode\x12>\n\x11slow_op_threshold\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0b\n\x07SLOW_OP\x10\x02\x12\x07\n\x03\x41LL\x10\x03\x1aV\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\"\xd9\x07\n\x1cMongoCfgConfig5_0_enterprise\x12Y\n\x07storage\x18\x01 \x01(\x0b\x32H.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.Storage\x12p\n\x13operation_profiling\x18\x02 \x01(\x0b\x32S.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.OperationProfiling\x12U\n\x03net\x18\x03 \x01(\x0b\x32H.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.Network\x1a\xc0\x02\n\x07Storage\x12h\n\x0bwired_tiger\x18\x01 \x01(\x0b\x32S.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.Storage.WiredTiger\x1a\xca\x01\n\nWiredTiger\x12w\n\rengine_config\x18\x01 \x01(\x0b\x32`.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.Storage.WiredTiger.EngineConfig\x1a\x43\n\x0c\x45ngineConfig\x12\x33\n\rcache_size_gb\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x1a\xf9\x01\n\x12OperationProfiling\x12\x66\n\x04mode\x18\x01 \x01(\x0e\x32X.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.OperationProfiling.Mode\x12>\n\x11slow_op_threshold\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x06\xfa\xc7\x31\x02>0\";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x07\n\x03OFF\x10\x01\x12\x0b\n\x07SLOW_OP\x10\x02\x12\x07\n\x03\x41LL\x10\x03\x1aV\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\"\xc9\x01\n\x1aMongosConfig5_0_enterprise\x12S\n\x03net\x18\x01 \x01(\x0b\x32\x46.yandex.cloud.mdb.mongodb.v1.config.MongosConfig5_0_enterprise.Network\x1aV\n\x07Network\x12K\n\x18max_incoming_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-16384\"\xa6\x02\n\x1dMongodConfigSet5_0_enterprise\x12X\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise\x12S\n\x0buser_config\x18\x02 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise\x12V\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise\"\xae\x02\n\x1fMongoCfgConfigSet5_0_enterprise\x12Z\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32@.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise\x12U\n\x0buser_config\x18\x02 \x01(\x0b\x32@.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise\x12X\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32@.yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise\"\xa6\x02\n\x1dMongosConfigSet5_0_enterprise\x12X\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongosConfig5_0_enterprise\x12S\n\x0buser_config\x18\x02 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongosConfig5_0_enterprise\x12V\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32>.yandex.cloud.mdb.mongodb.v1.config.MongosConfig5_0_enterpriseBx\n&yandex.cloud.api.mdb.mongodb.v1.configZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1/config;mongodbb\x06proto3')



_MONGODCONFIG5_0_ENTERPRISE = DESCRIPTOR.message_types_by_name['MongodConfig5_0_enterprise']
_MONGODCONFIG5_0_ENTERPRISE_STORAGE = _MONGODCONFIG5_0_ENTERPRISE.nested_types_by_name['Storage']
_MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER = _MONGODCONFIG5_0_ENTERPRISE_STORAGE.nested_types_by_name['WiredTiger']
_MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG = _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER.nested_types_by_name['EngineConfig']
_MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG = _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER.nested_types_by_name['CollectionConfig']
_MONGODCONFIG5_0_ENTERPRISE_STORAGE_JOURNAL = _MONGODCONFIG5_0_ENTERPRISE_STORAGE.nested_types_by_name['Journal']
_MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING = _MONGODCONFIG5_0_ENTERPRISE.nested_types_by_name['OperationProfiling']
_MONGODCONFIG5_0_ENTERPRISE_NETWORK = _MONGODCONFIG5_0_ENTERPRISE.nested_types_by_name['Network']
_MONGOCFGCONFIG5_0_ENTERPRISE = DESCRIPTOR.message_types_by_name['MongoCfgConfig5_0_enterprise']
_MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE = _MONGOCFGCONFIG5_0_ENTERPRISE.nested_types_by_name['Storage']
_MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER = _MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE.nested_types_by_name['WiredTiger']
_MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG = _MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER.nested_types_by_name['EngineConfig']
_MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING = _MONGOCFGCONFIG5_0_ENTERPRISE.nested_types_by_name['OperationProfiling']
_MONGOCFGCONFIG5_0_ENTERPRISE_NETWORK = _MONGOCFGCONFIG5_0_ENTERPRISE.nested_types_by_name['Network']
_MONGOSCONFIG5_0_ENTERPRISE = DESCRIPTOR.message_types_by_name['MongosConfig5_0_enterprise']
_MONGOSCONFIG5_0_ENTERPRISE_NETWORK = _MONGOSCONFIG5_0_ENTERPRISE.nested_types_by_name['Network']
_MONGODCONFIGSET5_0_ENTERPRISE = DESCRIPTOR.message_types_by_name['MongodConfigSet5_0_enterprise']
_MONGOCFGCONFIGSET5_0_ENTERPRISE = DESCRIPTOR.message_types_by_name['MongoCfgConfigSet5_0_enterprise']
_MONGOSCONFIGSET5_0_ENTERPRISE = DESCRIPTOR.message_types_by_name['MongosConfigSet5_0_enterprise']
_MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG_COMPRESSOR = _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG.enum_types_by_name['Compressor']
_MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING_MODE = _MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING.enum_types_by_name['Mode']
_MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING_MODE = _MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING.enum_types_by_name['Mode']
MongodConfig5_0_enterprise = _reflection.GeneratedProtocolMessageType('MongodConfig5_0_enterprise', (_message.Message,), {

  'Storage' : _reflection.GeneratedProtocolMessageType('Storage', (_message.Message,), {

    'WiredTiger' : _reflection.GeneratedProtocolMessageType('WiredTiger', (_message.Message,), {

      'EngineConfig' : _reflection.GeneratedProtocolMessageType('EngineConfig', (_message.Message,), {
        'DESCRIPTOR' : _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG,
        '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
        # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.WiredTiger.EngineConfig)
        })
      ,

      'CollectionConfig' : _reflection.GeneratedProtocolMessageType('CollectionConfig', (_message.Message,), {
        'DESCRIPTOR' : _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG,
        '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
        # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.WiredTiger.CollectionConfig)
        })
      ,
      'DESCRIPTOR' : _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER,
      '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
      # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.WiredTiger)
      })
    ,

    'Journal' : _reflection.GeneratedProtocolMessageType('Journal', (_message.Message,), {
      'DESCRIPTOR' : _MONGODCONFIG5_0_ENTERPRISE_STORAGE_JOURNAL,
      '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
      # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage.Journal)
      })
    ,
    'DESCRIPTOR' : _MONGODCONFIG5_0_ENTERPRISE_STORAGE,
    '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Storage)
    })
  ,

  'OperationProfiling' : _reflection.GeneratedProtocolMessageType('OperationProfiling', (_message.Message,), {
    'DESCRIPTOR' : _MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING,
    '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.OperationProfiling)
    })
  ,

  'Network' : _reflection.GeneratedProtocolMessageType('Network', (_message.Message,), {
    'DESCRIPTOR' : _MONGODCONFIG5_0_ENTERPRISE_NETWORK,
    '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise.Network)
    })
  ,
  'DESCRIPTOR' : _MONGODCONFIG5_0_ENTERPRISE,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongodConfig5_0_enterprise)
  })
_sym_db.RegisterMessage(MongodConfig5_0_enterprise)
_sym_db.RegisterMessage(MongodConfig5_0_enterprise.Storage)
_sym_db.RegisterMessage(MongodConfig5_0_enterprise.Storage.WiredTiger)
_sym_db.RegisterMessage(MongodConfig5_0_enterprise.Storage.WiredTiger.EngineConfig)
_sym_db.RegisterMessage(MongodConfig5_0_enterprise.Storage.WiredTiger.CollectionConfig)
_sym_db.RegisterMessage(MongodConfig5_0_enterprise.Storage.Journal)
_sym_db.RegisterMessage(MongodConfig5_0_enterprise.OperationProfiling)
_sym_db.RegisterMessage(MongodConfig5_0_enterprise.Network)

MongoCfgConfig5_0_enterprise = _reflection.GeneratedProtocolMessageType('MongoCfgConfig5_0_enterprise', (_message.Message,), {

  'Storage' : _reflection.GeneratedProtocolMessageType('Storage', (_message.Message,), {

    'WiredTiger' : _reflection.GeneratedProtocolMessageType('WiredTiger', (_message.Message,), {

      'EngineConfig' : _reflection.GeneratedProtocolMessageType('EngineConfig', (_message.Message,), {
        'DESCRIPTOR' : _MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG,
        '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
        # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.Storage.WiredTiger.EngineConfig)
        })
      ,
      'DESCRIPTOR' : _MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER,
      '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
      # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.Storage.WiredTiger)
      })
    ,
    'DESCRIPTOR' : _MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE,
    '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.Storage)
    })
  ,

  'OperationProfiling' : _reflection.GeneratedProtocolMessageType('OperationProfiling', (_message.Message,), {
    'DESCRIPTOR' : _MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING,
    '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.OperationProfiling)
    })
  ,

  'Network' : _reflection.GeneratedProtocolMessageType('Network', (_message.Message,), {
    'DESCRIPTOR' : _MONGOCFGCONFIG5_0_ENTERPRISE_NETWORK,
    '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise.Network)
    })
  ,
  'DESCRIPTOR' : _MONGOCFGCONFIG5_0_ENTERPRISE,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfig5_0_enterprise)
  })
_sym_db.RegisterMessage(MongoCfgConfig5_0_enterprise)
_sym_db.RegisterMessage(MongoCfgConfig5_0_enterprise.Storage)
_sym_db.RegisterMessage(MongoCfgConfig5_0_enterprise.Storage.WiredTiger)
_sym_db.RegisterMessage(MongoCfgConfig5_0_enterprise.Storage.WiredTiger.EngineConfig)
_sym_db.RegisterMessage(MongoCfgConfig5_0_enterprise.OperationProfiling)
_sym_db.RegisterMessage(MongoCfgConfig5_0_enterprise.Network)

MongosConfig5_0_enterprise = _reflection.GeneratedProtocolMessageType('MongosConfig5_0_enterprise', (_message.Message,), {

  'Network' : _reflection.GeneratedProtocolMessageType('Network', (_message.Message,), {
    'DESCRIPTOR' : _MONGOSCONFIG5_0_ENTERPRISE_NETWORK,
    '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongosConfig5_0_enterprise.Network)
    })
  ,
  'DESCRIPTOR' : _MONGOSCONFIG5_0_ENTERPRISE,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongosConfig5_0_enterprise)
  })
_sym_db.RegisterMessage(MongosConfig5_0_enterprise)
_sym_db.RegisterMessage(MongosConfig5_0_enterprise.Network)

MongodConfigSet5_0_enterprise = _reflection.GeneratedProtocolMessageType('MongodConfigSet5_0_enterprise', (_message.Message,), {
  'DESCRIPTOR' : _MONGODCONFIGSET5_0_ENTERPRISE,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongodConfigSet5_0_enterprise)
  })
_sym_db.RegisterMessage(MongodConfigSet5_0_enterprise)

MongoCfgConfigSet5_0_enterprise = _reflection.GeneratedProtocolMessageType('MongoCfgConfigSet5_0_enterprise', (_message.Message,), {
  'DESCRIPTOR' : _MONGOCFGCONFIGSET5_0_ENTERPRISE,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongoCfgConfigSet5_0_enterprise)
  })
_sym_db.RegisterMessage(MongoCfgConfigSet5_0_enterprise)

MongosConfigSet5_0_enterprise = _reflection.GeneratedProtocolMessageType('MongosConfigSet5_0_enterprise', (_message.Message,), {
  'DESCRIPTOR' : _MONGOSCONFIGSET5_0_ENTERPRISE,
  '__module__' : 'yandex.cloud.mdb.mongodb.v1.config.mongodb5_0_enterprise_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.mongodb.v1.config.MongosConfigSet5_0_enterprise)
  })
_sym_db.RegisterMessage(MongosConfigSet5_0_enterprise)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&yandex.cloud.api.mdb.mongodb.v1.configZNgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/mongodb/v1/config;mongodb'
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_JOURNAL.fields_by_name['commit_interval']._options = None
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_JOURNAL.fields_by_name['commit_interval']._serialized_options = b'\372\3071\0051-500'
  _MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._options = None
  _MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._serialized_options = b'\372\3071\002>0'
  _MONGODCONFIG5_0_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._options = None
  _MONGODCONFIG5_0_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._options = None
  _MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING.fields_by_name['slow_op_threshold']._serialized_options = b'\372\3071\002>0'
  _MONGOCFGCONFIG5_0_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._options = None
  _MONGOCFGCONFIG5_0_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _MONGOSCONFIG5_0_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._options = None
  _MONGOSCONFIG5_0_ENTERPRISE_NETWORK.fields_by_name['max_incoming_connections']._serialized_options = b'\372\3071\01010-16384'
  _MONGODCONFIG5_0_ENTERPRISE._serialized_start=166
  _MONGODCONFIG5_0_ENTERPRISE._serialized_end=1670
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE._serialized_start=483
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE._serialized_end=1332
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER._serialized_start=696
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER._serialized_end=1256
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG._serialized_start=956
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG._serialized_end=1023
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG._serialized_start=1026
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG._serialized_end=1256
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG_COMPRESSOR._serialized_start=1184
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_COLLECTIONCONFIG_COMPRESSOR._serialized_end=1256
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_JOURNAL._serialized_start=1258
  _MONGODCONFIG5_0_ENTERPRISE_STORAGE_JOURNAL._serialized_end=1332
  _MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING._serialized_start=1335
  _MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING._serialized_end=1582
  _MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING_MODE._serialized_start=1523
  _MONGODCONFIG5_0_ENTERPRISE_OPERATIONPROFILING_MODE._serialized_end=1582
  _MONGODCONFIG5_0_ENTERPRISE_NETWORK._serialized_start=1584
  _MONGODCONFIG5_0_ENTERPRISE_NETWORK._serialized_end=1670
  _MONGOCFGCONFIG5_0_ENTERPRISE._serialized_start=1673
  _MONGOCFGCONFIG5_0_ENTERPRISE._serialized_end=2658
  _MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE._serialized_start=1998
  _MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE._serialized_end=2318
  _MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER._serialized_start=2116
  _MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER._serialized_end=2318
  _MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG._serialized_start=956
  _MONGOCFGCONFIG5_0_ENTERPRISE_STORAGE_WIREDTIGER_ENGINECONFIG._serialized_end=1023
  _MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING._serialized_start=2321
  _MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING._serialized_end=2570
  _MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING_MODE._serialized_start=1523
  _MONGOCFGCONFIG5_0_ENTERPRISE_OPERATIONPROFILING_MODE._serialized_end=1582
  _MONGOCFGCONFIG5_0_ENTERPRISE_NETWORK._serialized_start=1584
  _MONGOCFGCONFIG5_0_ENTERPRISE_NETWORK._serialized_end=1670
  _MONGOSCONFIG5_0_ENTERPRISE._serialized_start=2661
  _MONGOSCONFIG5_0_ENTERPRISE._serialized_end=2862
  _MONGOSCONFIG5_0_ENTERPRISE_NETWORK._serialized_start=1584
  _MONGOSCONFIG5_0_ENTERPRISE_NETWORK._serialized_end=1670
  _MONGODCONFIGSET5_0_ENTERPRISE._serialized_start=2865
  _MONGODCONFIGSET5_0_ENTERPRISE._serialized_end=3159
  _MONGOCFGCONFIGSET5_0_ENTERPRISE._serialized_start=3162
  _MONGOCFGCONFIGSET5_0_ENTERPRISE._serialized_end=3464
  _MONGOSCONFIGSET5_0_ENTERPRISE._serialized_start=3467
  _MONGOSCONFIGSET5_0_ENTERPRISE._serialized_end=3761
# @@protoc_insertion_point(module_scope)
