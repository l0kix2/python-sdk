# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/triggers/v1/trigger.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.logging.v1 import log_entry_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__entry__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1yandex/cloud/serverless/triggers/v1/trigger.proto\x12#yandex.cloud.serverless.triggers.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\'yandex/cloud/logging/v1/log_entry.proto\x1a\x1dyandex/cloud/validation.proto\"\xe7!\n\x07Trigger\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1f\n\tfolder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x04name\x18\x04 \x01(\tB\x08\x8a\xc8\x31\x04\x33-63\x12\x1e\n\x0b\x64\x65scription\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05\x30-256\x12H\n\x06labels\x18\x06 \x03(\x0b\x32\x38.yandex.cloud.serverless.triggers.v1.Trigger.LabelsEntry\x12\x45\n\x04rule\x18\x08 \x01(\x0b\x32\x31.yandex.cloud.serverless.triggers.v1.Trigger.RuleB\x04\xe8\xc7\x31\x01\x12\x43\n\x06status\x18\t \x01(\x0e\x32\x33.yandex.cloud.serverless.triggers.v1.Trigger.Status\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xde\x05\n\x04Rule\x12\x43\n\x05timer\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.Trigger.TimerH\x00\x12R\n\rmessage_queue\x18\x03 \x01(\x0b\x32\x39.yandex.cloud.serverless.triggers.v1.Trigger.MessageQueueH\x00\x12N\n\x0biot_message\x18\x04 \x01(\x0b\x32\x37.yandex.cloud.serverless.triggers.v1.Trigger.IoTMessageH\x00\x12T\n\x0eobject_storage\x18\x05 \x01(\x0b\x32:.yandex.cloud.serverless.triggers.v1.Trigger.ObjectStorageH\x00\x12\\\n\x12\x63ontainer_registry\x18\x06 \x01(\x0b\x32>.yandex.cloud.serverless.triggers.v1.Trigger.ContainerRegistryH\x00\x12L\n\ncloud_logs\x18\t \x01(\x0b\x32\x36.yandex.cloud.serverless.triggers.v1.Trigger.CloudLogsH\x00\x12G\n\x07logging\x18\n \x01(\x0b\x32\x34.yandex.cloud.serverless.triggers.v1.Trigger.LoggingH\x00\x12L\n\x0e\x62illing_budget\x18\x0b \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.BillingBudgetH\x00\x12\x46\n\x0b\x64\x61ta_stream\x18\x0c \x01(\x0b\x32/.yandex.cloud.serverless.triggers.v1.DataStreamH\x00\x42\x0c\n\x04rule\x12\x04\xc0\xc1\x31\x01\x1a\xdd\x02\n\x05Timer\x12&\n\x0f\x63ron_expression\x18\x01 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05<=100\x12R\n\x0finvoke_function\x18\x65 \x01(\x0b\x32\x37.yandex.cloud.serverless.triggers.v1.InvokeFunctionOnceH\x00\x12\x62\n\x1ainvoke_function_with_retry\x18g \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12\x64\n\x1binvoke_container_with_retry\x18h \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\x9e\x03\n\x0cMessageQueue\x12\x16\n\x08queue_id\x18\x0b \x01(\tB\x04\xe8\xc7\x31\x01\x12(\n\x12service_account_id\x18\x03 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12P\n\x0e\x62\x61tch_settings\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.BatchSettingsB\x04\xe8\xc7\x31\x01\x12@\n\x12visibility_timeout\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05<=12h\x12R\n\x0finvoke_function\x18\x65 \x01(\x0b\x32\x37.yandex.cloud.serverless.triggers.v1.InvokeFunctionOnceH\x00\x12T\n\x10invoke_container\x18\x66 \x01(\x0b\x32\x38.yandex.cloud.serverless.triggers.v1.InvokeContainerOnceH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\x92\x02\n\nIoTMessage\x12\x19\n\x0bregistry_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x12\n\nmqtt_topic\x18\x03 \x01(\t\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18\x66 \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\xe7\x02\n\rObjectStorage\x12_\n\nevent_type\x18\x03 \x03(\x0e\x32\x43.yandex.cloud.serverless.triggers.v1.Trigger.ObjectStorageEventTypeB\x06\x82\xc8\x31\x02>0\x12\x11\n\tbucket_id\x18\x04 \x01(\t\x12\x0e\n\x06prefix\x18\x06 \x01(\t\x12\x0e\n\x06suffix\x18\x07 \x01(\t\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18\x66 \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\xf2\x02\n\x11\x43ontainerRegistry\x12\x63\n\nevent_type\x18\x03 \x03(\x0e\x32G.yandex.cloud.serverless.triggers.v1.Trigger.ContainerRegistryEventTypeB\x06\x82\xc8\x31\x02>0\x12\x13\n\x0bregistry_id\x18\x04 \x01(\t\x12\x12\n\nimage_name\x18\x05 \x01(\t\x12\x0b\n\x03tag\x18\x06 \x01(\t\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18\x66 \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\xc0\x02\n\tCloudLogs\x12\x14\n\x0clog_group_id\x18\x01 \x03(\t\x12Y\n\x0e\x62\x61tch_settings\x18\x02 \x01(\x0b\x32;.yandex.cloud.serverless.triggers.v1.CloudLogsBatchSettingsB\x04\xe8\xc7\x31\x01\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18\x66 \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\x8b\x04\n\x07Logging\x12\x1e\n\x0clog_group_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12@\n\rresource_type\x18\x03 \x03(\tB)\xf2\xc7\x31\x1c[a-zA-Z][-a-zA-Z0-9_.]{1,62}\x82\xc8\x31\x05<=100\x12>\n\x0bresource_id\x18\x04 \x03(\tB)\xf2\xc7\x31\x1c[a-zA-Z][-a-zA-Z0-9_.]{1,62}\x82\xc8\x31\x05<=100\x12\x41\n\x06levels\x18\x05 \x03(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.LevelB\x08\x82\xc8\x31\x04<=10\x12W\n\x0e\x62\x61tch_settings\x18\x06 \x01(\x0b\x32\x39.yandex.cloud.serverless.triggers.v1.LoggingBatchSettingsB\x04\xe8\xc7\x31\x01\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18g \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\"\xca\x01\n\x16ObjectStorageEventType\x12)\n%OBJECT_STORAGE_EVENT_TYPE_UNSPECIFIED\x10\x00\x12+\n\'OBJECT_STORAGE_EVENT_TYPE_CREATE_OBJECT\x10\x01\x12+\n\'OBJECT_STORAGE_EVENT_TYPE_UPDATE_OBJECT\x10\x02\x12+\n\'OBJECT_STORAGE_EVENT_TYPE_DELETE_OBJECT\x10\x03\"\x93\x02\n\x1a\x43ontainerRegistryEventType\x12-\n)CONTAINER_REGISTRY_EVENT_TYPE_UNSPECIFIED\x10\x00\x12.\n*CONTAINER_REGISTRY_EVENT_TYPE_CREATE_IMAGE\x10\x01\x12.\n*CONTAINER_REGISTRY_EVENT_TYPE_DELETE_IMAGE\x10\x02\x12\x32\n.CONTAINER_REGISTRY_EVENT_TYPE_CREATE_IMAGE_TAG\x10\x03\x12\x32\n.CONTAINER_REGISTRY_EVENT_TYPE_DELETE_IMAGE_TAG\x10\x04\"8\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\n\n\x06PAUSED\x10\x02\"i\n\x12InvokeFunctionOnce\x12!\n\x0b\x66unction_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x14\n\x0c\x66unction_tag\x18\x02 \x01(\t\x12\x1a\n\x12service_account_id\x18\x03 \x01(\t\"\x8b\x02\n\x17InvokeFunctionWithRetry\x12!\n\x0b\x66unction_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x14\n\x0c\x66unction_tag\x18\x02 \x01(\t\x12\x1a\n\x12service_account_id\x18\x03 \x01(\t\x12J\n\x0eretry_settings\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.RetrySettings\x12O\n\x11\x64\x65\x61\x64_letter_queue\x18\x05 \x01(\x0b\x32\x34.yandex.cloud.serverless.triggers.v1.PutQueueMessage\"c\n\x13InvokeContainerOnce\x12\"\n\x0c\x63ontainer_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x1a\n\x12service_account_id\x18\x04 \x01(\t\"\x85\x02\n\x18InvokeContainerWithRetry\x12\"\n\x0c\x63ontainer_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x1a\n\x12service_account_id\x18\x04 \x01(\t\x12J\n\x0eretry_settings\x18\x05 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.RetrySettings\x12O\n\x11\x64\x65\x61\x64_letter_queue\x18\x06 \x01(\x0b\x32\x34.yandex.cloud.serverless.triggers.v1.PutQueueMessage\"M\n\x0fPutQueueMessage\x12\x10\n\x08queue_id\x18\x0b \x01(\t\x12(\n\x12service_account_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"X\n\rBatchSettings\x12\x16\n\x04size\x18\x01 \x01(\x03\x42\x08\xfa\xc7\x31\x04\x30-10\x12/\n\x06\x63utoff\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\xe8\xc7\x31\x01\"g\n\x16\x43loudLogsBatchSettings\x12\x17\n\x04size\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x34\n\x06\x63utoff\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05\x31s-1m\"e\n\x14LoggingBatchSettings\x12\x17\n\x04size\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x31-100\x12\x34\n\x06\x63utoff\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05\x31s-1m\"c\n\rRetrySettings\x12\x1f\n\x0eretry_attempts\x18\x01 \x01(\x03\x42\x07\xfa\xc7\x31\x03\x31-5\x12\x31\n\x08interval\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\xe8\xc7\x31\x01\"\x9a\x02\n\rBillingBudget\x12(\n\x12\x62illing_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1b\n\tbudget_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18g \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\"j\n\x17\x44\x61taStreamBatchSettings\x12\x19\n\x04size\x18\x01 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x31-65536\x12\x34\n\x06\x63utoff\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05\x31s-1m\"\xf6\x02\n\nDataStream\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0e\n\x06stream\x18\x03 \x01(\t\x12\x1a\n\x12service_account_id\x18\x04 \x01(\t\x12T\n\x0e\x62\x61tch_settings\x18\x05 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.DataStreamBatchSettings\x12W\n\x0finvoke_function\x18\r \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18\x0f \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01*\xc0\x01\n\x0bTriggerType\x12\x1c\n\x18TRIGGER_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TIMER\x10\x02\x12\x11\n\rMESSAGE_QUEUE\x10\x03\x12\x0f\n\x0bIOT_MESSAGE\x10\x04\x12\x12\n\x0eOBJECT_STORAGE\x10\x05\x12\x16\n\x12\x43ONTAINER_REGISTRY\x10\x06\x12\x0e\n\nCLOUD_LOGS\x10\x07\x12\x0b\n\x07LOGGING\x10\x08\x12\x12\n\x0e\x42ILLING_BUDGET\x10\t\x12\x07\n\x03YDS\x10\nB{\n\'yandex.cloud.api.serverless.triggers.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/triggers/v1;triggersb\x06proto3')

_TRIGGERTYPE = DESCRIPTOR.enum_types_by_name['TriggerType']
TriggerType = enum_type_wrapper.EnumTypeWrapper(_TRIGGERTYPE)
TRIGGER_TYPE_UNSPECIFIED = 0
TIMER = 2
MESSAGE_QUEUE = 3
IOT_MESSAGE = 4
OBJECT_STORAGE = 5
CONTAINER_REGISTRY = 6
CLOUD_LOGS = 7
LOGGING = 8
BILLING_BUDGET = 9
YDS = 10


_TRIGGER = DESCRIPTOR.message_types_by_name['Trigger']
_TRIGGER_LABELSENTRY = _TRIGGER.nested_types_by_name['LabelsEntry']
_TRIGGER_RULE = _TRIGGER.nested_types_by_name['Rule']
_TRIGGER_TIMER = _TRIGGER.nested_types_by_name['Timer']
_TRIGGER_MESSAGEQUEUE = _TRIGGER.nested_types_by_name['MessageQueue']
_TRIGGER_IOTMESSAGE = _TRIGGER.nested_types_by_name['IoTMessage']
_TRIGGER_OBJECTSTORAGE = _TRIGGER.nested_types_by_name['ObjectStorage']
_TRIGGER_CONTAINERREGISTRY = _TRIGGER.nested_types_by_name['ContainerRegistry']
_TRIGGER_CLOUDLOGS = _TRIGGER.nested_types_by_name['CloudLogs']
_TRIGGER_LOGGING = _TRIGGER.nested_types_by_name['Logging']
_INVOKEFUNCTIONONCE = DESCRIPTOR.message_types_by_name['InvokeFunctionOnce']
_INVOKEFUNCTIONWITHRETRY = DESCRIPTOR.message_types_by_name['InvokeFunctionWithRetry']
_INVOKECONTAINERONCE = DESCRIPTOR.message_types_by_name['InvokeContainerOnce']
_INVOKECONTAINERWITHRETRY = DESCRIPTOR.message_types_by_name['InvokeContainerWithRetry']
_PUTQUEUEMESSAGE = DESCRIPTOR.message_types_by_name['PutQueueMessage']
_BATCHSETTINGS = DESCRIPTOR.message_types_by_name['BatchSettings']
_CLOUDLOGSBATCHSETTINGS = DESCRIPTOR.message_types_by_name['CloudLogsBatchSettings']
_LOGGINGBATCHSETTINGS = DESCRIPTOR.message_types_by_name['LoggingBatchSettings']
_RETRYSETTINGS = DESCRIPTOR.message_types_by_name['RetrySettings']
_BILLINGBUDGET = DESCRIPTOR.message_types_by_name['BillingBudget']
_DATASTREAMBATCHSETTINGS = DESCRIPTOR.message_types_by_name['DataStreamBatchSettings']
_DATASTREAM = DESCRIPTOR.message_types_by_name['DataStream']
_TRIGGER_OBJECTSTORAGEEVENTTYPE = _TRIGGER.enum_types_by_name['ObjectStorageEventType']
_TRIGGER_CONTAINERREGISTRYEVENTTYPE = _TRIGGER.enum_types_by_name['ContainerRegistryEventType']
_TRIGGER_STATUS = _TRIGGER.enum_types_by_name['Status']
Trigger = _reflection.GeneratedProtocolMessageType('Trigger', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRIGGER_LABELSENTRY,
    '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.LabelsEntry)
    })
  ,

  'Rule' : _reflection.GeneratedProtocolMessageType('Rule', (_message.Message,), {
    'DESCRIPTOR' : _TRIGGER_RULE,
    '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.Rule)
    })
  ,

  'Timer' : _reflection.GeneratedProtocolMessageType('Timer', (_message.Message,), {
    'DESCRIPTOR' : _TRIGGER_TIMER,
    '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.Timer)
    })
  ,

  'MessageQueue' : _reflection.GeneratedProtocolMessageType('MessageQueue', (_message.Message,), {
    'DESCRIPTOR' : _TRIGGER_MESSAGEQUEUE,
    '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.MessageQueue)
    })
  ,

  'IoTMessage' : _reflection.GeneratedProtocolMessageType('IoTMessage', (_message.Message,), {
    'DESCRIPTOR' : _TRIGGER_IOTMESSAGE,
    '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.IoTMessage)
    })
  ,

  'ObjectStorage' : _reflection.GeneratedProtocolMessageType('ObjectStorage', (_message.Message,), {
    'DESCRIPTOR' : _TRIGGER_OBJECTSTORAGE,
    '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.ObjectStorage)
    })
  ,

  'ContainerRegistry' : _reflection.GeneratedProtocolMessageType('ContainerRegistry', (_message.Message,), {
    'DESCRIPTOR' : _TRIGGER_CONTAINERREGISTRY,
    '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.ContainerRegistry)
    })
  ,

  'CloudLogs' : _reflection.GeneratedProtocolMessageType('CloudLogs', (_message.Message,), {
    'DESCRIPTOR' : _TRIGGER_CLOUDLOGS,
    '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.CloudLogs)
    })
  ,

  'Logging' : _reflection.GeneratedProtocolMessageType('Logging', (_message.Message,), {
    'DESCRIPTOR' : _TRIGGER_LOGGING,
    '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger.Logging)
    })
  ,
  'DESCRIPTOR' : _TRIGGER,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.Trigger)
  })
_sym_db.RegisterMessage(Trigger)
_sym_db.RegisterMessage(Trigger.LabelsEntry)
_sym_db.RegisterMessage(Trigger.Rule)
_sym_db.RegisterMessage(Trigger.Timer)
_sym_db.RegisterMessage(Trigger.MessageQueue)
_sym_db.RegisterMessage(Trigger.IoTMessage)
_sym_db.RegisterMessage(Trigger.ObjectStorage)
_sym_db.RegisterMessage(Trigger.ContainerRegistry)
_sym_db.RegisterMessage(Trigger.CloudLogs)
_sym_db.RegisterMessage(Trigger.Logging)

InvokeFunctionOnce = _reflection.GeneratedProtocolMessageType('InvokeFunctionOnce', (_message.Message,), {
  'DESCRIPTOR' : _INVOKEFUNCTIONONCE,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.InvokeFunctionOnce)
  })
_sym_db.RegisterMessage(InvokeFunctionOnce)

InvokeFunctionWithRetry = _reflection.GeneratedProtocolMessageType('InvokeFunctionWithRetry', (_message.Message,), {
  'DESCRIPTOR' : _INVOKEFUNCTIONWITHRETRY,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetry)
  })
_sym_db.RegisterMessage(InvokeFunctionWithRetry)

InvokeContainerOnce = _reflection.GeneratedProtocolMessageType('InvokeContainerOnce', (_message.Message,), {
  'DESCRIPTOR' : _INVOKECONTAINERONCE,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.InvokeContainerOnce)
  })
_sym_db.RegisterMessage(InvokeContainerOnce)

InvokeContainerWithRetry = _reflection.GeneratedProtocolMessageType('InvokeContainerWithRetry', (_message.Message,), {
  'DESCRIPTOR' : _INVOKECONTAINERWITHRETRY,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetry)
  })
_sym_db.RegisterMessage(InvokeContainerWithRetry)

PutQueueMessage = _reflection.GeneratedProtocolMessageType('PutQueueMessage', (_message.Message,), {
  'DESCRIPTOR' : _PUTQUEUEMESSAGE,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.PutQueueMessage)
  })
_sym_db.RegisterMessage(PutQueueMessage)

BatchSettings = _reflection.GeneratedProtocolMessageType('BatchSettings', (_message.Message,), {
  'DESCRIPTOR' : _BATCHSETTINGS,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.BatchSettings)
  })
_sym_db.RegisterMessage(BatchSettings)

CloudLogsBatchSettings = _reflection.GeneratedProtocolMessageType('CloudLogsBatchSettings', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDLOGSBATCHSETTINGS,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.CloudLogsBatchSettings)
  })
_sym_db.RegisterMessage(CloudLogsBatchSettings)

LoggingBatchSettings = _reflection.GeneratedProtocolMessageType('LoggingBatchSettings', (_message.Message,), {
  'DESCRIPTOR' : _LOGGINGBATCHSETTINGS,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.LoggingBatchSettings)
  })
_sym_db.RegisterMessage(LoggingBatchSettings)

RetrySettings = _reflection.GeneratedProtocolMessageType('RetrySettings', (_message.Message,), {
  'DESCRIPTOR' : _RETRYSETTINGS,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.RetrySettings)
  })
_sym_db.RegisterMessage(RetrySettings)

BillingBudget = _reflection.GeneratedProtocolMessageType('BillingBudget', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGBUDGET,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.BillingBudget)
  })
_sym_db.RegisterMessage(BillingBudget)

DataStreamBatchSettings = _reflection.GeneratedProtocolMessageType('DataStreamBatchSettings', (_message.Message,), {
  'DESCRIPTOR' : _DATASTREAMBATCHSETTINGS,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.DataStreamBatchSettings)
  })
_sym_db.RegisterMessage(DataStreamBatchSettings)

DataStream = _reflection.GeneratedProtocolMessageType('DataStream', (_message.Message,), {
  'DESCRIPTOR' : _DATASTREAM,
  '__module__' : 'yandex.cloud.serverless.triggers.v1.trigger_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.serverless.triggers.v1.DataStream)
  })
_sym_db.RegisterMessage(DataStream)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'yandex.cloud.api.serverless.triggers.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/triggers/v1;triggers'
  _TRIGGER_LABELSENTRY._options = None
  _TRIGGER_LABELSENTRY._serialized_options = b'8\001'
  _TRIGGER_RULE.oneofs_by_name['rule']._options = None
  _TRIGGER_RULE.oneofs_by_name['rule']._serialized_options = b'\300\3011\001'
  _TRIGGER_TIMER.oneofs_by_name['action']._options = None
  _TRIGGER_TIMER.oneofs_by_name['action']._serialized_options = b'\300\3011\001'
  _TRIGGER_TIMER.fields_by_name['cron_expression']._options = None
  _TRIGGER_TIMER.fields_by_name['cron_expression']._serialized_options = b'\350\3071\001\212\3101\005<=100'
  _TRIGGER_MESSAGEQUEUE.oneofs_by_name['action']._options = None
  _TRIGGER_MESSAGEQUEUE.oneofs_by_name['action']._serialized_options = b'\300\3011\001'
  _TRIGGER_MESSAGEQUEUE.fields_by_name['queue_id']._options = None
  _TRIGGER_MESSAGEQUEUE.fields_by_name['queue_id']._serialized_options = b'\350\3071\001'
  _TRIGGER_MESSAGEQUEUE.fields_by_name['service_account_id']._options = None
  _TRIGGER_MESSAGEQUEUE.fields_by_name['service_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _TRIGGER_MESSAGEQUEUE.fields_by_name['batch_settings']._options = None
  _TRIGGER_MESSAGEQUEUE.fields_by_name['batch_settings']._serialized_options = b'\350\3071\001'
  _TRIGGER_MESSAGEQUEUE.fields_by_name['visibility_timeout']._options = None
  _TRIGGER_MESSAGEQUEUE.fields_by_name['visibility_timeout']._serialized_options = b'\372\3071\005<=12h'
  _TRIGGER_IOTMESSAGE.oneofs_by_name['action']._options = None
  _TRIGGER_IOTMESSAGE.oneofs_by_name['action']._serialized_options = b'\300\3011\001'
  _TRIGGER_IOTMESSAGE.fields_by_name['registry_id']._options = None
  _TRIGGER_IOTMESSAGE.fields_by_name['registry_id']._serialized_options = b'\350\3071\001'
  _TRIGGER_OBJECTSTORAGE.oneofs_by_name['action']._options = None
  _TRIGGER_OBJECTSTORAGE.oneofs_by_name['action']._serialized_options = b'\300\3011\001'
  _TRIGGER_OBJECTSTORAGE.fields_by_name['event_type']._options = None
  _TRIGGER_OBJECTSTORAGE.fields_by_name['event_type']._serialized_options = b'\202\3101\002>0'
  _TRIGGER_CONTAINERREGISTRY.oneofs_by_name['action']._options = None
  _TRIGGER_CONTAINERREGISTRY.oneofs_by_name['action']._serialized_options = b'\300\3011\001'
  _TRIGGER_CONTAINERREGISTRY.fields_by_name['event_type']._options = None
  _TRIGGER_CONTAINERREGISTRY.fields_by_name['event_type']._serialized_options = b'\202\3101\002>0'
  _TRIGGER_CLOUDLOGS.oneofs_by_name['action']._options = None
  _TRIGGER_CLOUDLOGS.oneofs_by_name['action']._serialized_options = b'\300\3011\001'
  _TRIGGER_CLOUDLOGS.fields_by_name['batch_settings']._options = None
  _TRIGGER_CLOUDLOGS.fields_by_name['batch_settings']._serialized_options = b'\350\3071\001'
  _TRIGGER_LOGGING.oneofs_by_name['action']._options = None
  _TRIGGER_LOGGING.oneofs_by_name['action']._serialized_options = b'\300\3011\001'
  _TRIGGER_LOGGING.fields_by_name['log_group_id']._options = None
  _TRIGGER_LOGGING.fields_by_name['log_group_id']._serialized_options = b'\212\3101\004<=50'
  _TRIGGER_LOGGING.fields_by_name['resource_type']._options = None
  _TRIGGER_LOGGING.fields_by_name['resource_type']._serialized_options = b'\362\3071\034[a-zA-Z][-a-zA-Z0-9_.]{1,62}\202\3101\005<=100'
  _TRIGGER_LOGGING.fields_by_name['resource_id']._options = None
  _TRIGGER_LOGGING.fields_by_name['resource_id']._serialized_options = b'\362\3071\034[a-zA-Z][-a-zA-Z0-9_.]{1,62}\202\3101\005<=100'
  _TRIGGER_LOGGING.fields_by_name['levels']._options = None
  _TRIGGER_LOGGING.fields_by_name['levels']._serialized_options = b'\202\3101\004<=10'
  _TRIGGER_LOGGING.fields_by_name['batch_settings']._options = None
  _TRIGGER_LOGGING.fields_by_name['batch_settings']._serialized_options = b'\350\3071\001'
  _TRIGGER.fields_by_name['folder_id']._options = None
  _TRIGGER.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _TRIGGER.fields_by_name['name']._options = None
  _TRIGGER.fields_by_name['name']._serialized_options = b'\212\3101\0043-63'
  _TRIGGER.fields_by_name['description']._options = None
  _TRIGGER.fields_by_name['description']._serialized_options = b'\212\3101\0050-256'
  _TRIGGER.fields_by_name['rule']._options = None
  _TRIGGER.fields_by_name['rule']._serialized_options = b'\350\3071\001'
  _INVOKEFUNCTIONONCE.fields_by_name['function_id']._options = None
  _INVOKEFUNCTIONONCE.fields_by_name['function_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _INVOKEFUNCTIONWITHRETRY.fields_by_name['function_id']._options = None
  _INVOKEFUNCTIONWITHRETRY.fields_by_name['function_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _INVOKECONTAINERONCE.fields_by_name['container_id']._options = None
  _INVOKECONTAINERONCE.fields_by_name['container_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _INVOKECONTAINERWITHRETRY.fields_by_name['container_id']._options = None
  _INVOKECONTAINERWITHRETRY.fields_by_name['container_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _PUTQUEUEMESSAGE.fields_by_name['service_account_id']._options = None
  _PUTQUEUEMESSAGE.fields_by_name['service_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _BATCHSETTINGS.fields_by_name['size']._options = None
  _BATCHSETTINGS.fields_by_name['size']._serialized_options = b'\372\3071\0040-10'
  _BATCHSETTINGS.fields_by_name['cutoff']._options = None
  _BATCHSETTINGS.fields_by_name['cutoff']._serialized_options = b'\350\3071\001'
  _CLOUDLOGSBATCHSETTINGS.fields_by_name['size']._options = None
  _CLOUDLOGSBATCHSETTINGS.fields_by_name['size']._serialized_options = b'\372\3071\0050-100'
  _CLOUDLOGSBATCHSETTINGS.fields_by_name['cutoff']._options = None
  _CLOUDLOGSBATCHSETTINGS.fields_by_name['cutoff']._serialized_options = b'\372\3071\0051s-1m'
  _LOGGINGBATCHSETTINGS.fields_by_name['size']._options = None
  _LOGGINGBATCHSETTINGS.fields_by_name['size']._serialized_options = b'\372\3071\0051-100'
  _LOGGINGBATCHSETTINGS.fields_by_name['cutoff']._options = None
  _LOGGINGBATCHSETTINGS.fields_by_name['cutoff']._serialized_options = b'\372\3071\0051s-1m'
  _RETRYSETTINGS.fields_by_name['retry_attempts']._options = None
  _RETRYSETTINGS.fields_by_name['retry_attempts']._serialized_options = b'\372\3071\0031-5'
  _RETRYSETTINGS.fields_by_name['interval']._options = None
  _RETRYSETTINGS.fields_by_name['interval']._serialized_options = b'\350\3071\001'
  _BILLINGBUDGET.oneofs_by_name['action']._options = None
  _BILLINGBUDGET.oneofs_by_name['action']._serialized_options = b'\300\3011\001'
  _BILLINGBUDGET.fields_by_name['billing_account_id']._options = None
  _BILLINGBUDGET.fields_by_name['billing_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _BILLINGBUDGET.fields_by_name['budget_id']._options = None
  _BILLINGBUDGET.fields_by_name['budget_id']._serialized_options = b'\212\3101\004<=50'
  _DATASTREAMBATCHSETTINGS.fields_by_name['size']._options = None
  _DATASTREAMBATCHSETTINGS.fields_by_name['size']._serialized_options = b'\372\3071\0071-65536'
  _DATASTREAMBATCHSETTINGS.fields_by_name['cutoff']._options = None
  _DATASTREAMBATCHSETTINGS.fields_by_name['cutoff']._serialized_options = b'\372\3071\0051s-1m'
  _DATASTREAM.oneofs_by_name['action']._options = None
  _DATASTREAM.oneofs_by_name['action']._serialized_options = b'\300\3011\001'
  _TRIGGERTYPE._serialized_start=6548
  _TRIGGERTYPE._serialized_end=6740
  _TRIGGER._serialized_start=228
  _TRIGGER._serialized_end=4555
  _TRIGGER_LABELSENTRY._serialized_start=602
  _TRIGGER_LABELSENTRY._serialized_end=647
  _TRIGGER_RULE._serialized_start=650
  _TRIGGER_RULE._serialized_end=1384
  _TRIGGER_TIMER._serialized_start=1387
  _TRIGGER_TIMER._serialized_end=1736
  _TRIGGER_MESSAGEQUEUE._serialized_start=1739
  _TRIGGER_MESSAGEQUEUE._serialized_end=2153
  _TRIGGER_IOTMESSAGE._serialized_start=2156
  _TRIGGER_IOTMESSAGE._serialized_end=2430
  _TRIGGER_OBJECTSTORAGE._serialized_start=2433
  _TRIGGER_OBJECTSTORAGE._serialized_end=2792
  _TRIGGER_CONTAINERREGISTRY._serialized_start=2795
  _TRIGGER_CONTAINERREGISTRY._serialized_end=3165
  _TRIGGER_CLOUDLOGS._serialized_start=3168
  _TRIGGER_CLOUDLOGS._serialized_end=3488
  _TRIGGER_LOGGING._serialized_start=3491
  _TRIGGER_LOGGING._serialized_end=4014
  _TRIGGER_OBJECTSTORAGEEVENTTYPE._serialized_start=4017
  _TRIGGER_OBJECTSTORAGEEVENTTYPE._serialized_end=4219
  _TRIGGER_CONTAINERREGISTRYEVENTTYPE._serialized_start=4222
  _TRIGGER_CONTAINERREGISTRYEVENTTYPE._serialized_end=4497
  _TRIGGER_STATUS._serialized_start=4499
  _TRIGGER_STATUS._serialized_end=4555
  _INVOKEFUNCTIONONCE._serialized_start=4557
  _INVOKEFUNCTIONONCE._serialized_end=4662
  _INVOKEFUNCTIONWITHRETRY._serialized_start=4665
  _INVOKEFUNCTIONWITHRETRY._serialized_end=4932
  _INVOKECONTAINERONCE._serialized_start=4934
  _INVOKECONTAINERONCE._serialized_end=5033
  _INVOKECONTAINERWITHRETRY._serialized_start=5036
  _INVOKECONTAINERWITHRETRY._serialized_end=5297
  _PUTQUEUEMESSAGE._serialized_start=5299
  _PUTQUEUEMESSAGE._serialized_end=5376
  _BATCHSETTINGS._serialized_start=5378
  _BATCHSETTINGS._serialized_end=5466
  _CLOUDLOGSBATCHSETTINGS._serialized_start=5468
  _CLOUDLOGSBATCHSETTINGS._serialized_end=5571
  _LOGGINGBATCHSETTINGS._serialized_start=5573
  _LOGGINGBATCHSETTINGS._serialized_end=5674
  _RETRYSETTINGS._serialized_start=5676
  _RETRYSETTINGS._serialized_end=5775
  _BILLINGBUDGET._serialized_start=5778
  _BILLINGBUDGET._serialized_end=6060
  _DATASTREAMBATCHSETTINGS._serialized_start=6062
  _DATASTREAMBATCHSETTINGS._serialized_end=6168
  _DATASTREAM._serialized_start=6171
  _DATASTREAM._serialized_end=6545
# @@protoc_insertion_point(module_scope)
