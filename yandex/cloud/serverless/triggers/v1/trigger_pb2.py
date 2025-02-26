# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/serverless/triggers/v1/trigger.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.logging.v1 import log_entry_pb2 as yandex_dot_cloud_dot_logging_dot_v1_dot_log__entry__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1yandex/cloud/serverless/triggers/v1/trigger.proto\x12#yandex.cloud.serverless.triggers.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\'yandex/cloud/logging/v1/log_entry.proto\x1a\x1dyandex/cloud/validation.proto\"\x93(\n\x07Trigger\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1f\n\tfolder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x04name\x18\x04 \x01(\tB\x08\x8a\xc8\x31\x04\x33-63\x12\x1e\n\x0b\x64\x65scription\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05\x30-256\x12H\n\x06labels\x18\x06 \x03(\x0b\x32\x38.yandex.cloud.serverless.triggers.v1.Trigger.LabelsEntry\x12\x45\n\x04rule\x18\x08 \x01(\x0b\x32\x31.yandex.cloud.serverless.triggers.v1.Trigger.RuleB\x04\xe8\xc7\x31\x01\x12\x43\n\x06status\x18\t \x01(\x0e\x32\x33.yandex.cloud.serverless.triggers.v1.Trigger.Status\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\xf6\x06\n\x04Rule\x12\x43\n\x05timer\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.Trigger.TimerH\x00\x12R\n\rmessage_queue\x18\x03 \x01(\x0b\x32\x39.yandex.cloud.serverless.triggers.v1.Trigger.MessageQueueH\x00\x12N\n\x0biot_message\x18\x04 \x01(\x0b\x32\x37.yandex.cloud.serverless.triggers.v1.Trigger.IoTMessageH\x00\x12[\n\x12iot_broker_message\x18\x0e \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.Trigger.IoTBrokerMessageH\x00\x12T\n\x0eobject_storage\x18\x05 \x01(\x0b\x32:.yandex.cloud.serverless.triggers.v1.Trigger.ObjectStorageH\x00\x12\\\n\x12\x63ontainer_registry\x18\x06 \x01(\x0b\x32>.yandex.cloud.serverless.triggers.v1.Trigger.ContainerRegistryH\x00\x12L\n\ncloud_logs\x18\t \x01(\x0b\x32\x36.yandex.cloud.serverless.triggers.v1.Trigger.CloudLogsH\x00\x12G\n\x07logging\x18\n \x01(\x0b\x32\x34.yandex.cloud.serverless.triggers.v1.Trigger.LoggingH\x00\x12L\n\x0e\x62illing_budget\x18\x0b \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.BillingBudgetH\x00\x12\x46\n\x0b\x64\x61ta_stream\x18\x0c \x01(\x0b\x32/.yandex.cloud.serverless.triggers.v1.DataStreamH\x00\x12\x39\n\x04mail\x18\r \x01(\x0b\x32).yandex.cloud.serverless.triggers.v1.MailH\x00\x42\x0c\n\x04rule\x12\x04\xc0\xc1\x31\x01\x1a\xfa\x02\n\x05Timer\x12&\n\x0f\x63ron_expression\x18\x01 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05<=100\x12\x1b\n\x07payload\x18\x02 \x01(\tB\n\x8a\xc8\x31\x06<=4096\x12R\n\x0finvoke_function\x18\x65 \x01(\x0b\x32\x37.yandex.cloud.serverless.triggers.v1.InvokeFunctionOnceH\x00\x12\x62\n\x1ainvoke_function_with_retry\x18g \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12\x64\n\x1binvoke_container_with_retry\x18h \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\x9e\x03\n\x0cMessageQueue\x12\x16\n\x08queue_id\x18\x0b \x01(\tB\x04\xe8\xc7\x31\x01\x12(\n\x12service_account_id\x18\x03 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12P\n\x0e\x62\x61tch_settings\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.BatchSettingsB\x04\xe8\xc7\x31\x01\x12@\n\x12visibility_timeout\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05<=12h\x12R\n\x0finvoke_function\x18\x65 \x01(\x0b\x32\x37.yandex.cloud.serverless.triggers.v1.InvokeFunctionOnceH\x00\x12T\n\x10invoke_container\x18\x66 \x01(\x0b\x32\x38.yandex.cloud.serverless.triggers.v1.InvokeContainerOnceH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\xde\x02\n\nIoTMessage\x12\x19\n\x0bregistry_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x12\n\nmqtt_topic\x18\x03 \x01(\t\x12J\n\x0e\x62\x61tch_settings\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.BatchSettings\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18\x66 \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\xcf\x02\n\x10IoTBrokerMessage\x12\x17\n\tbroker_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x12\n\nmqtt_topic\x18\x02 \x01(\t\x12J\n\x0e\x62\x61tch_settings\x18\x03 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.BatchSettings\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18\x66 \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\xb3\x03\n\rObjectStorage\x12_\n\nevent_type\x18\x03 \x03(\x0e\x32\x43.yandex.cloud.serverless.triggers.v1.Trigger.ObjectStorageEventTypeB\x06\x82\xc8\x31\x02>0\x12\x11\n\tbucket_id\x18\x04 \x01(\t\x12\x0e\n\x06prefix\x18\x06 \x01(\t\x12\x0e\n\x06suffix\x18\x07 \x01(\t\x12J\n\x0e\x62\x61tch_settings\x18\x08 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.BatchSettings\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18\x66 \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\xbe\x03\n\x11\x43ontainerRegistry\x12\x63\n\nevent_type\x18\x03 \x03(\x0e\x32G.yandex.cloud.serverless.triggers.v1.Trigger.ContainerRegistryEventTypeB\x06\x82\xc8\x31\x02>0\x12\x13\n\x0bregistry_id\x18\x04 \x01(\t\x12\x12\n\nimage_name\x18\x05 \x01(\t\x12\x0b\n\x03tag\x18\x06 \x01(\t\x12J\n\x0e\x62\x61tch_settings\x18\x07 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.BatchSettings\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18\x66 \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\xc0\x02\n\tCloudLogs\x12\x14\n\x0clog_group_id\x18\x01 \x03(\t\x12Y\n\x0e\x62\x61tch_settings\x18\x02 \x01(\x0b\x32;.yandex.cloud.serverless.triggers.v1.CloudLogsBatchSettingsB\x04\xe8\xc7\x31\x01\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18\x66 \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\x1a\xcc\x04\n\x07Logging\x12\x1e\n\x0clog_group_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12@\n\rresource_type\x18\x03 \x03(\tB)\xf2\xc7\x31\x1c[a-zA-Z][-a-zA-Z0-9_.]{1,62}\x82\xc8\x31\x05<=100\x12>\n\x0bresource_id\x18\x04 \x03(\tB)\xf2\xc7\x31\x1c[a-zA-Z][-a-zA-Z0-9_.]{1,62}\x82\xc8\x31\x05<=100\x12?\n\x0bstream_name\x18\x07 \x03(\tB*\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x82\xc8\x31\x05<=100\x12\x41\n\x06levels\x18\x05 \x03(\x0e\x32\'.yandex.cloud.logging.v1.LogLevel.LevelB\x08\x82\xc8\x31\x04<=10\x12W\n\x0e\x62\x61tch_settings\x18\x06 \x01(\x0b\x32\x39.yandex.cloud.serverless.triggers.v1.LoggingBatchSettingsB\x04\xe8\xc7\x31\x01\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18g \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\"\xca\x01\n\x16ObjectStorageEventType\x12)\n%OBJECT_STORAGE_EVENT_TYPE_UNSPECIFIED\x10\x00\x12+\n\'OBJECT_STORAGE_EVENT_TYPE_CREATE_OBJECT\x10\x01\x12+\n\'OBJECT_STORAGE_EVENT_TYPE_UPDATE_OBJECT\x10\x02\x12+\n\'OBJECT_STORAGE_EVENT_TYPE_DELETE_OBJECT\x10\x03\"\x93\x02\n\x1a\x43ontainerRegistryEventType\x12-\n)CONTAINER_REGISTRY_EVENT_TYPE_UNSPECIFIED\x10\x00\x12.\n*CONTAINER_REGISTRY_EVENT_TYPE_CREATE_IMAGE\x10\x01\x12.\n*CONTAINER_REGISTRY_EVENT_TYPE_DELETE_IMAGE\x10\x02\x12\x32\n.CONTAINER_REGISTRY_EVENT_TYPE_CREATE_IMAGE_TAG\x10\x03\x12\x32\n.CONTAINER_REGISTRY_EVENT_TYPE_DELETE_IMAGE_TAG\x10\x04\"8\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\n\n\x06PAUSED\x10\x02\"i\n\x12InvokeFunctionOnce\x12!\n\x0b\x66unction_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x14\n\x0c\x66unction_tag\x18\x02 \x01(\t\x12\x1a\n\x12service_account_id\x18\x03 \x01(\t\"\x8b\x02\n\x17InvokeFunctionWithRetry\x12!\n\x0b\x66unction_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x14\n\x0c\x66unction_tag\x18\x02 \x01(\t\x12\x1a\n\x12service_account_id\x18\x03 \x01(\t\x12J\n\x0eretry_settings\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.RetrySettings\x12O\n\x11\x64\x65\x61\x64_letter_queue\x18\x05 \x01(\x0b\x32\x34.yandex.cloud.serverless.triggers.v1.PutQueueMessage\"c\n\x13InvokeContainerOnce\x12\"\n\x0c\x63ontainer_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x1a\n\x12service_account_id\x18\x04 \x01(\t\"\x85\x02\n\x18InvokeContainerWithRetry\x12\"\n\x0c\x63ontainer_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x1a\n\x12service_account_id\x18\x04 \x01(\t\x12J\n\x0eretry_settings\x18\x05 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.RetrySettings\x12O\n\x11\x64\x65\x61\x64_letter_queue\x18\x06 \x01(\x0b\x32\x34.yandex.cloud.serverless.triggers.v1.PutQueueMessage\"M\n\x0fPutQueueMessage\x12\x10\n\x08queue_id\x18\x0b \x01(\t\x12(\n\x12service_account_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"X\n\rBatchSettings\x12\x16\n\x04size\x18\x01 \x01(\x03\x42\x08\xfa\xc7\x31\x04\x30-10\x12/\n\x06\x63utoff\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x04\xe8\xc7\x31\x01\"g\n\x16\x43loudLogsBatchSettings\x12\x17\n\x04size\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x30-100\x12\x34\n\x06\x63utoff\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05\x31s-1m\"e\n\x14LoggingBatchSettings\x12\x17\n\x04size\x18\x01 \x01(\x03\x42\t\xfa\xc7\x31\x05\x31-100\x12\x34\n\x06\x63utoff\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05\x31s-1m\"m\n\rRetrySettings\x12\x1f\n\x0eretry_attempts\x18\x01 \x01(\x03\x42\x07\xfa\xc7\x31\x03\x31-5\x12;\n\x08interval\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0e\xe8\xc7\x31\x01\xfa\xc7\x31\x06\x31\x30s-1m\"\x9a\x02\n\rBillingBudget\x12(\n\x12\x62illing_account_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1b\n\tbudget_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18g \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\"j\n\x17\x44\x61taStreamBatchSettings\x12\x19\n\x04size\x18\x01 \x01(\x03\x42\x0b\xfa\xc7\x31\x07\x31-65536\x12\x34\n\x06\x63utoff\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\t\xfa\xc7\x31\x05\x31s-1m\"\xf6\x02\n\nDataStream\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x02 \x01(\t\x12\x0e\n\x06stream\x18\x03 \x01(\t\x12\x1a\n\x12service_account_id\x18\x04 \x01(\t\x12T\n\x0e\x62\x61tch_settings\x18\x05 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.DataStreamBatchSettings\x12W\n\x0finvoke_function\x18\r \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18\x0f \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01\"v\n\x1bObjectStorageBucketSettings\x12-\n\tbucket_id\x18\x01 \x01(\tB\x1a\xf2\xc7\x31\x0e[-.0-9a-zA-Z]*\x8a\xc8\x31\x04\x33-63\x12(\n\x12service_account_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x83\x03\n\x04Mail\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12J\n\x0e\x62\x61tch_settings\x18\x03 \x01(\x0b\x32\x32.yandex.cloud.serverless.triggers.v1.BatchSettings\x12\\\n\x12\x61ttachments_bucket\x18\x04 \x01(\x0b\x32@.yandex.cloud.serverless.triggers.v1.ObjectStorageBucketSettings\x12W\n\x0finvoke_function\x18\x65 \x01(\x0b\x32<.yandex.cloud.serverless.triggers.v1.InvokeFunctionWithRetryH\x00\x12Y\n\x10invoke_container\x18g \x01(\x0b\x32=.yandex.cloud.serverless.triggers.v1.InvokeContainerWithRetryH\x00\x42\x0e\n\x06\x61\x63tion\x12\x04\xc0\xc1\x31\x01*\xe2\x01\n\x0bTriggerType\x12\x1c\n\x18TRIGGER_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TIMER\x10\x02\x12\x11\n\rMESSAGE_QUEUE\x10\x03\x12\x0f\n\x0bIOT_MESSAGE\x10\x04\x12\x16\n\x12IOT_BROKER_MESSAGE\x10\x0c\x12\x12\n\x0eOBJECT_STORAGE\x10\x05\x12\x16\n\x12\x43ONTAINER_REGISTRY\x10\x06\x12\x0e\n\nCLOUD_LOGS\x10\x07\x12\x0b\n\x07LOGGING\x10\x08\x12\x12\n\x0e\x42ILLING_BUDGET\x10\t\x12\x07\n\x03YDS\x10\n\x12\x08\n\x04MAIL\x10\x0b\x42{\n\'yandex.cloud.api.serverless.triggers.v1ZPgithub.com/yandex-cloud/go-genproto/yandex/cloud/serverless/triggers/v1;triggersb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.serverless.triggers.v1.trigger_pb2', _globals)
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
  _TRIGGER_TIMER.fields_by_name['payload']._options = None
  _TRIGGER_TIMER.fields_by_name['payload']._serialized_options = b'\212\3101\006<=4096'
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
  _TRIGGER_IOTBROKERMESSAGE.oneofs_by_name['action']._options = None
  _TRIGGER_IOTBROKERMESSAGE.oneofs_by_name['action']._serialized_options = b'\300\3011\001'
  _TRIGGER_IOTBROKERMESSAGE.fields_by_name['broker_id']._options = None
  _TRIGGER_IOTBROKERMESSAGE.fields_by_name['broker_id']._serialized_options = b'\350\3071\001'
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
  _TRIGGER_LOGGING.fields_by_name['stream_name']._options = None
  _TRIGGER_LOGGING.fields_by_name['stream_name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]\202\3101\005<=100'
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
  _RETRYSETTINGS.fields_by_name['interval']._serialized_options = b'\350\3071\001\372\3071\00610s-1m'
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
  _OBJECTSTORAGEBUCKETSETTINGS.fields_by_name['bucket_id']._options = None
  _OBJECTSTORAGEBUCKETSETTINGS.fields_by_name['bucket_id']._serialized_options = b'\362\3071\016[-.0-9a-zA-Z]*\212\3101\0043-63'
  _OBJECTSTORAGEBUCKETSETTINGS.fields_by_name['service_account_id']._options = None
  _OBJECTSTORAGEBUCKETSETTINGS.fields_by_name['service_account_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _MAIL.oneofs_by_name['action']._options = None
  _MAIL.oneofs_by_name['action']._serialized_options = b'\300\3011\001'
  _globals['_TRIGGERTYPE']._serialized_start=7880
  _globals['_TRIGGERTYPE']._serialized_end=8106
  _globals['_TRIGGER']._serialized_start=228
  _globals['_TRIGGER']._serialized_end=5367
  _globals['_TRIGGER_LABELSENTRY']._serialized_start=602
  _globals['_TRIGGER_LABELSENTRY']._serialized_end=647
  _globals['_TRIGGER_RULE']._serialized_start=650
  _globals['_TRIGGER_RULE']._serialized_end=1536
  _globals['_TRIGGER_TIMER']._serialized_start=1539
  _globals['_TRIGGER_TIMER']._serialized_end=1917
  _globals['_TRIGGER_MESSAGEQUEUE']._serialized_start=1920
  _globals['_TRIGGER_MESSAGEQUEUE']._serialized_end=2334
  _globals['_TRIGGER_IOTMESSAGE']._serialized_start=2337
  _globals['_TRIGGER_IOTMESSAGE']._serialized_end=2687
  _globals['_TRIGGER_IOTBROKERMESSAGE']._serialized_start=2690
  _globals['_TRIGGER_IOTBROKERMESSAGE']._serialized_end=3025
  _globals['_TRIGGER_OBJECTSTORAGE']._serialized_start=3028
  _globals['_TRIGGER_OBJECTSTORAGE']._serialized_end=3463
  _globals['_TRIGGER_CONTAINERREGISTRY']._serialized_start=3466
  _globals['_TRIGGER_CONTAINERREGISTRY']._serialized_end=3912
  _globals['_TRIGGER_CLOUDLOGS']._serialized_start=3915
  _globals['_TRIGGER_CLOUDLOGS']._serialized_end=4235
  _globals['_TRIGGER_LOGGING']._serialized_start=4238
  _globals['_TRIGGER_LOGGING']._serialized_end=4826
  _globals['_TRIGGER_OBJECTSTORAGEEVENTTYPE']._serialized_start=4829
  _globals['_TRIGGER_OBJECTSTORAGEEVENTTYPE']._serialized_end=5031
  _globals['_TRIGGER_CONTAINERREGISTRYEVENTTYPE']._serialized_start=5034
  _globals['_TRIGGER_CONTAINERREGISTRYEVENTTYPE']._serialized_end=5309
  _globals['_TRIGGER_STATUS']._serialized_start=5311
  _globals['_TRIGGER_STATUS']._serialized_end=5367
  _globals['_INVOKEFUNCTIONONCE']._serialized_start=5369
  _globals['_INVOKEFUNCTIONONCE']._serialized_end=5474
  _globals['_INVOKEFUNCTIONWITHRETRY']._serialized_start=5477
  _globals['_INVOKEFUNCTIONWITHRETRY']._serialized_end=5744
  _globals['_INVOKECONTAINERONCE']._serialized_start=5746
  _globals['_INVOKECONTAINERONCE']._serialized_end=5845
  _globals['_INVOKECONTAINERWITHRETRY']._serialized_start=5848
  _globals['_INVOKECONTAINERWITHRETRY']._serialized_end=6109
  _globals['_PUTQUEUEMESSAGE']._serialized_start=6111
  _globals['_PUTQUEUEMESSAGE']._serialized_end=6188
  _globals['_BATCHSETTINGS']._serialized_start=6190
  _globals['_BATCHSETTINGS']._serialized_end=6278
  _globals['_CLOUDLOGSBATCHSETTINGS']._serialized_start=6280
  _globals['_CLOUDLOGSBATCHSETTINGS']._serialized_end=6383
  _globals['_LOGGINGBATCHSETTINGS']._serialized_start=6385
  _globals['_LOGGINGBATCHSETTINGS']._serialized_end=6486
  _globals['_RETRYSETTINGS']._serialized_start=6488
  _globals['_RETRYSETTINGS']._serialized_end=6597
  _globals['_BILLINGBUDGET']._serialized_start=6600
  _globals['_BILLINGBUDGET']._serialized_end=6882
  _globals['_DATASTREAMBATCHSETTINGS']._serialized_start=6884
  _globals['_DATASTREAMBATCHSETTINGS']._serialized_end=6990
  _globals['_DATASTREAM']._serialized_start=6993
  _globals['_DATASTREAM']._serialized_end=7367
  _globals['_OBJECTSTORAGEBUCKETSETTINGS']._serialized_start=7369
  _globals['_OBJECTSTORAGEBUCKETSETTINGS']._serialized_end=7487
  _globals['_MAIL']._serialized_start=7490
  _globals['_MAIL']._serialized_end=7877
# @@protoc_insertion_point(module_scope)
