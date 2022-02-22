# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/vpc/v1/address_service.proto
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
from yandex.cloud.vpc.v1 import address_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_address__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)yandex/cloud/vpc/v1/address_service.proto\x12\x13yandex.cloud.vpc.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a!yandex/cloud/vpc/v1/address.proto\x1a\x1dyandex/cloud/validation.proto\"5\n\x11GetAddressRequest\x12 \n\naddress_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"F\n\x18GetAddressByValueRequest\x12\x1f\n\x15\x65xternal_ipv4_address\x18\x01 \x01(\tH\x00\x42\t\n\x07\x61\x64\x64ress\"\x85\x01\n\x14ListAddressesRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\"a\n\x15ListAddressesResponse\x12/\n\taddresses\x18\x01 \x03(\x0b\x32\x1c.yandex.cloud.vpc.v1.Address\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xa4\x03\n\x14\x43reateAddressRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x04name\x18\x02 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x86\x01\n\x06labels\x18\x04 \x03(\x0b\x32\x35.yandex.cloud.vpc.v1.CreateAddressRequest.LabelsEntryB?\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0b[-_0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x12\x12\x10[a-z][-_0-9a-z]*\x12R\n\x1a\x65xternal_ipv4_address_spec\x18\x05 \x01(\x0b\x32,.yandex.cloud.vpc.v1.ExternalIpv4AddressSpecH\x00\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0e\n\x0c\x61\x64\x64ress_spec\"{\n\x17\x45xternalIpv4AddressSpec\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0f\n\x07zone_id\x18\x02 \x01(\t\x12>\n\x0crequirements\x18\x03 \x01(\x0b\x32(.yandex.cloud.vpc.v1.AddressRequirements\"+\n\x15\x43reateAddressMetadata\x12\x12\n\naddress_id\x18\x01 \x01(\t\"\x84\x03\n\x14UpdateAddressRequest\x12 \n\naddress_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12/\n\x04name\x18\x03 \x01(\tB!\xf2\xc7\x31\x1d|[a-z][-a-z0-9]{1,61}[a-z0-9]\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x86\x01\n\x06labels\x18\x05 \x03(\x0b\x32\x35.yandex.cloud.vpc.v1.UpdateAddressRequest.LabelsEntryB?\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xf2\xc7\x31\x0b[-_0-9a-z]*\xb2\xc8\x31\x06\x1a\x04\x31-63\xb2\xc8\x31\x12\x12\x10[a-z][-_0-9a-z]*\x12\x10\n\x08reserved\x18\x06 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x15UpdateAddressMetadata\x12\x12\n\naddress_id\x18\x01 \x01(\t\"8\n\x14\x44\x65leteAddressRequest\x12 \n\naddress_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"+\n\x15\x44\x65leteAddressMetadata\x12\x12\n\naddress_id\x18\x01 \x01(\t\"~\n\x1cListAddressOperationsRequest\x12 \n\naddress_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"o\n\x1dListAddressOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"c\n\x12MoveAddressRequest\x12 \n\naddress_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12+\n\x15\x64\x65stination_folder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\")\n\x13MoveAddressMetadata\x12\x12\n\naddress_id\x18\x01 \x01(\t2\xc7\t\n\x0e\x41\x64\x64ressService\x12s\n\x03Get\x12&.yandex.cloud.vpc.v1.GetAddressRequest\x1a\x1c.yandex.cloud.vpc.v1.Address\"&\x82\xd3\xe4\x93\x02 \x12\x1e/vpc/v1/addresses/{address_id}\x12|\n\nGetByValue\x12-.yandex.cloud.vpc.v1.GetAddressByValueRequest\x1a\x1c.yandex.cloud.vpc.v1.Address\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/vpc/v1/addresses:byValue\x12x\n\x04List\x12).yandex.cloud.vpc.v1.ListAddressesRequest\x1a*.yandex.cloud.vpc.v1.ListAddressesResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/vpc/v1/addresses\x12\x98\x01\n\x06\x43reate\x12).yandex.cloud.vpc.v1.CreateAddressRequest\x1a!.yandex.cloud.operation.Operation\"@\x82\xd3\xe4\x93\x02\x16\"\x11/vpc/v1/addresses:\x01*\xb2\xd2* \n\x15\x43reateAddressMetadata\x12\x07\x41\x64\x64ress\x12\xa5\x01\n\x06Update\x12).yandex.cloud.vpc.v1.UpdateAddressRequest\x1a!.yandex.cloud.operation.Operation\"M\x82\xd3\xe4\x93\x02#2\x1e/vpc/v1/addresses/{address_id}:\x01*\xb2\xd2* \n\x15UpdateAddressMetadata\x12\x07\x41\x64\x64ress\x12\xb0\x01\n\x06\x44\x65lete\x12).yandex.cloud.vpc.v1.DeleteAddressRequest\x1a!.yandex.cloud.operation.Operation\"X\x82\xd3\xe4\x93\x02 *\x1e/vpc/v1/addresses/{address_id}\xb2\xd2*.\n\x15\x44\x65leteAddressMetadata\x12\x15google.protobuf.Empty\x12\xaa\x01\n\x0eListOperations\x12\x31.yandex.cloud.vpc.v1.ListAddressOperationsRequest\x1a\x32.yandex.cloud.vpc.v1.ListAddressOperationsResponse\"1\x82\xd3\xe4\x93\x02+\x12)/vpc/v1/addresses/{address_id}/operations\x12\xa4\x01\n\x04Move\x12\'.yandex.cloud.vpc.v1.MoveAddressRequest\x1a!.yandex.cloud.operation.Operation\"P\x82\xd3\xe4\x93\x02(\"#/vpc/v1/addresses/{address_id}:move:\x01*\xb2\xd2*\x1e\n\x13MoveAddressMetadata\x12\x07\x41\x64\x64ressBV\n\x17yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpcb\x06proto3')



_GETADDRESSREQUEST = DESCRIPTOR.message_types_by_name['GetAddressRequest']
_GETADDRESSBYVALUEREQUEST = DESCRIPTOR.message_types_by_name['GetAddressByValueRequest']
_LISTADDRESSESREQUEST = DESCRIPTOR.message_types_by_name['ListAddressesRequest']
_LISTADDRESSESRESPONSE = DESCRIPTOR.message_types_by_name['ListAddressesResponse']
_CREATEADDRESSREQUEST = DESCRIPTOR.message_types_by_name['CreateAddressRequest']
_CREATEADDRESSREQUEST_LABELSENTRY = _CREATEADDRESSREQUEST.nested_types_by_name['LabelsEntry']
_EXTERNALIPV4ADDRESSSPEC = DESCRIPTOR.message_types_by_name['ExternalIpv4AddressSpec']
_CREATEADDRESSMETADATA = DESCRIPTOR.message_types_by_name['CreateAddressMetadata']
_UPDATEADDRESSREQUEST = DESCRIPTOR.message_types_by_name['UpdateAddressRequest']
_UPDATEADDRESSREQUEST_LABELSENTRY = _UPDATEADDRESSREQUEST.nested_types_by_name['LabelsEntry']
_UPDATEADDRESSMETADATA = DESCRIPTOR.message_types_by_name['UpdateAddressMetadata']
_DELETEADDRESSREQUEST = DESCRIPTOR.message_types_by_name['DeleteAddressRequest']
_DELETEADDRESSMETADATA = DESCRIPTOR.message_types_by_name['DeleteAddressMetadata']
_LISTADDRESSOPERATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListAddressOperationsRequest']
_LISTADDRESSOPERATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListAddressOperationsResponse']
_MOVEADDRESSREQUEST = DESCRIPTOR.message_types_by_name['MoveAddressRequest']
_MOVEADDRESSMETADATA = DESCRIPTOR.message_types_by_name['MoveAddressMetadata']
GetAddressRequest = _reflection.GeneratedProtocolMessageType('GetAddressRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETADDRESSREQUEST,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.GetAddressRequest)
  })
_sym_db.RegisterMessage(GetAddressRequest)

GetAddressByValueRequest = _reflection.GeneratedProtocolMessageType('GetAddressByValueRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETADDRESSBYVALUEREQUEST,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.GetAddressByValueRequest)
  })
_sym_db.RegisterMessage(GetAddressByValueRequest)

ListAddressesRequest = _reflection.GeneratedProtocolMessageType('ListAddressesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTADDRESSESREQUEST,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.ListAddressesRequest)
  })
_sym_db.RegisterMessage(ListAddressesRequest)

ListAddressesResponse = _reflection.GeneratedProtocolMessageType('ListAddressesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTADDRESSESRESPONSE,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.ListAddressesResponse)
  })
_sym_db.RegisterMessage(ListAddressesResponse)

CreateAddressRequest = _reflection.GeneratedProtocolMessageType('CreateAddressRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATEADDRESSREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.CreateAddressRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CREATEADDRESSREQUEST,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.CreateAddressRequest)
  })
_sym_db.RegisterMessage(CreateAddressRequest)
_sym_db.RegisterMessage(CreateAddressRequest.LabelsEntry)

ExternalIpv4AddressSpec = _reflection.GeneratedProtocolMessageType('ExternalIpv4AddressSpec', (_message.Message,), {
  'DESCRIPTOR' : _EXTERNALIPV4ADDRESSSPEC,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.ExternalIpv4AddressSpec)
  })
_sym_db.RegisterMessage(ExternalIpv4AddressSpec)

CreateAddressMetadata = _reflection.GeneratedProtocolMessageType('CreateAddressMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEADDRESSMETADATA,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.CreateAddressMetadata)
  })
_sym_db.RegisterMessage(CreateAddressMetadata)

UpdateAddressRequest = _reflection.GeneratedProtocolMessageType('UpdateAddressRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEADDRESSREQUEST_LABELSENTRY,
    '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.UpdateAddressRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATEADDRESSREQUEST,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.UpdateAddressRequest)
  })
_sym_db.RegisterMessage(UpdateAddressRequest)
_sym_db.RegisterMessage(UpdateAddressRequest.LabelsEntry)

UpdateAddressMetadata = _reflection.GeneratedProtocolMessageType('UpdateAddressMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEADDRESSMETADATA,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.UpdateAddressMetadata)
  })
_sym_db.RegisterMessage(UpdateAddressMetadata)

DeleteAddressRequest = _reflection.GeneratedProtocolMessageType('DeleteAddressRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEADDRESSREQUEST,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.DeleteAddressRequest)
  })
_sym_db.RegisterMessage(DeleteAddressRequest)

DeleteAddressMetadata = _reflection.GeneratedProtocolMessageType('DeleteAddressMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEADDRESSMETADATA,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.DeleteAddressMetadata)
  })
_sym_db.RegisterMessage(DeleteAddressMetadata)

ListAddressOperationsRequest = _reflection.GeneratedProtocolMessageType('ListAddressOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTADDRESSOPERATIONSREQUEST,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.ListAddressOperationsRequest)
  })
_sym_db.RegisterMessage(ListAddressOperationsRequest)

ListAddressOperationsResponse = _reflection.GeneratedProtocolMessageType('ListAddressOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTADDRESSOPERATIONSRESPONSE,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.ListAddressOperationsResponse)
  })
_sym_db.RegisterMessage(ListAddressOperationsResponse)

MoveAddressRequest = _reflection.GeneratedProtocolMessageType('MoveAddressRequest', (_message.Message,), {
  'DESCRIPTOR' : _MOVEADDRESSREQUEST,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.MoveAddressRequest)
  })
_sym_db.RegisterMessage(MoveAddressRequest)

MoveAddressMetadata = _reflection.GeneratedProtocolMessageType('MoveAddressMetadata', (_message.Message,), {
  'DESCRIPTOR' : _MOVEADDRESSMETADATA,
  '__module__' : 'yandex.cloud.vpc.v1.address_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.vpc.v1.MoveAddressMetadata)
  })
_sym_db.RegisterMessage(MoveAddressMetadata)

_ADDRESSSERVICE = DESCRIPTOR.services_by_name['AddressService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027yandex.cloud.api.vpc.v1Z;github.com/yandex-cloud/go-genproto/yandex/cloud/vpc/v1;vpc'
  _GETADDRESSREQUEST.fields_by_name['address_id']._options = None
  _GETADDRESSREQUEST.fields_by_name['address_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTADDRESSESREQUEST.fields_by_name['folder_id']._options = None
  _LISTADDRESSESREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTADDRESSESREQUEST.fields_by_name['page_size']._options = None
  _LISTADDRESSESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTADDRESSESREQUEST.fields_by_name['page_token']._options = None
  _LISTADDRESSESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _CREATEADDRESSREQUEST_LABELSENTRY._options = None
  _CREATEADDRESSREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATEADDRESSREQUEST.fields_by_name['folder_id']._options = None
  _CREATEADDRESSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATEADDRESSREQUEST.fields_by_name['name']._options = None
  _CREATEADDRESSREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _CREATEADDRESSREQUEST.fields_by_name['description']._options = None
  _CREATEADDRESSREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATEADDRESSREQUEST.fields_by_name['labels']._options = None
  _CREATEADDRESSREQUEST.fields_by_name['labels']._serialized_options = b'\202\3101\004<=64\212\3101\004<=63\362\3071\013[-_0-9a-z]*\262\3101\006\032\0041-63\262\3101\022\022\020[a-z][-_0-9a-z]*'
  _UPDATEADDRESSREQUEST_LABELSENTRY._options = None
  _UPDATEADDRESSREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATEADDRESSREQUEST.fields_by_name['address_id']._options = None
  _UPDATEADDRESSREQUEST.fields_by_name['address_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEADDRESSREQUEST.fields_by_name['name']._options = None
  _UPDATEADDRESSREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\035|[a-z][-a-z0-9]{1,61}[a-z0-9]'
  _UPDATEADDRESSREQUEST.fields_by_name['description']._options = None
  _UPDATEADDRESSREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATEADDRESSREQUEST.fields_by_name['labels']._options = None
  _UPDATEADDRESSREQUEST.fields_by_name['labels']._serialized_options = b'\202\3101\004<=64\212\3101\004<=63\362\3071\013[-_0-9a-z]*\262\3101\006\032\0041-63\262\3101\022\022\020[a-z][-_0-9a-z]*'
  _DELETEADDRESSREQUEST.fields_by_name['address_id']._options = None
  _DELETEADDRESSREQUEST.fields_by_name['address_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTADDRESSOPERATIONSREQUEST.fields_by_name['address_id']._options = None
  _LISTADDRESSOPERATIONSREQUEST.fields_by_name['address_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTADDRESSOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTADDRESSOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTADDRESSOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTADDRESSOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _MOVEADDRESSREQUEST.fields_by_name['address_id']._options = None
  _MOVEADDRESSREQUEST.fields_by_name['address_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _MOVEADDRESSREQUEST.fields_by_name['destination_folder_id']._options = None
  _MOVEADDRESSREQUEST.fields_by_name['destination_folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _ADDRESSSERVICE.methods_by_name['Get']._options = None
  _ADDRESSSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002 \022\036/vpc/v1/addresses/{address_id}'
  _ADDRESSSERVICE.methods_by_name['GetByValue']._options = None
  _ADDRESSSERVICE.methods_by_name['GetByValue']._serialized_options = b'\202\323\344\223\002\033\022\031/vpc/v1/addresses:byValue'
  _ADDRESSSERVICE.methods_by_name['List']._options = None
  _ADDRESSSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\023\022\021/vpc/v1/addresses'
  _ADDRESSSERVICE.methods_by_name['Create']._options = None
  _ADDRESSSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\026\"\021/vpc/v1/addresses:\001*\262\322* \n\025CreateAddressMetadata\022\007Address'
  _ADDRESSSERVICE.methods_by_name['Update']._options = None
  _ADDRESSSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002#2\036/vpc/v1/addresses/{address_id}:\001*\262\322* \n\025UpdateAddressMetadata\022\007Address'
  _ADDRESSSERVICE.methods_by_name['Delete']._options = None
  _ADDRESSSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002 *\036/vpc/v1/addresses/{address_id}\262\322*.\n\025DeleteAddressMetadata\022\025google.protobuf.Empty'
  _ADDRESSSERVICE.methods_by_name['ListOperations']._options = None
  _ADDRESSSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002+\022)/vpc/v1/addresses/{address_id}/operations'
  _ADDRESSSERVICE.methods_by_name['Move']._options = None
  _ADDRESSSERVICE.methods_by_name['Move']._serialized_options = b'\202\323\344\223\002(\"#/vpc/v1/addresses/{address_id}:move:\001*\262\322*\036\n\023MoveAddressMetadata\022\007Address'
  _GETADDRESSREQUEST._serialized_start=270
  _GETADDRESSREQUEST._serialized_end=323
  _GETADDRESSBYVALUEREQUEST._serialized_start=325
  _GETADDRESSBYVALUEREQUEST._serialized_end=395
  _LISTADDRESSESREQUEST._serialized_start=398
  _LISTADDRESSESREQUEST._serialized_end=531
  _LISTADDRESSESRESPONSE._serialized_start=533
  _LISTADDRESSESRESPONSE._serialized_end=630
  _CREATEADDRESSREQUEST._serialized_start=633
  _CREATEADDRESSREQUEST._serialized_end=1053
  _CREATEADDRESSREQUEST_LABELSENTRY._serialized_start=992
  _CREATEADDRESSREQUEST_LABELSENTRY._serialized_end=1037
  _EXTERNALIPV4ADDRESSSPEC._serialized_start=1055
  _EXTERNALIPV4ADDRESSSPEC._serialized_end=1178
  _CREATEADDRESSMETADATA._serialized_start=1180
  _CREATEADDRESSMETADATA._serialized_end=1223
  _UPDATEADDRESSREQUEST._serialized_start=1226
  _UPDATEADDRESSREQUEST._serialized_end=1614
  _UPDATEADDRESSREQUEST_LABELSENTRY._serialized_start=992
  _UPDATEADDRESSREQUEST_LABELSENTRY._serialized_end=1037
  _UPDATEADDRESSMETADATA._serialized_start=1616
  _UPDATEADDRESSMETADATA._serialized_end=1659
  _DELETEADDRESSREQUEST._serialized_start=1661
  _DELETEADDRESSREQUEST._serialized_end=1717
  _DELETEADDRESSMETADATA._serialized_start=1719
  _DELETEADDRESSMETADATA._serialized_end=1762
  _LISTADDRESSOPERATIONSREQUEST._serialized_start=1764
  _LISTADDRESSOPERATIONSREQUEST._serialized_end=1890
  _LISTADDRESSOPERATIONSRESPONSE._serialized_start=1892
  _LISTADDRESSOPERATIONSRESPONSE._serialized_end=2003
  _MOVEADDRESSREQUEST._serialized_start=2005
  _MOVEADDRESSREQUEST._serialized_end=2104
  _MOVEADDRESSMETADATA._serialized_start=2106
  _MOVEADDRESSMETADATA._serialized_end=2147
  _ADDRESSSERVICE._serialized_start=2150
  _ADDRESSSERVICE._serialized_end=3373
# @@protoc_insertion_point(module_scope)
