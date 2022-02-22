# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/iot/devices/v1/device_service.proto
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
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.iot.devices.v1 import device_pb2 as yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0yandex/cloud/iot/devices/v1/device_service.proto\x12\x1byandex.cloud.iot.devices.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1dyandex/cloud/validation.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a(yandex/cloud/iot/devices/v1/device.proto\"q\n\x10GetDeviceRequest\x12\x1f\n\tdevice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12<\n\x0b\x64\x65vice_view\x18\x02 \x01(\x0e\x32\'.yandex.cloud.iot.devices.v1.DeviceView\"\xae\x01\n\x16GetByNameDeviceRequest\x12!\n\x0bregistry_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x33\n\x0b\x64\x65vice_name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x12<\n\x0b\x64\x65vice_view\x18\x03 \x01(\x0e\x32\'.yandex.cloud.iot.devices.v1.DeviceView\"\xdc\x01\n\x12ListDevicesRequest\x12\x1f\n\x0bregistry_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12\x1d\n\tfolder_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50H\x00\x12\x1d\n\tpage_size\x18\x03 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12<\n\x0b\x64\x65vice_view\x18\x05 \x01(\x0e\x32\'.yandex.cloud.iot.devices.v1.DeviceViewB\n\n\x02id\x12\x04\xc0\xc1\x31\x01\"d\n\x13ListDevicesResponse\x12\x34\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32#.yandex.cloud.iot.devices.v1.Device\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xa5\x03\n\x13\x43reateDeviceRequest\x12!\n\x0bregistry_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12,\n\x04name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12R\n\x0c\x63\x65rtificates\x18\x04 \x03(\x0b\x32<.yandex.cloud.iot.devices.v1.CreateDeviceRequest.Certificate\x12Y\n\rtopic_aliases\x18\x05 \x03(\x0b\x32\x42.yandex.cloud.iot.devices.v1.CreateDeviceRequest.TopicAliasesEntry\x12\x10\n\x08password\x18\x06 \x01(\t\x1a\x33\n\x11TopicAliasesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\'\n\x0b\x43\x65rtificate\x12\x18\n\x10\x63\x65rtificate_data\x18\x01 \x01(\t\")\n\x14\x43reateDeviceMetadata\x12\x11\n\tdevice_id\x18\x01 \x01(\t\"\xc1\x02\n\x13UpdateDeviceRequest\x12\x1f\n\tdevice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12(\n\x04name\x18\x03 \x01(\tB\x1a\x8a\xc8\x31\x04<=50\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12Y\n\rtopic_aliases\x18\x05 \x03(\x0b\x32\x42.yandex.cloud.iot.devices.v1.UpdateDeviceRequest.TopicAliasesEntry\x1a\x33\n\x11TopicAliasesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\")\n\x14UpdateDeviceMetadata\x12\x11\n\tdevice_id\x18\x01 \x01(\t\"6\n\x13\x44\x65leteDeviceRequest\x12\x1f\n\tdevice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\")\n\x14\x44\x65leteDeviceMetadata\x12\x11\n\tdevice_id\x18\x01 \x01(\t\"@\n\x1dListDeviceCertificatesRequest\x12\x1f\n\tdevice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"f\n\x1eListDeviceCertificatesResponse\x12\x44\n\x0c\x63\x65rtificates\x18\x01 \x03(\x0b\x32..yandex.cloud.iot.devices.v1.DeviceCertificate\"X\n\x1b\x41\x64\x64\x44\x65viceCertificateRequest\x12\x1f\n\tdevice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x18\n\x10\x63\x65rtificate_data\x18\x03 \x01(\t\"F\n\x1c\x41\x64\x64\x44\x65viceCertificateMetadata\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66ingerprint\x18\x02 \x01(\t\"d\n\x1e\x44\x65leteDeviceCertificateRequest\x12\x1f\n\tdevice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12!\n\x0b\x66ingerprint\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"e\n\x1f\x44\x65leteDeviceCertificateMetadata\x12\x1f\n\tdevice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12!\n\x0b\x66ingerprint\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"=\n\x1aListDevicePasswordsRequest\x12\x1f\n\tdevice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"]\n\x1bListDevicePasswordsResponse\x12>\n\tpasswords\x18\x01 \x03(\x0b\x32+.yandex.cloud.iot.devices.v1.DevicePassword\"W\n\x18\x41\x64\x64\x44\x65vicePasswordRequest\x12\x1f\n\tdevice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1a\n\x08password\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04>=14\"C\n\x19\x41\x64\x64\x44\x65vicePasswordMetadata\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x13\n\x0bpassword_id\x18\x02 \x01(\t\"a\n\x1b\x44\x65leteDevicePasswordRequest\x12\x1f\n\tdevice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12!\n\x0bpassword_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"b\n\x1c\x44\x65leteDevicePasswordMetadata\x12\x1f\n\tdevice_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12!\n\x0bpassword_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x90\x01\n\x1bListDeviceOperationsRequest\x12\x17\n\tdevice_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"n\n\x1cListDeviceOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xb0\x13\n\rDeviceService\x12\x86\x01\n\x03Get\x12-.yandex.cloud.iot.devices.v1.GetDeviceRequest\x1a#.yandex.cloud.iot.devices.v1.Device\"+\x82\xd3\xe4\x93\x02%\x12#/iot-devices/v1/devices/{device_id}\x12\x90\x01\n\tGetByName\x12\x33.yandex.cloud.iot.devices.v1.GetByNameDeviceRequest\x1a#.yandex.cloud.iot.devices.v1.Device\")\x82\xd3\xe4\x93\x02#\x12!/iot-devices/v1/devices:getByName\x12\x8a\x01\n\x04List\x12/.yandex.cloud.iot.devices.v1.ListDevicesRequest\x1a\x30.yandex.cloud.iot.devices.v1.ListDevicesResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/iot-devices/v1/devices\x12\xa3\x01\n\x06\x43reate\x12\x30.yandex.cloud.iot.devices.v1.CreateDeviceRequest\x1a!.yandex.cloud.operation.Operation\"D\x82\xd3\xe4\x93\x02\x1c\"\x17/iot-devices/v1/devices:\x01*\xb2\xd2*\x1e\n\x14\x43reateDeviceMetadata\x12\x06\x44\x65vice\x12\xaf\x01\n\x06Update\x12\x30.yandex.cloud.iot.devices.v1.UpdateDeviceRequest\x1a!.yandex.cloud.operation.Operation\"P\x82\xd3\xe4\x93\x02(2#/iot-devices/v1/devices/{device_id}:\x01*\xb2\xd2*\x1e\n\x14UpdateDeviceMetadata\x12\x06\x44\x65vice\x12\xbb\x01\n\x06\x44\x65lete\x12\x30.yandex.cloud.iot.devices.v1.DeleteDeviceRequest\x1a!.yandex.cloud.operation.Operation\"\\\x82\xd3\xe4\x93\x02%*#/iot-devices/v1/devices/{device_id}\xb2\xd2*-\n\x14\x44\x65leteDeviceMetadata\x12\x15google.protobuf.Empty\x12\xc5\x01\n\x10ListCertificates\x12:.yandex.cloud.iot.devices.v1.ListDeviceCertificatesRequest\x1a;.yandex.cloud.iot.devices.v1.ListDeviceCertificatesResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/iot-devices/v1/devices/{device_id}/certificates\x12\xdf\x01\n\x0e\x41\x64\x64\x43\x65rtificate\x12\x38.yandex.cloud.iot.devices.v1.AddDeviceCertificateRequest\x1a!.yandex.cloud.operation.Operation\"p\x82\xd3\xe4\x93\x02\x35\"0/iot-devices/v1/devices/{device_id}/certificates:\x01*\xb2\xd2*1\n\x1c\x41\x64\x64\x44\x65viceCertificateMetadata\x12\x11\x44\x65viceCertificate\x12\xf8\x01\n\x11\x44\x65leteCertificate\x12;.yandex.cloud.iot.devices.v1.DeleteDeviceCertificateRequest\x1a!.yandex.cloud.operation.Operation\"\x82\x01\x82\xd3\xe4\x93\x02@*>/iot-devices/v1/devices/{device_id}/certificates/{fingerprint}\xb2\xd2*8\n\x1f\x44\x65leteDeviceCertificateMetadata\x12\x15google.protobuf.Empty\x12\xb9\x01\n\rListPasswords\x12\x37.yandex.cloud.iot.devices.v1.ListDevicePasswordsRequest\x1a\x38.yandex.cloud.iot.devices.v1.ListDevicePasswordsResponse\"5\x82\xd3\xe4\x93\x02/\x12-/iot-devices/v1/devices/{device_id}/passwords\x12\xd0\x01\n\x0b\x41\x64\x64Password\x12\x35.yandex.cloud.iot.devices.v1.AddDevicePasswordRequest\x1a!.yandex.cloud.operation.Operation\"g\x82\xd3\xe4\x93\x02\x32\"-/iot-devices/v1/devices/{device_id}/passwords:\x01*\xb2\xd2*+\n\x19\x41\x64\x64\x44\x65vicePasswordMetadata\x12\x0e\x44\x65vicePassword\x12\xeb\x01\n\x0e\x44\x65letePassword\x12\x38.yandex.cloud.iot.devices.v1.DeleteDevicePasswordRequest\x1a!.yandex.cloud.operation.Operation\"|\x82\xd3\xe4\x93\x02=*;/iot-devices/v1/devices/{device_id}/passwords/{password_id}\xb2\xd2*5\n\x1c\x44\x65leteDevicePasswordMetadata\x12\x15google.protobuf.Empty\x12\xbd\x01\n\x0eListOperations\x12\x38.yandex.cloud.iot.devices.v1.ListDeviceOperationsRequest\x1a\x39.yandex.cloud.iot.devices.v1.ListDeviceOperationsResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./iot-devices/v1/devices/{device_id}/operationsBj\n\x1fyandex.cloud.api.iot.devices.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/devices/v1;devicesb\x06proto3')



_GETDEVICEREQUEST = DESCRIPTOR.message_types_by_name['GetDeviceRequest']
_GETBYNAMEDEVICEREQUEST = DESCRIPTOR.message_types_by_name['GetByNameDeviceRequest']
_LISTDEVICESREQUEST = DESCRIPTOR.message_types_by_name['ListDevicesRequest']
_LISTDEVICESRESPONSE = DESCRIPTOR.message_types_by_name['ListDevicesResponse']
_CREATEDEVICEREQUEST = DESCRIPTOR.message_types_by_name['CreateDeviceRequest']
_CREATEDEVICEREQUEST_TOPICALIASESENTRY = _CREATEDEVICEREQUEST.nested_types_by_name['TopicAliasesEntry']
_CREATEDEVICEREQUEST_CERTIFICATE = _CREATEDEVICEREQUEST.nested_types_by_name['Certificate']
_CREATEDEVICEMETADATA = DESCRIPTOR.message_types_by_name['CreateDeviceMetadata']
_UPDATEDEVICEREQUEST = DESCRIPTOR.message_types_by_name['UpdateDeviceRequest']
_UPDATEDEVICEREQUEST_TOPICALIASESENTRY = _UPDATEDEVICEREQUEST.nested_types_by_name['TopicAliasesEntry']
_UPDATEDEVICEMETADATA = DESCRIPTOR.message_types_by_name['UpdateDeviceMetadata']
_DELETEDEVICEREQUEST = DESCRIPTOR.message_types_by_name['DeleteDeviceRequest']
_DELETEDEVICEMETADATA = DESCRIPTOR.message_types_by_name['DeleteDeviceMetadata']
_LISTDEVICECERTIFICATESREQUEST = DESCRIPTOR.message_types_by_name['ListDeviceCertificatesRequest']
_LISTDEVICECERTIFICATESRESPONSE = DESCRIPTOR.message_types_by_name['ListDeviceCertificatesResponse']
_ADDDEVICECERTIFICATEREQUEST = DESCRIPTOR.message_types_by_name['AddDeviceCertificateRequest']
_ADDDEVICECERTIFICATEMETADATA = DESCRIPTOR.message_types_by_name['AddDeviceCertificateMetadata']
_DELETEDEVICECERTIFICATEREQUEST = DESCRIPTOR.message_types_by_name['DeleteDeviceCertificateRequest']
_DELETEDEVICECERTIFICATEMETADATA = DESCRIPTOR.message_types_by_name['DeleteDeviceCertificateMetadata']
_LISTDEVICEPASSWORDSREQUEST = DESCRIPTOR.message_types_by_name['ListDevicePasswordsRequest']
_LISTDEVICEPASSWORDSRESPONSE = DESCRIPTOR.message_types_by_name['ListDevicePasswordsResponse']
_ADDDEVICEPASSWORDREQUEST = DESCRIPTOR.message_types_by_name['AddDevicePasswordRequest']
_ADDDEVICEPASSWORDMETADATA = DESCRIPTOR.message_types_by_name['AddDevicePasswordMetadata']
_DELETEDEVICEPASSWORDREQUEST = DESCRIPTOR.message_types_by_name['DeleteDevicePasswordRequest']
_DELETEDEVICEPASSWORDMETADATA = DESCRIPTOR.message_types_by_name['DeleteDevicePasswordMetadata']
_LISTDEVICEOPERATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListDeviceOperationsRequest']
_LISTDEVICEOPERATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListDeviceOperationsResponse']
GetDeviceRequest = _reflection.GeneratedProtocolMessageType('GetDeviceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDEVICEREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.GetDeviceRequest)
  })
_sym_db.RegisterMessage(GetDeviceRequest)

GetByNameDeviceRequest = _reflection.GeneratedProtocolMessageType('GetByNameDeviceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBYNAMEDEVICEREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.GetByNameDeviceRequest)
  })
_sym_db.RegisterMessage(GetByNameDeviceRequest)

ListDevicesRequest = _reflection.GeneratedProtocolMessageType('ListDevicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEVICESREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.ListDevicesRequest)
  })
_sym_db.RegisterMessage(ListDevicesRequest)

ListDevicesResponse = _reflection.GeneratedProtocolMessageType('ListDevicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEVICESRESPONSE,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.ListDevicesResponse)
  })
_sym_db.RegisterMessage(ListDevicesResponse)

CreateDeviceRequest = _reflection.GeneratedProtocolMessageType('CreateDeviceRequest', (_message.Message,), {

  'TopicAliasesEntry' : _reflection.GeneratedProtocolMessageType('TopicAliasesEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATEDEVICEREQUEST_TOPICALIASESENTRY,
    '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.CreateDeviceRequest.TopicAliasesEntry)
    })
  ,

  'Certificate' : _reflection.GeneratedProtocolMessageType('Certificate', (_message.Message,), {
    'DESCRIPTOR' : _CREATEDEVICEREQUEST_CERTIFICATE,
    '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.CreateDeviceRequest.Certificate)
    })
  ,
  'DESCRIPTOR' : _CREATEDEVICEREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.CreateDeviceRequest)
  })
_sym_db.RegisterMessage(CreateDeviceRequest)
_sym_db.RegisterMessage(CreateDeviceRequest.TopicAliasesEntry)
_sym_db.RegisterMessage(CreateDeviceRequest.Certificate)

CreateDeviceMetadata = _reflection.GeneratedProtocolMessageType('CreateDeviceMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDEVICEMETADATA,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.CreateDeviceMetadata)
  })
_sym_db.RegisterMessage(CreateDeviceMetadata)

UpdateDeviceRequest = _reflection.GeneratedProtocolMessageType('UpdateDeviceRequest', (_message.Message,), {

  'TopicAliasesEntry' : _reflection.GeneratedProtocolMessageType('TopicAliasesEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEDEVICEREQUEST_TOPICALIASESENTRY,
    '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.UpdateDeviceRequest.TopicAliasesEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATEDEVICEREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.UpdateDeviceRequest)
  })
_sym_db.RegisterMessage(UpdateDeviceRequest)
_sym_db.RegisterMessage(UpdateDeviceRequest.TopicAliasesEntry)

UpdateDeviceMetadata = _reflection.GeneratedProtocolMessageType('UpdateDeviceMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDEVICEMETADATA,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.UpdateDeviceMetadata)
  })
_sym_db.RegisterMessage(UpdateDeviceMetadata)

DeleteDeviceRequest = _reflection.GeneratedProtocolMessageType('DeleteDeviceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDEVICEREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.DeleteDeviceRequest)
  })
_sym_db.RegisterMessage(DeleteDeviceRequest)

DeleteDeviceMetadata = _reflection.GeneratedProtocolMessageType('DeleteDeviceMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDEVICEMETADATA,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.DeleteDeviceMetadata)
  })
_sym_db.RegisterMessage(DeleteDeviceMetadata)

ListDeviceCertificatesRequest = _reflection.GeneratedProtocolMessageType('ListDeviceCertificatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEVICECERTIFICATESREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.ListDeviceCertificatesRequest)
  })
_sym_db.RegisterMessage(ListDeviceCertificatesRequest)

ListDeviceCertificatesResponse = _reflection.GeneratedProtocolMessageType('ListDeviceCertificatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEVICECERTIFICATESRESPONSE,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.ListDeviceCertificatesResponse)
  })
_sym_db.RegisterMessage(ListDeviceCertificatesResponse)

AddDeviceCertificateRequest = _reflection.GeneratedProtocolMessageType('AddDeviceCertificateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDDEVICECERTIFICATEREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.AddDeviceCertificateRequest)
  })
_sym_db.RegisterMessage(AddDeviceCertificateRequest)

AddDeviceCertificateMetadata = _reflection.GeneratedProtocolMessageType('AddDeviceCertificateMetadata', (_message.Message,), {
  'DESCRIPTOR' : _ADDDEVICECERTIFICATEMETADATA,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.AddDeviceCertificateMetadata)
  })
_sym_db.RegisterMessage(AddDeviceCertificateMetadata)

DeleteDeviceCertificateRequest = _reflection.GeneratedProtocolMessageType('DeleteDeviceCertificateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDEVICECERTIFICATEREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.DeleteDeviceCertificateRequest)
  })
_sym_db.RegisterMessage(DeleteDeviceCertificateRequest)

DeleteDeviceCertificateMetadata = _reflection.GeneratedProtocolMessageType('DeleteDeviceCertificateMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDEVICECERTIFICATEMETADATA,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.DeleteDeviceCertificateMetadata)
  })
_sym_db.RegisterMessage(DeleteDeviceCertificateMetadata)

ListDevicePasswordsRequest = _reflection.GeneratedProtocolMessageType('ListDevicePasswordsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEVICEPASSWORDSREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.ListDevicePasswordsRequest)
  })
_sym_db.RegisterMessage(ListDevicePasswordsRequest)

ListDevicePasswordsResponse = _reflection.GeneratedProtocolMessageType('ListDevicePasswordsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEVICEPASSWORDSRESPONSE,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.ListDevicePasswordsResponse)
  })
_sym_db.RegisterMessage(ListDevicePasswordsResponse)

AddDevicePasswordRequest = _reflection.GeneratedProtocolMessageType('AddDevicePasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDDEVICEPASSWORDREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.AddDevicePasswordRequest)
  })
_sym_db.RegisterMessage(AddDevicePasswordRequest)

AddDevicePasswordMetadata = _reflection.GeneratedProtocolMessageType('AddDevicePasswordMetadata', (_message.Message,), {
  'DESCRIPTOR' : _ADDDEVICEPASSWORDMETADATA,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.AddDevicePasswordMetadata)
  })
_sym_db.RegisterMessage(AddDevicePasswordMetadata)

DeleteDevicePasswordRequest = _reflection.GeneratedProtocolMessageType('DeleteDevicePasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDEVICEPASSWORDREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.DeleteDevicePasswordRequest)
  })
_sym_db.RegisterMessage(DeleteDevicePasswordRequest)

DeleteDevicePasswordMetadata = _reflection.GeneratedProtocolMessageType('DeleteDevicePasswordMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDEVICEPASSWORDMETADATA,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.DeleteDevicePasswordMetadata)
  })
_sym_db.RegisterMessage(DeleteDevicePasswordMetadata)

ListDeviceOperationsRequest = _reflection.GeneratedProtocolMessageType('ListDeviceOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEVICEOPERATIONSREQUEST,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.ListDeviceOperationsRequest)
  })
_sym_db.RegisterMessage(ListDeviceOperationsRequest)

ListDeviceOperationsResponse = _reflection.GeneratedProtocolMessageType('ListDeviceOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEVICEOPERATIONSRESPONSE,
  '__module__' : 'yandex.cloud.iot.devices.v1.device_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.iot.devices.v1.ListDeviceOperationsResponse)
  })
_sym_db.RegisterMessage(ListDeviceOperationsResponse)

_DEVICESERVICE = DESCRIPTOR.services_by_name['DeviceService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037yandex.cloud.api.iot.devices.v1ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/iot/devices/v1;devices'
  _GETDEVICEREQUEST.fields_by_name['device_id']._options = None
  _GETDEVICEREQUEST.fields_by_name['device_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _GETBYNAMEDEVICEREQUEST.fields_by_name['registry_id']._options = None
  _GETBYNAMEDEVICEREQUEST.fields_by_name['registry_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _GETBYNAMEDEVICEREQUEST.fields_by_name['device_name']._options = None
  _GETBYNAMEDEVICEREQUEST.fields_by_name['device_name']._serialized_options = b'\350\3071\001\212\3101\004<=50\362\3071\016[a-zA-Z0-9_-]*'
  _LISTDEVICESREQUEST.oneofs_by_name['id']._options = None
  _LISTDEVICESREQUEST.oneofs_by_name['id']._serialized_options = b'\300\3011\001'
  _LISTDEVICESREQUEST.fields_by_name['registry_id']._options = None
  _LISTDEVICESREQUEST.fields_by_name['registry_id']._serialized_options = b'\212\3101\004<=50'
  _LISTDEVICESREQUEST.fields_by_name['folder_id']._options = None
  _LISTDEVICESREQUEST.fields_by_name['folder_id']._serialized_options = b'\212\3101\004<=50'
  _LISTDEVICESREQUEST.fields_by_name['page_size']._options = None
  _LISTDEVICESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTDEVICESREQUEST.fields_by_name['page_token']._options = None
  _LISTDEVICESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _CREATEDEVICEREQUEST_TOPICALIASESENTRY._options = None
  _CREATEDEVICEREQUEST_TOPICALIASESENTRY._serialized_options = b'8\001'
  _CREATEDEVICEREQUEST.fields_by_name['registry_id']._options = None
  _CREATEDEVICEREQUEST.fields_by_name['registry_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATEDEVICEREQUEST.fields_by_name['name']._options = None
  _CREATEDEVICEREQUEST.fields_by_name['name']._serialized_options = b'\350\3071\001\212\3101\004<=50\362\3071\016[a-zA-Z0-9_-]*'
  _CREATEDEVICEREQUEST.fields_by_name['description']._options = None
  _CREATEDEVICEREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATEDEVICEREQUEST_TOPICALIASESENTRY._options = None
  _UPDATEDEVICEREQUEST_TOPICALIASESENTRY._serialized_options = b'8\001'
  _UPDATEDEVICEREQUEST.fields_by_name['device_id']._options = None
  _UPDATEDEVICEREQUEST.fields_by_name['device_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEDEVICEREQUEST.fields_by_name['name']._options = None
  _UPDATEDEVICEREQUEST.fields_by_name['name']._serialized_options = b'\212\3101\004<=50\362\3071\016[a-zA-Z0-9_-]*'
  _UPDATEDEVICEREQUEST.fields_by_name['description']._options = None
  _UPDATEDEVICEREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _DELETEDEVICEREQUEST.fields_by_name['device_id']._options = None
  _DELETEDEVICEREQUEST.fields_by_name['device_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTDEVICECERTIFICATESREQUEST.fields_by_name['device_id']._options = None
  _LISTDEVICECERTIFICATESREQUEST.fields_by_name['device_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _ADDDEVICECERTIFICATEREQUEST.fields_by_name['device_id']._options = None
  _ADDDEVICECERTIFICATEREQUEST.fields_by_name['device_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEDEVICECERTIFICATEREQUEST.fields_by_name['device_id']._options = None
  _DELETEDEVICECERTIFICATEREQUEST.fields_by_name['device_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEDEVICECERTIFICATEREQUEST.fields_by_name['fingerprint']._options = None
  _DELETEDEVICECERTIFICATEREQUEST.fields_by_name['fingerprint']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEDEVICECERTIFICATEMETADATA.fields_by_name['device_id']._options = None
  _DELETEDEVICECERTIFICATEMETADATA.fields_by_name['device_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEDEVICECERTIFICATEMETADATA.fields_by_name['fingerprint']._options = None
  _DELETEDEVICECERTIFICATEMETADATA.fields_by_name['fingerprint']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTDEVICEPASSWORDSREQUEST.fields_by_name['device_id']._options = None
  _LISTDEVICEPASSWORDSREQUEST.fields_by_name['device_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _ADDDEVICEPASSWORDREQUEST.fields_by_name['device_id']._options = None
  _ADDDEVICEPASSWORDREQUEST.fields_by_name['device_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _ADDDEVICEPASSWORDREQUEST.fields_by_name['password']._options = None
  _ADDDEVICEPASSWORDREQUEST.fields_by_name['password']._serialized_options = b'\212\3101\004>=14'
  _DELETEDEVICEPASSWORDREQUEST.fields_by_name['device_id']._options = None
  _DELETEDEVICEPASSWORDREQUEST.fields_by_name['device_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEDEVICEPASSWORDREQUEST.fields_by_name['password_id']._options = None
  _DELETEDEVICEPASSWORDREQUEST.fields_by_name['password_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEDEVICEPASSWORDMETADATA.fields_by_name['device_id']._options = None
  _DELETEDEVICEPASSWORDMETADATA.fields_by_name['device_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEDEVICEPASSWORDMETADATA.fields_by_name['password_id']._options = None
  _DELETEDEVICEPASSWORDMETADATA.fields_by_name['password_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTDEVICEOPERATIONSREQUEST.fields_by_name['device_id']._options = None
  _LISTDEVICEOPERATIONSREQUEST.fields_by_name['device_id']._serialized_options = b'\350\3071\001'
  _LISTDEVICEOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTDEVICEOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTDEVICEOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTDEVICEOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTDEVICEOPERATIONSREQUEST.fields_by_name['filter']._options = None
  _LISTDEVICEOPERATIONSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _DEVICESERVICE.methods_by_name['Get']._options = None
  _DEVICESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002%\022#/iot-devices/v1/devices/{device_id}'
  _DEVICESERVICE.methods_by_name['GetByName']._options = None
  _DEVICESERVICE.methods_by_name['GetByName']._serialized_options = b'\202\323\344\223\002#\022!/iot-devices/v1/devices:getByName'
  _DEVICESERVICE.methods_by_name['List']._options = None
  _DEVICESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\031\022\027/iot-devices/v1/devices'
  _DEVICESERVICE.methods_by_name['Create']._options = None
  _DEVICESERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\034\"\027/iot-devices/v1/devices:\001*\262\322*\036\n\024CreateDeviceMetadata\022\006Device'
  _DEVICESERVICE.methods_by_name['Update']._options = None
  _DEVICESERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002(2#/iot-devices/v1/devices/{device_id}:\001*\262\322*\036\n\024UpdateDeviceMetadata\022\006Device'
  _DEVICESERVICE.methods_by_name['Delete']._options = None
  _DEVICESERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002%*#/iot-devices/v1/devices/{device_id}\262\322*-\n\024DeleteDeviceMetadata\022\025google.protobuf.Empty'
  _DEVICESERVICE.methods_by_name['ListCertificates']._options = None
  _DEVICESERVICE.methods_by_name['ListCertificates']._serialized_options = b'\202\323\344\223\0022\0220/iot-devices/v1/devices/{device_id}/certificates'
  _DEVICESERVICE.methods_by_name['AddCertificate']._options = None
  _DEVICESERVICE.methods_by_name['AddCertificate']._serialized_options = b'\202\323\344\223\0025\"0/iot-devices/v1/devices/{device_id}/certificates:\001*\262\322*1\n\034AddDeviceCertificateMetadata\022\021DeviceCertificate'
  _DEVICESERVICE.methods_by_name['DeleteCertificate']._options = None
  _DEVICESERVICE.methods_by_name['DeleteCertificate']._serialized_options = b'\202\323\344\223\002@*>/iot-devices/v1/devices/{device_id}/certificates/{fingerprint}\262\322*8\n\037DeleteDeviceCertificateMetadata\022\025google.protobuf.Empty'
  _DEVICESERVICE.methods_by_name['ListPasswords']._options = None
  _DEVICESERVICE.methods_by_name['ListPasswords']._serialized_options = b'\202\323\344\223\002/\022-/iot-devices/v1/devices/{device_id}/passwords'
  _DEVICESERVICE.methods_by_name['AddPassword']._options = None
  _DEVICESERVICE.methods_by_name['AddPassword']._serialized_options = b'\202\323\344\223\0022\"-/iot-devices/v1/devices/{device_id}/passwords:\001*\262\322*+\n\031AddDevicePasswordMetadata\022\016DevicePassword'
  _DEVICESERVICE.methods_by_name['DeletePassword']._options = None
  _DEVICESERVICE.methods_by_name['DeletePassword']._serialized_options = b'\202\323\344\223\002=*;/iot-devices/v1/devices/{device_id}/passwords/{password_id}\262\322*5\n\034DeleteDevicePasswordMetadata\022\025google.protobuf.Empty'
  _DEVICESERVICE.methods_by_name['ListOperations']._options = None
  _DEVICESERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0020\022./iot-devices/v1/devices/{device_id}/operations'
  _GETDEVICEREQUEST._serialized_start=292
  _GETDEVICEREQUEST._serialized_end=405
  _GETBYNAMEDEVICEREQUEST._serialized_start=408
  _GETBYNAMEDEVICEREQUEST._serialized_end=582
  _LISTDEVICESREQUEST._serialized_start=585
  _LISTDEVICESREQUEST._serialized_end=805
  _LISTDEVICESRESPONSE._serialized_start=807
  _LISTDEVICESRESPONSE._serialized_end=907
  _CREATEDEVICEREQUEST._serialized_start=910
  _CREATEDEVICEREQUEST._serialized_end=1331
  _CREATEDEVICEREQUEST_TOPICALIASESENTRY._serialized_start=1239
  _CREATEDEVICEREQUEST_TOPICALIASESENTRY._serialized_end=1290
  _CREATEDEVICEREQUEST_CERTIFICATE._serialized_start=1292
  _CREATEDEVICEREQUEST_CERTIFICATE._serialized_end=1331
  _CREATEDEVICEMETADATA._serialized_start=1333
  _CREATEDEVICEMETADATA._serialized_end=1374
  _UPDATEDEVICEREQUEST._serialized_start=1377
  _UPDATEDEVICEREQUEST._serialized_end=1698
  _UPDATEDEVICEREQUEST_TOPICALIASESENTRY._serialized_start=1239
  _UPDATEDEVICEREQUEST_TOPICALIASESENTRY._serialized_end=1290
  _UPDATEDEVICEMETADATA._serialized_start=1700
  _UPDATEDEVICEMETADATA._serialized_end=1741
  _DELETEDEVICEREQUEST._serialized_start=1743
  _DELETEDEVICEREQUEST._serialized_end=1797
  _DELETEDEVICEMETADATA._serialized_start=1799
  _DELETEDEVICEMETADATA._serialized_end=1840
  _LISTDEVICECERTIFICATESREQUEST._serialized_start=1842
  _LISTDEVICECERTIFICATESREQUEST._serialized_end=1906
  _LISTDEVICECERTIFICATESRESPONSE._serialized_start=1908
  _LISTDEVICECERTIFICATESRESPONSE._serialized_end=2010
  _ADDDEVICECERTIFICATEREQUEST._serialized_start=2012
  _ADDDEVICECERTIFICATEREQUEST._serialized_end=2100
  _ADDDEVICECERTIFICATEMETADATA._serialized_start=2102
  _ADDDEVICECERTIFICATEMETADATA._serialized_end=2172
  _DELETEDEVICECERTIFICATEREQUEST._serialized_start=2174
  _DELETEDEVICECERTIFICATEREQUEST._serialized_end=2274
  _DELETEDEVICECERTIFICATEMETADATA._serialized_start=2276
  _DELETEDEVICECERTIFICATEMETADATA._serialized_end=2377
  _LISTDEVICEPASSWORDSREQUEST._serialized_start=2379
  _LISTDEVICEPASSWORDSREQUEST._serialized_end=2440
  _LISTDEVICEPASSWORDSRESPONSE._serialized_start=2442
  _LISTDEVICEPASSWORDSRESPONSE._serialized_end=2535
  _ADDDEVICEPASSWORDREQUEST._serialized_start=2537
  _ADDDEVICEPASSWORDREQUEST._serialized_end=2624
  _ADDDEVICEPASSWORDMETADATA._serialized_start=2626
  _ADDDEVICEPASSWORDMETADATA._serialized_end=2693
  _DELETEDEVICEPASSWORDREQUEST._serialized_start=2695
  _DELETEDEVICEPASSWORDREQUEST._serialized_end=2792
  _DELETEDEVICEPASSWORDMETADATA._serialized_start=2794
  _DELETEDEVICEPASSWORDMETADATA._serialized_end=2892
  _LISTDEVICEOPERATIONSREQUEST._serialized_start=2895
  _LISTDEVICEOPERATIONSREQUEST._serialized_end=3039
  _LISTDEVICEOPERATIONSRESPONSE._serialized_start=3041
  _LISTDEVICEOPERATIONSRESPONSE._serialized_end=3151
  _DEVICESERVICE._serialized_start=3154
  _DEVICESERVICE._serialized_end=5634
# @@protoc_insertion_point(module_scope)
