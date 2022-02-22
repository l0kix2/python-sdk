# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/triggers/v1/trigger_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.serverless.triggers.v1 import trigger_pb2 as yandex_dot_cloud_dot_serverless_dot_triggers_dot_v1_dot_trigger__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9yandex/cloud/serverless/triggers/v1/trigger_service.proto\x12#yandex.cloud.serverless.triggers.v1\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a\x31yandex/cloud/serverless/triggers/v1/trigger.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"-\n\x11GetTriggerRequest\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"e\n\x13ListTriggersRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\"o\n\x14ListTriggersResponse\x12>\n\x08triggers\x18\x01 \x03(\x0b\x32,.yandex.cloud.serverless.triggers.v1.Trigger\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x8f\x03\n\x14\x43reateTriggerRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x96\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x45.yandex.cloud.serverless.triggers.v1.CreateTriggerRequest.LabelsEntryB?\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0b[-_0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x12\x12\x10[a-z][-_0-9a-z]*\x12\x45\n\x04rule\x18\x05 \x01(\x0b\x32\x31.yandex.cloud.serverless.triggers.v1.Trigger.RuleB\x04\xe8\xc7\x31\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x15\x43reateTriggerMetadata\x12\x12\n\ntrigger_id\x18\x01 \x01(\t\"\xfa\x02\n\x14UpdateTriggerRequest\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x96\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x45.yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest.LabelsEntryB?\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0b[-_0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x12\x12\x10[a-z][-_0-9a-z]*\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"1\n\x15UpdateTriggerMetadata\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"0\n\x14\x44\x65leteTriggerRequest\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"1\n\x15\x44\x65leteTriggerMetadata\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"/\n\x13PauseTriggerRequest\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"0\n\x14PauseTriggerMetadata\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"0\n\x14ResumeTriggerRequest\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"1\n\x15ResumeTriggerMetadata\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x92\x01\n\x1cListTriggerOperationsRequest\x12\x18\n\ntrigger_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"o\n\x1dListTriggerOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xcc\x0b\n\x0eTriggerService\x12\x97\x01\n\x03Get\x12\x36.yandex.cloud.serverless.triggers.v1.GetTriggerRequest\x1a,.yandex.cloud.serverless.triggers.v1.Trigger\"*\x82\xd3\xe4\x93\x02$\x12\"/triggers/v1/triggers/{trigger_id}\x12\x9a\x01\n\x04List\x12\x38.yandex.cloud.serverless.triggers.v1.ListTriggersRequest\x1a\x39.yandex.cloud.serverless.triggers.v1.ListTriggersResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/triggers/v1/triggers\x12\xac\x01\n\x06\x43reate\x12\x39.yandex.cloud.serverless.triggers.v1.CreateTriggerRequest\x1a!.yandex.cloud.operation.Operation\"D\x82\xd3\xe4\x93\x02\x1a\"\x15/triggers/v1/triggers:\x01*\xb2\xd2* \n\x15\x43reateTriggerMetadata\x12\x07Trigger\x12\xb9\x01\n\x06Update\x12\x39.yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest\x1a!.yandex.cloud.operation.Operation\"Q\x82\xd3\xe4\x93\x02\'2\"/triggers/v1/triggers/{trigger_id}:\x01*\xb2\xd2* \n\x15UpdateTriggerMetadata\x12\x07Trigger\x12\xc4\x01\n\x06\x44\x65lete\x12\x39.yandex.cloud.serverless.triggers.v1.DeleteTriggerRequest\x1a!.yandex.cloud.operation.Operation\"\\\x82\xd3\xe4\x93\x02$*\"/triggers/v1/triggers/{trigger_id}\xb2\xd2*.\n\x15\x44\x65leteTriggerMetadata\x12\x15google.protobuf.Empty\x12\xbc\x01\n\x05Pause\x12\x38.yandex.cloud.serverless.triggers.v1.PauseTriggerRequest\x1a!.yandex.cloud.operation.Operation\"V\x82\xd3\xe4\x93\x02-\"(/triggers/v1/triggers/{trigger_id}:pause:\x01*\xb2\xd2*\x1f\n\x14PauseTriggerMetadata\x12\x07Trigger\x12\xc0\x01\n\x06Resume\x12\x39.yandex.cloud.serverless.triggers.v1.ResumeTriggerRequest\x1a!.yandex.cloud.operation.Operation\"X\x82\xd3\xe4\x93\x02.\")/triggers/v1/triggers/{trigger_id}:resume:\x01*\xb2\xd2* \n\x15ResumeTriggerMetadata\x12\x07Trigger\x12\xce\x01\n\x0eListOperations\x12\x41.yandex.cloud.serverless.triggers.v1.ListTriggerOperationsRequest\x1a\x42.yandex.cloud.serverless.triggers.v1.ListTriggerOperationsResponse\"5\x82\xd3\xe4\x93\x02/\x12-/triggers/v1/triggers/{trigger_id}/operationsB{\n\'yandex.cloud.api.serverless.triggers.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/triggers/v1;triggersb\x06proto3')



_GETTRIGGERREQUEST = DESCRIPTOR.message_types_by_name['GetTriggerRequest']
_LISTTRIGGERSREQUEST = DESCRIPTOR.message_types_by_name['ListTriggersRequest']
_LISTTRIGGERSRESPONSE = DESCRIPTOR.message_types_by_name['ListTriggersResponse']
_CREATETRIGGERREQUEST = DESCRIPTOR.message_types_by_name['CreateTriggerRequest']
_CREATETRIGGERREQUEST_LABELSENTRY = _CREATETRIGGERREQUEST.nested_types_by_name['LabelsEntry']
_CREATETRIGGERMETADATA = DESCRIPTOR.message_types_by_name['CreateTriggerMetadata']
_UPDATETRIGGERREQUEST = DESCRIPTOR.message_types_by_name['UpdateTriggerRequest']
_UPDATETRIGGERREQUEST_LABELSENTRY = _UPDATETRIGGERREQUEST.nested_types_by_name['LabelsEntry']
_UPDATETRIGGERMETADATA = DESCRIPTOR.message_types_by_name['UpdateTriggerMetadata']
_DELETETRIGGERREQUEST = DESCRIPTOR.message_types_by_name['DeleteTriggerRequest']
_DELETETRIGGERMETADATA = DESCRIPTOR.message_types_by_name['DeleteTriggerMetadata']
_PAUSETRIGGERREQUEST = DESCRIPTOR.message_types_by_name['PauseTriggerRequest']
_PAUSETRIGGERMETADATA = DESCRIPTOR.message_types_by_name['PauseTriggerMetadata']
_RESUMETRIGGERREQUEST = DESCRIPTOR.message_types_by_name['ResumeTriggerRequest']
_RESUMETRIGGERMETADATA = DESCRIPTOR.message_types_by_name['ResumeTriggerMetadata']
_LISTTRIGGEROPERATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListTriggerOperationsRequest']
_LISTTRIGGEROPERATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListTriggerOperationsResponse']
GetTriggerRequest = _reflection.GeneratedProtocolMessageType('GetTriggerRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRIGGERREQUEST,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.GetTriggerRequest)
  })
_sym_db.RegisterMessage(GetTriggerRequest)

ListTriggersRequest = _reflection.GeneratedProtocolMessageType('ListTriggersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRIGGERSREQUEST,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.ListTriggersRequest)
  })
_sym_db.RegisterMessage(ListTriggersRequest)

ListTriggersResponse = _reflection.GeneratedProtocolMessageType('ListTriggersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRIGGERSRESPONSE,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.ListTriggersResponse)
  })
_sym_db.RegisterMessage(ListTriggersResponse)

CreateTriggerRequest = _reflection.GeneratedProtocolMessageType('CreateTriggerRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATETRIGGERREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.CreateTriggerRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CREATETRIGGERREQUEST,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.CreateTriggerRequest)
  })
_sym_db.RegisterMessage(CreateTriggerRequest)
_sym_db.RegisterMessage(CreateTriggerRequest.LabelsEntry)

CreateTriggerMetadata = _reflection.GeneratedProtocolMessageType('CreateTriggerMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATETRIGGERMETADATA,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.CreateTriggerMetadata)
  })
_sym_db.RegisterMessage(CreateTriggerMetadata)

UpdateTriggerRequest = _reflection.GeneratedProtocolMessageType('UpdateTriggerRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATETRIGGERREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATETRIGGERREQUEST,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.UpdateTriggerRequest)
  })
_sym_db.RegisterMessage(UpdateTriggerRequest)
_sym_db.RegisterMessage(UpdateTriggerRequest.LabelsEntry)

UpdateTriggerMetadata = _reflection.GeneratedProtocolMessageType('UpdateTriggerMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETRIGGERMETADATA,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.UpdateTriggerMetadata)
  })
_sym_db.RegisterMessage(UpdateTriggerMetadata)

DeleteTriggerRequest = _reflection.GeneratedProtocolMessageType('DeleteTriggerRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETRIGGERREQUEST,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.DeleteTriggerRequest)
  })
_sym_db.RegisterMessage(DeleteTriggerRequest)

DeleteTriggerMetadata = _reflection.GeneratedProtocolMessageType('DeleteTriggerMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETETRIGGERMETADATA,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.DeleteTriggerMetadata)
  })
_sym_db.RegisterMessage(DeleteTriggerMetadata)

PauseTriggerRequest = _reflection.GeneratedProtocolMessageType('PauseTriggerRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAUSETRIGGERREQUEST,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.PauseTriggerRequest)
  })
_sym_db.RegisterMessage(PauseTriggerRequest)

PauseTriggerMetadata = _reflection.GeneratedProtocolMessageType('PauseTriggerMetadata', (_message.Message,), {
  'DESCRIPTOR' : _PAUSETRIGGERMETADATA,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.PauseTriggerMetadata)
  })
_sym_db.RegisterMessage(PauseTriggerMetadata)

ResumeTriggerRequest = _reflection.GeneratedProtocolMessageType('ResumeTriggerRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESUMETRIGGERREQUEST,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.ResumeTriggerRequest)
  })
_sym_db.RegisterMessage(ResumeTriggerRequest)

ResumeTriggerMetadata = _reflection.GeneratedProtocolMessageType('ResumeTriggerMetadata', (_message.Message,), {
  'DESCRIPTOR' : _RESUMETRIGGERMETADATA,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.ResumeTriggerMetadata)
  })
_sym_db.RegisterMessage(ResumeTriggerMetadata)

ListTriggerOperationsRequest = _reflection.GeneratedProtocolMessageType('ListTriggerOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRIGGEROPERATIONSREQUEST,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.ListTriggerOperationsRequest)
  })
_sym_db.RegisterMessage(ListTriggerOperationsRequest)

ListTriggerOperationsResponse = _reflection.GeneratedProtocolMessageType('ListTriggerOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRIGGEROPERATIONSRESPONSE,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.ListTriggerOperationsResponse)
  })
_sym_db.RegisterMessage(ListTriggerOperationsResponse)

_TRIGGERSERVICE = DESCRIPTOR.services_by_name['TriggerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'yandex.cloud.api.serverless.triggers.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/triggers/v1;triggers'
  _GETTRIGGERREQUEST.fields_by_name['trigger_id']._options = None
  _GETTRIGGERREQUEST.fields_by_name['trigger_id']._serialized_options = b'\350\3071\001'
  _LISTTRIGGERSREQUEST.fields_by_name['folder_id']._options = None
  _LISTTRIGGERSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATETRIGGERREQUEST_LABELSENTRY._options = None
  _CREATETRIGGERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATETRIGGERREQUEST.fields_by_name['folder_id']._options = None
  _CREATETRIGGERREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATETRIGGERREQUEST.fields_by_name['name']._options = None
  _CREATETRIGGERREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _CREATETRIGGERREQUEST.fields_by_name['description']._options = None
  _CREATETRIGGERREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATETRIGGERREQUEST.fields_by_name['labels']._options = None
  _CREATETRIGGERREQUEST.fields_by_name['labels']._serialized_options = b'\202\3101\004<=64\212\3101\004<=63\362\3071\013[-_0-9a-z]*\262\3101\006\032\0041-63\262\3101\022\022\020[a-z][-_0-9a-z]*'
  _CREATETRIGGERREQUEST.fields_by_name['rule']._options = None
  _CREATETRIGGERREQUEST.fields_by_name['rule']._serialized_options = b'\350\3071\001'
  _UPDATETRIGGERREQUEST_LABELSENTRY._options = None
  _UPDATETRIGGERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATETRIGGERREQUEST.fields_by_name['trigger_id']._options = None
  _UPDATETRIGGERREQUEST.fields_by_name['trigger_id']._serialized_options = b'\350\3071\001'
  _UPDATETRIGGERREQUEST.fields_by_name['name']._options = None
  _UPDATETRIGGERREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _UPDATETRIGGERREQUEST.fields_by_name['description']._options = None
  _UPDATETRIGGERREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATETRIGGERREQUEST.fields_by_name['labels']._options = None
  _UPDATETRIGGERREQUEST.fields_by_name['labels']._serialized_options = b'\202\3101\004<=64\212\3101\004<=63\362\3071\013[-_0-9a-z]*\262\3101\006\032\0041-63\262\3101\022\022\020[a-z][-_0-9a-z]*'
  _UPDATETRIGGERMETADATA.fields_by_name['trigger_id']._options = None
  _UPDATETRIGGERMETADATA.fields_by_name['trigger_id']._serialized_options = b'\350\3071\001'
  _DELETETRIGGERREQUEST.fields_by_name['trigger_id']._options = None
  _DELETETRIGGERREQUEST.fields_by_name['trigger_id']._serialized_options = b'\350\3071\001'
  _DELETETRIGGERMETADATA.fields_by_name['trigger_id']._options = None
  _DELETETRIGGERMETADATA.fields_by_name['trigger_id']._serialized_options = b'\350\3071\001'
  _PAUSETRIGGERREQUEST.fields_by_name['trigger_id']._options = None
  _PAUSETRIGGERREQUEST.fields_by_name['trigger_id']._serialized_options = b'\350\3071\001'
  _PAUSETRIGGERMETADATA.fields_by_name['trigger_id']._options = None
  _PAUSETRIGGERMETADATA.fields_by_name['trigger_id']._serialized_options = b'\350\3071\001'
  _RESUMETRIGGERREQUEST.fields_by_name['trigger_id']._options = None
  _RESUMETRIGGERREQUEST.fields_by_name['trigger_id']._serialized_options = b'\350\3071\001'
  _RESUMETRIGGERMETADATA.fields_by_name['trigger_id']._options = None
  _RESUMETRIGGERMETADATA.fields_by_name['trigger_id']._serialized_options = b'\350\3071\001'
  _LISTTRIGGEROPERATIONSREQUEST.fields_by_name['trigger_id']._options = None
  _LISTTRIGGEROPERATIONSREQUEST.fields_by_name['trigger_id']._serialized_options = b'\350\3071\001'
  _LISTTRIGGEROPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTTRIGGEROPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTTRIGGEROPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTTRIGGEROPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTTRIGGEROPERATIONSREQUEST.fields_by_name['filter']._options = None
  _LISTTRIGGEROPERATIONSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _TRIGGERSERVICE.methods_by_name['Get']._options = None
  _TRIGGERSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002$\022\"/triggers/v1/triggers/{trigger_id}'
  _TRIGGERSERVICE.methods_by_name['List']._options = None
  _TRIGGERSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\027\022\025/triggers/v1/triggers'
  _TRIGGERSERVICE.methods_by_name['Create']._options = None
  _TRIGGERSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\032\"\025/triggers/v1/triggers:\001*\262\322* \n\025CreateTriggerMetadata\022\007Trigger'
  _TRIGGERSERVICE.methods_by_name['Update']._options = None
  _TRIGGERSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002\'2\"/triggers/v1/triggers/{trigger_id}:\001*\262\322* \n\025UpdateTriggerMetadata\022\007Trigger'
  _TRIGGERSERVICE.methods_by_name['Delete']._options = None
  _TRIGGERSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002$*\"/triggers/v1/triggers/{trigger_id}\262\322*.\n\025DeleteTriggerMetadata\022\025google.protobuf.Empty'
  _TRIGGERSERVICE.methods_by_name['Pause']._options = None
  _TRIGGERSERVICE.methods_by_name['Pause']._serialized_options = b'\202\323\344\223\002-\"(/triggers/v1/triggers/{trigger_id}:pause:\001*\262\322*\037\n\024PauseTriggerMetadata\022\007Trigger'
  _TRIGGERSERVICE.methods_by_name['Resume']._options = None
  _TRIGGERSERVICE.methods_by_name['Resume']._serialized_options = b'\202\323\344\223\002.\")/triggers/v1/triggers/{trigger_id}:resume:\001*\262\322* \n\025ResumeTriggerMetadata\022\007Trigger'
  _TRIGGERSERVICE.methods_by_name['ListOperations']._options = None
  _TRIGGERSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002/\022-/triggers/v1/triggers/{trigger_id}/operations'
  _GETTRIGGERREQUEST._serialized_start=318
  _GETTRIGGERREQUEST._serialized_end=363
  _LISTTRIGGERSREQUEST._serialized_start=365
  _LISTTRIGGERSREQUEST._serialized_end=466
  _LISTTRIGGERSRESPONSE._serialized_start=468
  _LISTTRIGGERSRESPONSE._serialized_end=579
  _CREATETRIGGERREQUEST._serialized_start=582
  _CREATETRIGGERREQUEST._serialized_end=981
  _CREATETRIGGERREQUEST_LABELSENTRY._serialized_start=936
  _CREATETRIGGERREQUEST_LABELSENTRY._serialized_end=981
  _CREATETRIGGERMETADATA._serialized_start=983
  _CREATETRIGGERMETADATA._serialized_end=1026
  _UPDATETRIGGERREQUEST._serialized_start=1029
  _UPDATETRIGGERREQUEST._serialized_end=1407
  _UPDATETRIGGERREQUEST_LABELSENTRY._serialized_start=936
  _UPDATETRIGGERREQUEST_LABELSENTRY._serialized_end=981
  _UPDATETRIGGERMETADATA._serialized_start=1409
  _UPDATETRIGGERMETADATA._serialized_end=1458
  _DELETETRIGGERREQUEST._serialized_start=1460
  _DELETETRIGGERREQUEST._serialized_end=1508
  _DELETETRIGGERMETADATA._serialized_start=1510
  _DELETETRIGGERMETADATA._serialized_end=1559
  _PAUSETRIGGERREQUEST._serialized_start=1561
  _PAUSETRIGGERREQUEST._serialized_end=1608
  _PAUSETRIGGERMETADATA._serialized_start=1610
  _PAUSETRIGGERMETADATA._serialized_end=1658
  _RESUMETRIGGERREQUEST._serialized_start=1660
  _RESUMETRIGGERREQUEST._serialized_end=1708
  _RESUMETRIGGERMETADATA._serialized_start=1710
  _RESUMETRIGGERMETADATA._serialized_end=1759
  _LISTTRIGGEROPERATIONSREQUEST._serialized_start=1762
  _LISTTRIGGEROPERATIONSREQUEST._serialized_end=1908
  _LISTTRIGGEROPERATIONSRESPONSE._serialized_start=1910
  _LISTTRIGGEROPERATIONSRESPONSE._serialized_end=2021
  _TRIGGERSERVICE._serialized_start=2024
  _TRIGGERSERVICE._serialized_end=3508
# @@protoc_insertion_point(module_scope)
