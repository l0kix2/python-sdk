# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/vpc/v1/security_group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(yandex/cloud/vpc/v1/security_group.proto\x12\x13yandex.cloud.vpc.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\xeb\x03\n\rSecurityGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12>\n\x06labels\x18\x06 \x03(\x0b\x32..yandex.cloud.vpc.v1.SecurityGroup.LabelsEntry\x12\x12\n\nnetwork_id\x18\x07 \x01(\t\x12\x39\n\x06status\x18\x08 \x01(\x0e\x32).yandex.cloud.vpc.v1.SecurityGroup.Status\x12\x35\n\x05rules\x18\t \x03(\x0b\x32&.yandex.cloud.vpc.v1.SecurityGroupRule\x12\x1b\n\x13\x64\x65\x66\x61ult_for_network\x18\n \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"V\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08\x44\x45LETING\x10\x04\"\x94\x04\n\x11SecurityGroupRule\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x42\n\x06labels\x18\x03 \x03(\x0b\x32\x32.yandex.cloud.vpc.v1.SecurityGroupRule.LabelsEntry\x12I\n\tdirection\x18\x04 \x01(\x0e\x32\x30.yandex.cloud.vpc.v1.SecurityGroupRule.DirectionB\x04\xe8\xc7\x31\x01\x12-\n\x05ports\x18\x05 \x01(\x0b\x32\x1e.yandex.cloud.vpc.v1.PortRange\x12\x15\n\rprotocol_name\x18\x06 \x01(\t\x12\x17\n\x0fprotocol_number\x18\x07 \x01(\x03\x12\x36\n\x0b\x63idr_blocks\x18\x08 \x01(\x0b\x32\x1f.yandex.cloud.vpc.v1.CidrBlocksH\x00\x12\x1b\n\x11security_group_id\x18\t \x01(\tH\x00\x12\x1b\n\x11predefined_target\x18\n \x01(\tH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"?\n\tDirection\x12\x19\n\x15\x44IRECTION_UNSPECIFIED\x10\x00\x12\x0b\n\x07INGRESS\x10\x01\x12\n\n\x06\x45GRESS\x10\x02\x42\x0e\n\x06target\x12\x04\xc0\xc1\x31\x01\"I\n\tPortRange\x12\x1e\n\tfrom_port\x18\x01 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-65535\x12\x1c\n\x07to_port\x18\x02 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x30-65535\"<\n\nCidrBlocks\x12\x16\n\x0ev4_cidr_blocks\x18\x01 \x03(\t\x12\x16\n\x0ev6_cidr_blocks\x18\x02 \x03(\tBV\n\x17yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpcb\x06proto3')



_SECURITYGROUP = DESCRIPTOR.message_types_by_name['SecurityGroup']
_SECURITYGROUP_LABELSENTRY = _SECURITYGROUP.nested_types_by_name['LabelsEntry']
_SECURITYGROUPRULE = DESCRIPTOR.message_types_by_name['SecurityGroupRule']
_SECURITYGROUPRULE_LABELSENTRY = _SECURITYGROUPRULE.nested_types_by_name['LabelsEntry']
_PORTRANGE = DESCRIPTOR.message_types_by_name['PortRange']
_CIDRBLOCKS = DESCRIPTOR.message_types_by_name['CidrBlocks']
_SECURITYGROUP_STATUS = _SECURITYGROUP.enum_types_by_name['Status']
_SECURITYGROUPRULE_DIRECTION = _SECURITYGROUPRULE.enum_types_by_name['Direction']
SecurityGroup = _reflection.GeneratedProtocolMessageType('SecurityGroup', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SECURITYGROUP_LABELSENTRY,
    '__module__' : 'yandex.cloud.vpc.v1.security_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.SecurityGroup.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _SECURITYGROUP,
  '__module__' : 'yandex.cloud.vpc.v1.security_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.SecurityGroup)
  })
_sym_db.RegisterMessage(SecurityGroup)
_sym_db.RegisterMessage(SecurityGroup.LabelsEntry)

SecurityGroupRule = _reflection.GeneratedProtocolMessageType('SecurityGroupRule', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SECURITYGROUPRULE_LABELSENTRY,
    '__module__' : 'yandex.cloud.vpc.v1.security_group_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.SecurityGroupRule.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _SECURITYGROUPRULE,
  '__module__' : 'yandex.cloud.vpc.v1.security_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.SecurityGroupRule)
  })
_sym_db.RegisterMessage(SecurityGroupRule)
_sym_db.RegisterMessage(SecurityGroupRule.LabelsEntry)

PortRange = _reflection.GeneratedProtocolMessageType('PortRange', (_message.Message,), {
  'DESCRIPTOR' : _PORTRANGE,
  '__module__' : 'yandex.cloud.vpc.v1.security_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.PortRange)
  })
_sym_db.RegisterMessage(PortRange)

CidrBlocks = _reflection.GeneratedProtocolMessageType('CidrBlocks', (_message.Message,), {
  'DESCRIPTOR' : _CIDRBLOCKS,
  '__module__' : 'yandex.cloud.vpc.v1.security_group_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.CidrBlocks)
  })
_sym_db.RegisterMessage(CidrBlocks)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpc'
  _SECURITYGROUP_LABELSENTRY._options = None
  _SECURITYGROUP_LABELSENTRY._serialized_options = b'8\001'
  _SECURITYGROUPRULE_LABELSENTRY._options = None
  _SECURITYGROUPRULE_LABELSENTRY._serialized_options = b'8\001'
  _SECURITYGROUPRULE.oneofs_by_name['target']._options = None
  _SECURITYGROUPRULE.oneofs_by_name['target']._serialized_options = b'\300\3011\001'
  _SECURITYGROUPRULE.fields_by_name['direction']._options = None
  _SECURITYGROUPRULE.fields_by_name['direction']._serialized_options = b'\350\3071\001'
  _PORTRANGE.fields_by_name['from_port']._options = None
  _PORTRANGE.fields_by_name['from_port']._serialized_options = b'\372\3071\0070-65535'
  _PORTRANGE.fields_by_name['to_port']._options = None
  _PORTRANGE.fields_by_name['to_port']._serialized_options = b'\372\3071\0070-65535'
  _SECURITYGROUP._serialized_start=130
  _SECURITYGROUP._serialized_end=621
  _SECURITYGROUP_LABELSENTRY._serialized_start=488
  _SECURITYGROUP_LABELSENTRY._serialized_end=533
  _SECURITYGROUP_STATUS._serialized_start=535
  _SECURITYGROUP_STATUS._serialized_end=621
  _SECURITYGROUPRULE._serialized_start=624
  _SECURITYGROUPRULE._serialized_end=1156
  _SECURITYGROUPRULE_LABELSENTRY._serialized_start=488
  _SECURITYGROUPRULE_LABELSENTRY._serialized_end=533
  _SECURITYGROUPRULE_DIRECTION._serialized_start=1077
  _SECURITYGROUPRULE_DIRECTION._serialized_end=1140
  _PORTRANGE._serialized_start=1158
  _PORTRANGE._serialized_end=1231
  _CIDRBLOCKS._serialized_start=1233
  _CIDRBLOCKS._serialized_end=1293
# @@protoc_insertion_point(module_scope)
