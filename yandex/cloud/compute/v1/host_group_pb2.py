# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/host_group.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(yandex/cloud/compute/v1/host_group.proto\x12\x17yandex.cloud.compute.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa4\x04\n\tHostGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x06labels\x18\x06 \x03(\x0b\x32..yandex.cloud.compute.v1.HostGroup.LabelsEntry\x12\x0f\n\x07zone_id\x18\x07 \x01(\t\x12\x39\n\x06status\x18\x08 \x01(\x0e\x32).yandex.cloud.compute.v1.HostGroup.Status\x12\x0f\n\x07type_id\x18\t \x01(\t\x12\x46\n\x12maintenance_policy\x18\n \x01(\x0e\x32*.yandex.cloud.compute.v1.MaintenancePolicy\x12:\n\x0cscale_policy\x18\x0b \x01(\x0b\x32$.yandex.cloud.compute.v1.ScalePolicy\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"U\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08\x44\x45LETING\x10\x04\"\x8f\x01\n\x04Host\x12\n\n\x02id\x18\x01 \x01(\t\x12\x34\n\x06status\x18\x02 \x01(\x0e\x32$.yandex.cloud.compute.v1.Host.Status\x12\x11\n\tserver_id\x18\x03 \x01(\t\"2\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x06\n\x02UP\x10\x01\x12\x08\n\x04\x44OWN\x10\x02\"\x7f\n\x0bScalePolicy\x12\x46\n\x0b\x66ixed_scale\x18\x01 \x01(\x0b\x32/.yandex.cloud.compute.v1.ScalePolicy.FixedScaleH\x00\x1a\x1a\n\nFixedScale\x12\x0c\n\x04size\x18\x01 \x01(\x03\x42\x0c\n\nscale_type*Q\n\x11MaintenancePolicy\x12\"\n\x1eMAINTENANCE_POLICY_UNSPECIFIED\x10\x00\x12\x0b\n\x07RESTART\x10\x01\x12\x0b\n\x07MIGRATE\x10\x02\x42\x62\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')

_MAINTENANCEPOLICY = DESCRIPTOR.enum_types_by_name['MaintenancePolicy']
MaintenancePolicy = enum_type_wrapper.EnumTypeWrapper(_MAINTENANCEPOLICY)
MAINTENANCE_POLICY_UNSPECIFIED = 0
RESTART = 1
MIGRATE = 2


_HOSTGROUP = DESCRIPTOR.message_types_by_name['HostGroup']
_HOSTGROUP_LABELSENTRY = _HOSTGROUP.nested_types_by_name['LabelsEntry']
_HOST = DESCRIPTOR.message_types_by_name['Host']
_SCALEPOLICY = DESCRIPTOR.message_types_by_name['ScalePolicy']
_SCALEPOLICY_FIXEDSCALE = _SCALEPOLICY.nested_types_by_name['FixedScale']
_HOSTGROUP_STATUS = _HOSTGROUP.enum_types_by_name['Status']
_HOST_STATUS = _HOST.enum_types_by_name['Status']
HostGroup = _reflection.GeneratedProtocolMessageType('HostGroup', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _HOSTGROUP_LABELSENTRY,
    '__module__' : 'yandex.cloud.compute.v1.host_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.HostGroup.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _HOSTGROUP,
  '__module__' : 'yandex.cloud.compute.v1.host_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.HostGroup)
  })
_sym_db.RegisterMessage(HostGroup)
_sym_db.RegisterMessage(HostGroup.LabelsEntry)

Host = _reflection.GeneratedProtocolMessageType('Host', (_message.Message,), {
  'DESCRIPTOR' : _HOST,
  '__module__' : 'yandex.cloud.compute.v1.host_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.Host)
  })
_sym_db.RegisterMessage(Host)

ScalePolicy = _reflection.GeneratedProtocolMessageType('ScalePolicy', (_message.Message,), {

  'FixedScale' : _reflection.GeneratedProtocolMessageType('FixedScale', (_message.Message,), {
    'DESCRIPTOR' : _SCALEPOLICY_FIXEDSCALE,
    '__module__' : 'yandex.cloud.compute.v1.host_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.ScalePolicy.FixedScale)
    })
  ,
  'DESCRIPTOR' : _SCALEPOLICY,
  '__module__' : 'yandex.cloud.compute.v1.host_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.compute.v1.ScalePolicy)
  })
_sym_db.RegisterMessage(ScalePolicy)
_sym_db.RegisterMessage(ScalePolicy.FixedScale)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'
  _HOSTGROUP_LABELSENTRY._options = None
  _HOSTGROUP_LABELSENTRY._serialized_options = b'8\001'
  _MAINTENANCEPOLICY._serialized_start=928
  _MAINTENANCEPOLICY._serialized_end=1009
  _HOSTGROUP._serialized_start=103
  _HOSTGROUP._serialized_end=651
  _HOSTGROUP_LABELSENTRY._serialized_start=519
  _HOSTGROUP_LABELSENTRY._serialized_end=564
  _HOSTGROUP_STATUS._serialized_start=566
  _HOSTGROUP_STATUS._serialized_end=651
  _HOST._serialized_start=654
  _HOST._serialized_end=797
  _HOST_STATUS._serialized_start=747
  _HOST_STATUS._serialized_end=797
  _SCALEPOLICY._serialized_start=799
  _SCALEPOLICY._serialized_end=926
  _SCALEPOLICY_FIXEDSCALE._serialized_start=886
  _SCALEPOLICY_FIXEDSCALE._serialized_end=912
# @@protoc_insertion_point(module_scope)
