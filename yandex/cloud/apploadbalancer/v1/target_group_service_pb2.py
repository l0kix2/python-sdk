# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/apploadbalancer/v1/target_group_service.proto
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
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.apploadbalancer.v1 import target_group_pb2 as yandex_dot_cloud_dot_apploadbalancer_dot_v1_dot_target__group__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:yandex/cloud/apploadbalancer/v1/target_group_service.proto\x12\x1fyandex.cloud.apploadbalancer.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x32yandex/cloud/apploadbalancer/v1/target_group.proto\x1a\x1dyandex/cloud/validation.proto\"6\n\x15GetTargetGroupRequest\x12\x1d\n\x0ftarget_group_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x8c\x01\n\x17ListTargetGroupsRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"x\n\x18ListTargetGroupsResponse\x12\x43\n\rtarget_groups\x18\x01 \x03(\x0b\x32,.yandex.cloud.apploadbalancer.v1.TargetGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"9\n\x18\x44\x65leteTargetGroupRequest\x12\x1d\n\x0ftarget_group_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"4\n\x19\x44\x65leteTargetGroupMetadata\x12\x17\n\x0ftarget_group_id\x18\x01 \x01(\t\"\xca\x03\n\x18UpdateTargetGroupRequest\x12\x1d\n\x0ftarget_group_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x34\n\x04name\x18\x03 \x01(\tB&\xf2\xc7\x31\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x9e\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x45.yandex.cloud.apploadbalancer.v1.UpdateTargetGroupRequest.LabelsEntryBG\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x16\x12\x14[a-z][-_./\\@0-9a-z]*\x12\x38\n\x07targets\x18\x06 \x03(\x0b\x32\'.yandex.cloud.apploadbalancer.v1.Target\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"4\n\x19UpdateTargetGroupMetadata\x12\x17\n\x0ftarget_group_id\x18\x01 \x01(\t\"\x93\x03\n\x18\x43reateTargetGroupRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x34\n\x04name\x18\x02 \x01(\tB&\xf2\xc7\x31\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x9e\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x45.yandex.cloud.apploadbalancer.v1.CreateTargetGroupRequest.LabelsEntryBG\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x16\x12\x14[a-z][-_./\\@0-9a-z]*\x12\x38\n\x07targets\x18\x05 \x03(\x0b\x32\'.yandex.cloud.apploadbalancer.v1.Target\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"4\n\x19\x43reateTargetGroupMetadata\x12\x17\n\x0ftarget_group_id\x18\x01 \x01(\t\"t\n\x11\x41\x64\x64TargetsRequest\x12\x1d\n\x0ftarget_group_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12@\n\x07targets\x18\x02 \x03(\x0b\x32\'.yandex.cloud.apploadbalancer.v1.TargetB\x06\x82\xc8\x31\x02>0\"-\n\x12\x41\x64\x64TargetsMetadata\x12\x17\n\x0ftarget_group_id\x18\x01 \x01(\t\"w\n\x14RemoveTargetsRequest\x12\x1d\n\x0ftarget_group_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12@\n\x07targets\x18\x02 \x03(\x0b\x32\'.yandex.cloud.apploadbalancer.v1.TargetB\x06\x82\xc8\x31\x02>0\"0\n\x15RemoveTargetsMetadata\x12\x17\n\x0ftarget_group_id\x18\x01 \x01(\t\"\x87\x01\n ListTargetGroupOperationsRequest\x12%\n\x0ftarget_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"s\n!ListTargetGroupOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xee\x0c\n\x12TargetGroupService\x12\xa7\x01\n\x03Get\x12\x36.yandex.cloud.apploadbalancer.v1.GetTargetGroupRequest\x1a,.yandex.cloud.apploadbalancer.v1.TargetGroup\":\x82\xd3\xe4\x93\x02\x34\x12\x32/apploadbalancer/v1/targetGroups/{target_group_id}\x12\xa5\x01\n\x04List\x12\x38.yandex.cloud.apploadbalancer.v1.ListTargetGroupsRequest\x1a\x39.yandex.cloud.apploadbalancer.v1.ListTargetGroupsResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /apploadbalancer/v1/targetGroups\x12\xbf\x01\n\x06\x43reate\x12\x39.yandex.cloud.apploadbalancer.v1.CreateTargetGroupRequest\x1a!.yandex.cloud.operation.Operation\"W\x82\xd3\xe4\x93\x02%\" /apploadbalancer/v1/targetGroups:\x01*\xb2\xd2*(\n\x19\x43reateTargetGroupMetadata\x12\x0bTargetGroup\x12\xd1\x01\n\x06Update\x12\x39.yandex.cloud.apploadbalancer.v1.UpdateTargetGroupRequest\x1a!.yandex.cloud.operation.Operation\"i\x82\xd3\xe4\x93\x02\x37\x32\x32/apploadbalancer/v1/targetGroups/{target_group_id}:\x01*\xb2\xd2*(\n\x19UpdateTargetGroupMetadata\x12\x0bTargetGroup\x12\xd8\x01\n\x06\x44\x65lete\x12\x39.yandex.cloud.apploadbalancer.v1.DeleteTargetGroupRequest\x1a!.yandex.cloud.operation.Operation\"p\x82\xd3\xe4\x93\x02\x34*2/apploadbalancer/v1/targetGroups/{target_group_id}\xb2\xd2*2\n\x19\x44\x65leteTargetGroupMetadata\x12\x15google.protobuf.Empty\x12\xd2\x01\n\nAddTargets\x12\x32.yandex.cloud.apploadbalancer.v1.AddTargetsRequest\x1a!.yandex.cloud.operation.Operation\"m\x82\xd3\xe4\x93\x02\x42\"=/apploadbalancer/v1/targetGroups/{target_group_id}:addTargets:\x01*\xb2\xd2*!\n\x12\x41\x64\x64TargetsMetadata\x12\x0bTargetGroup\x12\xde\x01\n\rRemoveTargets\x12\x35.yandex.cloud.apploadbalancer.v1.RemoveTargetsRequest\x1a!.yandex.cloud.operation.Operation\"s\x82\xd3\xe4\x93\x02\x45\"@/apploadbalancer/v1/targetGroups/{target_group_id}:removeTargets:\x01*\xb2\xd2*$\n\x15RemoveTargetsMetadata\x12\x0bTargetGroup\x12\xde\x01\n\x0eListOperations\x12\x41.yandex.cloud.apploadbalancer.v1.ListTargetGroupOperationsRequest\x1a\x42.yandex.cloud.apploadbalancer.v1.ListTargetGroupOperationsResponse\"E\x82\xd3\xe4\x93\x02?\x12=/apploadbalancer/v1/targetGroups/{target_group_id}/operationsBz\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancerb\x06proto3')



_GETTARGETGROUPREQUEST = DESCRIPTOR.message_types_by_name['GetTargetGroupRequest']
_LISTTARGETGROUPSREQUEST = DESCRIPTOR.message_types_by_name['ListTargetGroupsRequest']
_LISTTARGETGROUPSRESPONSE = DESCRIPTOR.message_types_by_name['ListTargetGroupsResponse']
_DELETETARGETGROUPREQUEST = DESCRIPTOR.message_types_by_name['DeleteTargetGroupRequest']
_DELETETARGETGROUPMETADATA = DESCRIPTOR.message_types_by_name['DeleteTargetGroupMetadata']
_UPDATETARGETGROUPREQUEST = DESCRIPTOR.message_types_by_name['UpdateTargetGroupRequest']
_UPDATETARGETGROUPREQUEST_LABELSENTRY = _UPDATETARGETGROUPREQUEST.nested_types_by_name['LabelsEntry']
_UPDATETARGETGROUPMETADATA = DESCRIPTOR.message_types_by_name['UpdateTargetGroupMetadata']
_CREATETARGETGROUPREQUEST = DESCRIPTOR.message_types_by_name['CreateTargetGroupRequest']
_CREATETARGETGROUPREQUEST_LABELSENTRY = _CREATETARGETGROUPREQUEST.nested_types_by_name['LabelsEntry']
_CREATETARGETGROUPMETADATA = DESCRIPTOR.message_types_by_name['CreateTargetGroupMetadata']
_ADDTARGETSREQUEST = DESCRIPTOR.message_types_by_name['AddTargetsRequest']
_ADDTARGETSMETADATA = DESCRIPTOR.message_types_by_name['AddTargetsMetadata']
_REMOVETARGETSREQUEST = DESCRIPTOR.message_types_by_name['RemoveTargetsRequest']
_REMOVETARGETSMETADATA = DESCRIPTOR.message_types_by_name['RemoveTargetsMetadata']
_LISTTARGETGROUPOPERATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListTargetGroupOperationsRequest']
_LISTTARGETGROUPOPERATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListTargetGroupOperationsResponse']
GetTargetGroupRequest = _reflection.GeneratedProtocolMessageType('GetTargetGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTARGETGROUPREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.GetTargetGroupRequest)
  })
_sym_db.RegisterMessage(GetTargetGroupRequest)

ListTargetGroupsRequest = _reflection.GeneratedProtocolMessageType('ListTargetGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTARGETGROUPSREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.ListTargetGroupsRequest)
  })
_sym_db.RegisterMessage(ListTargetGroupsRequest)

ListTargetGroupsResponse = _reflection.GeneratedProtocolMessageType('ListTargetGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTARGETGROUPSRESPONSE,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.ListTargetGroupsResponse)
  })
_sym_db.RegisterMessage(ListTargetGroupsResponse)

DeleteTargetGroupRequest = _reflection.GeneratedProtocolMessageType('DeleteTargetGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETARGETGROUPREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.DeleteTargetGroupRequest)
  })
_sym_db.RegisterMessage(DeleteTargetGroupRequest)

DeleteTargetGroupMetadata = _reflection.GeneratedProtocolMessageType('DeleteTargetGroupMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETETARGETGROUPMETADATA,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.DeleteTargetGroupMetadata)
  })
_sym_db.RegisterMessage(DeleteTargetGroupMetadata)

UpdateTargetGroupRequest = _reflection.GeneratedProtocolMessageType('UpdateTargetGroupRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATETARGETGROUPREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.UpdateTargetGroupRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATETARGETGROUPREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.UpdateTargetGroupRequest)
  })
_sym_db.RegisterMessage(UpdateTargetGroupRequest)
_sym_db.RegisterMessage(UpdateTargetGroupRequest.LabelsEntry)

UpdateTargetGroupMetadata = _reflection.GeneratedProtocolMessageType('UpdateTargetGroupMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETARGETGROUPMETADATA,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.UpdateTargetGroupMetadata)
  })
_sym_db.RegisterMessage(UpdateTargetGroupMetadata)

CreateTargetGroupRequest = _reflection.GeneratedProtocolMessageType('CreateTargetGroupRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATETARGETGROUPREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.CreateTargetGroupRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CREATETARGETGROUPREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.CreateTargetGroupRequest)
  })
_sym_db.RegisterMessage(CreateTargetGroupRequest)
_sym_db.RegisterMessage(CreateTargetGroupRequest.LabelsEntry)

CreateTargetGroupMetadata = _reflection.GeneratedProtocolMessageType('CreateTargetGroupMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATETARGETGROUPMETADATA,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.CreateTargetGroupMetadata)
  })
_sym_db.RegisterMessage(CreateTargetGroupMetadata)

AddTargetsRequest = _reflection.GeneratedProtocolMessageType('AddTargetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDTARGETSREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.AddTargetsRequest)
  })
_sym_db.RegisterMessage(AddTargetsRequest)

AddTargetsMetadata = _reflection.GeneratedProtocolMessageType('AddTargetsMetadata', (_message.Message,), {
  'DESCRIPTOR' : _ADDTARGETSMETADATA,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.AddTargetsMetadata)
  })
_sym_db.RegisterMessage(AddTargetsMetadata)

RemoveTargetsRequest = _reflection.GeneratedProtocolMessageType('RemoveTargetsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVETARGETSREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.RemoveTargetsRequest)
  })
_sym_db.RegisterMessage(RemoveTargetsRequest)

RemoveTargetsMetadata = _reflection.GeneratedProtocolMessageType('RemoveTargetsMetadata', (_message.Message,), {
  'DESCRIPTOR' : _REMOVETARGETSMETADATA,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.RemoveTargetsMetadata)
  })
_sym_db.RegisterMessage(RemoveTargetsMetadata)

ListTargetGroupOperationsRequest = _reflection.GeneratedProtocolMessageType('ListTargetGroupOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTARGETGROUPOPERATIONSREQUEST,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.ListTargetGroupOperationsRequest)
  })
_sym_db.RegisterMessage(ListTargetGroupOperationsRequest)

ListTargetGroupOperationsResponse = _reflection.GeneratedProtocolMessageType('ListTargetGroupOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTARGETGROUPOPERATIONSRESPONSE,
  '__module__' : 'yandex.cloud.apploadbalancer.v1.target_group_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.apploadbalancer.v1.ListTargetGroupOperationsResponse)
  })
_sym_db.RegisterMessage(ListTargetGroupOperationsResponse)

_TARGETGROUPSERVICE = DESCRIPTOR.services_by_name['TargetGroupService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#yandex.cloud.api.apploadbalancer.v1ZSgithub.com/yandex-cloud/go-genproto/yandex/cloud/apploadbalancer/v1;apploadbalancer'
  _GETTARGETGROUPREQUEST.fields_by_name['target_group_id']._options = None
  _GETTARGETGROUPREQUEST.fields_by_name['target_group_id']._serialized_options = b'\350\3071\001'
  _LISTTARGETGROUPSREQUEST.fields_by_name['folder_id']._options = None
  _LISTTARGETGROUPSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _LISTTARGETGROUPSREQUEST.fields_by_name['page_size']._options = None
  _LISTTARGETGROUPSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTTARGETGROUPSREQUEST.fields_by_name['page_token']._options = None
  _LISTTARGETGROUPSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTTARGETGROUPSREQUEST.fields_by_name['filter']._options = None
  _LISTTARGETGROUPSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _DELETETARGETGROUPREQUEST.fields_by_name['target_group_id']._options = None
  _DELETETARGETGROUPREQUEST.fields_by_name['target_group_id']._serialized_options = b'\350\3071\001'
  _UPDATETARGETGROUPREQUEST_LABELSENTRY._options = None
  _UPDATETARGETGROUPREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATETARGETGROUPREQUEST.fields_by_name['target_group_id']._options = None
  _UPDATETARGETGROUPREQUEST.fields_by_name['target_group_id']._serialized_options = b'\350\3071\001'
  _UPDATETARGETGROUPREQUEST.fields_by_name['name']._options = None
  _UPDATETARGETGROUPREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?'
  _UPDATETARGETGROUPREQUEST.fields_by_name['description']._options = None
  _UPDATETARGETGROUPREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATETARGETGROUPREQUEST.fields_by_name['labels']._options = None
  _UPDATETARGETGROUPREQUEST.fields_by_name['labels']._serialized_options = b'\202\3101\004<=64\212\3101\004<=63\362\3071\017[-_./\\@0-9a-z]*\262\3101\006\032\0041-63\262\3101\026\022\024[a-z][-_./\\@0-9a-z]*'
  _CREATETARGETGROUPREQUEST_LABELSENTRY._options = None
  _CREATETARGETGROUPREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATETARGETGROUPREQUEST.fields_by_name['folder_id']._options = None
  _CREATETARGETGROUPREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATETARGETGROUPREQUEST.fields_by_name['name']._options = None
  _CREATETARGETGROUPREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\"([a-z]([-a-z0-9]{0,61}[a-z0-9])?)?'
  _CREATETARGETGROUPREQUEST.fields_by_name['description']._options = None
  _CREATETARGETGROUPREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATETARGETGROUPREQUEST.fields_by_name['labels']._options = None
  _CREATETARGETGROUPREQUEST.fields_by_name['labels']._serialized_options = b'\202\3101\004<=64\212\3101\004<=63\362\3071\017[-_./\\@0-9a-z]*\262\3101\006\032\0041-63\262\3101\026\022\024[a-z][-_./\\@0-9a-z]*'
  _ADDTARGETSREQUEST.fields_by_name['target_group_id']._options = None
  _ADDTARGETSREQUEST.fields_by_name['target_group_id']._serialized_options = b'\350\3071\001'
  _ADDTARGETSREQUEST.fields_by_name['targets']._options = None
  _ADDTARGETSREQUEST.fields_by_name['targets']._serialized_options = b'\202\3101\002>0'
  _REMOVETARGETSREQUEST.fields_by_name['target_group_id']._options = None
  _REMOVETARGETSREQUEST.fields_by_name['target_group_id']._serialized_options = b'\350\3071\001'
  _REMOVETARGETSREQUEST.fields_by_name['targets']._options = None
  _REMOVETARGETSREQUEST.fields_by_name['targets']._serialized_options = b'\202\3101\002>0'
  _LISTTARGETGROUPOPERATIONSREQUEST.fields_by_name['target_group_id']._options = None
  _LISTTARGETGROUPOPERATIONSREQUEST.fields_by_name['target_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTTARGETGROUPOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTTARGETGROUPOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTTARGETGROUPOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTTARGETGROUPOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _TARGETGROUPSERVICE.methods_by_name['Get']._options = None
  _TARGETGROUPSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\0024\0222/apploadbalancer/v1/targetGroups/{target_group_id}'
  _TARGETGROUPSERVICE.methods_by_name['List']._options = None
  _TARGETGROUPSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\"\022 /apploadbalancer/v1/targetGroups'
  _TARGETGROUPSERVICE.methods_by_name['Create']._options = None
  _TARGETGROUPSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002%\" /apploadbalancer/v1/targetGroups:\001*\262\322*(\n\031CreateTargetGroupMetadata\022\013TargetGroup'
  _TARGETGROUPSERVICE.methods_by_name['Update']._options = None
  _TARGETGROUPSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002722/apploadbalancer/v1/targetGroups/{target_group_id}:\001*\262\322*(\n\031UpdateTargetGroupMetadata\022\013TargetGroup'
  _TARGETGROUPSERVICE.methods_by_name['Delete']._options = None
  _TARGETGROUPSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\0024*2/apploadbalancer/v1/targetGroups/{target_group_id}\262\322*2\n\031DeleteTargetGroupMetadata\022\025google.protobuf.Empty'
  _TARGETGROUPSERVICE.methods_by_name['AddTargets']._options = None
  _TARGETGROUPSERVICE.methods_by_name['AddTargets']._serialized_options = b'\202\323\344\223\002B\"=/apploadbalancer/v1/targetGroups/{target_group_id}:addTargets:\001*\262\322*!\n\022AddTargetsMetadata\022\013TargetGroup'
  _TARGETGROUPSERVICE.methods_by_name['RemoveTargets']._options = None
  _TARGETGROUPSERVICE.methods_by_name['RemoveTargets']._serialized_options = b'\202\323\344\223\002E\"@/apploadbalancer/v1/targetGroups/{target_group_id}:removeTargets:\001*\262\322*$\n\025RemoveTargetsMetadata\022\013TargetGroup'
  _TARGETGROUPSERVICE.methods_by_name['ListOperations']._options = None
  _TARGETGROUPSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002?\022=/apploadbalancer/v1/targetGroups/{target_group_id}/operations'
  _GETTARGETGROUPREQUEST._serialized_start=316
  _GETTARGETGROUPREQUEST._serialized_end=370
  _LISTTARGETGROUPSREQUEST._serialized_start=373
  _LISTTARGETGROUPSREQUEST._serialized_end=513
  _LISTTARGETGROUPSRESPONSE._serialized_start=515
  _LISTTARGETGROUPSRESPONSE._serialized_end=635
  _DELETETARGETGROUPREQUEST._serialized_start=637
  _DELETETARGETGROUPREQUEST._serialized_end=694
  _DELETETARGETGROUPMETADATA._serialized_start=696
  _DELETETARGETGROUPMETADATA._serialized_end=748
  _UPDATETARGETGROUPREQUEST._serialized_start=751
  _UPDATETARGETGROUPREQUEST._serialized_end=1209
  _UPDATETARGETGROUPREQUEST_LABELSENTRY._serialized_start=1164
  _UPDATETARGETGROUPREQUEST_LABELSENTRY._serialized_end=1209
  _UPDATETARGETGROUPMETADATA._serialized_start=1211
  _UPDATETARGETGROUPMETADATA._serialized_end=1263
  _CREATETARGETGROUPREQUEST._serialized_start=1266
  _CREATETARGETGROUPREQUEST._serialized_end=1669
  _CREATETARGETGROUPREQUEST_LABELSENTRY._serialized_start=1164
  _CREATETARGETGROUPREQUEST_LABELSENTRY._serialized_end=1209
  _CREATETARGETGROUPMETADATA._serialized_start=1671
  _CREATETARGETGROUPMETADATA._serialized_end=1723
  _ADDTARGETSREQUEST._serialized_start=1725
  _ADDTARGETSREQUEST._serialized_end=1841
  _ADDTARGETSMETADATA._serialized_start=1843
  _ADDTARGETSMETADATA._serialized_end=1888
  _REMOVETARGETSREQUEST._serialized_start=1890
  _REMOVETARGETSREQUEST._serialized_end=2009
  _REMOVETARGETSMETADATA._serialized_start=2011
  _REMOVETARGETSMETADATA._serialized_end=2059
  _LISTTARGETGROUPOPERATIONSREQUEST._serialized_start=2062
  _LISTTARGETGROUPOPERATIONSREQUEST._serialized_end=2197
  _LISTTARGETGROUPOPERATIONSRESPONSE._serialized_start=2199
  _LISTTARGETGROUPOPERATIONSRESPONSE._serialized_end=2314
  _TARGETGROUPSERVICE._serialized_start=2317
  _TARGETGROUPSERVICE._serialized_end=3963
# @@protoc_insertion_point(module_scope)
