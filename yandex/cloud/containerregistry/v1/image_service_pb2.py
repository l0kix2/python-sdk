# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/containerregistry/v1/image_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.containerregistry.v1 import image_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_image__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5yandex/cloud/containerregistry/v1/image_service.proto\x12!yandex.cloud.containerregistry.v1\x1a yandex/cloud/api/operation.proto\x1a-yandex/cloud/containerregistry/v1/image.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a\x1cgoogle/api/annotations.proto\"\xa4\x02\n\x11ListImagesRequest\x12\x1d\n\x0bregistry_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\\\n\x0frepository_name\x18\x02 \x01(\tBC\xf2\xc7\x31?|[a-z0-9]+(?:[._-][a-z0-9]+)*(/([a-z0-9]+(?:[._-][a-z0-9]+)*))*\x12\x1b\n\tfolder_id\x18\x07 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x03 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x05 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x06 \x01(\tB\t\x8a\xc8\x31\x05<=100\"g\n\x12ListImagesResponse\x12\x38\n\x06images\x18\x01 \x03(\x0b\x32(.yandex.cloud.containerregistry.v1.Image\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"1\n\x0fGetImageRequest\x12\x1e\n\x08image_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"4\n\x12\x44\x65leteImageRequest\x12\x1e\n\x08image_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\'\n\x13\x44\x65leteImageMetadata\x12\x10\n\x08image_id\x18\x01 \x01(\t2\x8a\x04\n\x0cImageService\x12\x9a\x01\n\x04List\x12\x34.yandex.cloud.containerregistry.v1.ListImagesRequest\x1a\x35.yandex.cloud.containerregistry.v1.ListImagesResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/container-registry/v1/images\x12\x95\x01\n\x03Get\x12\x32.yandex.cloud.containerregistry.v1.GetImageRequest\x1a(.yandex.cloud.containerregistry.v1.Image\"0\x82\xd3\xe4\x93\x02*\x12(/container-registry/v1/images/{image_id}\x12\xc4\x01\n\x06\x44\x65lete\x12\x35.yandex.cloud.containerregistry.v1.DeleteImageRequest\x1a!.yandex.cloud.operation.Operation\"`\x82\xd3\xe4\x93\x02**(/container-registry/v1/images/{image_id}\xb2\xd2*,\n\x13\x44\x65leteImageMetadata\x12\x15google.protobuf.EmptyB\x80\x01\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistryb\x06proto3')



_LISTIMAGESREQUEST = DESCRIPTOR.message_types_by_name['ListImagesRequest']
_LISTIMAGESRESPONSE = DESCRIPTOR.message_types_by_name['ListImagesResponse']
_GETIMAGEREQUEST = DESCRIPTOR.message_types_by_name['GetImageRequest']
_DELETEIMAGEREQUEST = DESCRIPTOR.message_types_by_name['DeleteImageRequest']
_DELETEIMAGEMETADATA = DESCRIPTOR.message_types_by_name['DeleteImageMetadata']
ListImagesRequest = _reflection.GeneratedProtocolMessageType('ListImagesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTIMAGESREQUEST,
  '__module__' : 'yandex.cloud.containerregistry.v1.image_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.ListImagesRequest)
  })
_sym_db.RegisterMessage(ListImagesRequest)

ListImagesResponse = _reflection.GeneratedProtocolMessageType('ListImagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTIMAGESRESPONSE,
  '__module__' : 'yandex.cloud.containerregistry.v1.image_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.ListImagesResponse)
  })
_sym_db.RegisterMessage(ListImagesResponse)

GetImageRequest = _reflection.GeneratedProtocolMessageType('GetImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETIMAGEREQUEST,
  '__module__' : 'yandex.cloud.containerregistry.v1.image_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.GetImageRequest)
  })
_sym_db.RegisterMessage(GetImageRequest)

DeleteImageRequest = _reflection.GeneratedProtocolMessageType('DeleteImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEIMAGEREQUEST,
  '__module__' : 'yandex.cloud.containerregistry.v1.image_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.DeleteImageRequest)
  })
_sym_db.RegisterMessage(DeleteImageRequest)

DeleteImageMetadata = _reflection.GeneratedProtocolMessageType('DeleteImageMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEIMAGEMETADATA,
  '__module__' : 'yandex.cloud.containerregistry.v1.image_service_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.DeleteImageMetadata)
  })
_sym_db.RegisterMessage(DeleteImageMetadata)

_IMAGESERVICE = DESCRIPTOR.services_by_name['ImageService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistry'
  _LISTIMAGESREQUEST.fields_by_name['registry_id']._options = None
  _LISTIMAGESREQUEST.fields_by_name['registry_id']._serialized_options = b'\212\3101\004<=50'
  _LISTIMAGESREQUEST.fields_by_name['repository_name']._options = None
  _LISTIMAGESREQUEST.fields_by_name['repository_name']._serialized_options = b'\362\3071?|[a-z0-9]+(?:[._-][a-z0-9]+)*(/([a-z0-9]+(?:[._-][a-z0-9]+)*))*'
  _LISTIMAGESREQUEST.fields_by_name['folder_id']._options = None
  _LISTIMAGESREQUEST.fields_by_name['folder_id']._serialized_options = b'\212\3101\004<=50'
  _LISTIMAGESREQUEST.fields_by_name['page_size']._options = None
  _LISTIMAGESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTIMAGESREQUEST.fields_by_name['page_token']._options = None
  _LISTIMAGESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTIMAGESREQUEST.fields_by_name['filter']._options = None
  _LISTIMAGESREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTIMAGESREQUEST.fields_by_name['order_by']._options = None
  _LISTIMAGESREQUEST.fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _GETIMAGEREQUEST.fields_by_name['image_id']._options = None
  _GETIMAGEREQUEST.fields_by_name['image_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEIMAGEREQUEST.fields_by_name['image_id']._options = None
  _DELETEIMAGEREQUEST.fields_by_name['image_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _IMAGESERVICE.methods_by_name['List']._options = None
  _IMAGESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\037\022\035/container-registry/v1/images'
  _IMAGESERVICE.methods_by_name['Get']._options = None
  _IMAGESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002*\022(/container-registry/v1/images/{image_id}'
  _IMAGESERVICE.methods_by_name['Delete']._options = None
  _IMAGESERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002**(/container-registry/v1/images/{image_id}\262\322*,\n\023DeleteImageMetadata\022\025google.protobuf.Empty'
  _LISTIMAGESREQUEST._serialized_start=275
  _LISTIMAGESREQUEST._serialized_end=567
  _LISTIMAGESRESPONSE._serialized_start=569
  _LISTIMAGESRESPONSE._serialized_end=672
  _GETIMAGEREQUEST._serialized_start=674
  _GETIMAGEREQUEST._serialized_end=723
  _DELETEIMAGEREQUEST._serialized_start=725
  _DELETEIMAGEREQUEST._serialized_end=777
  _DELETEIMAGEMETADATA._serialized_start=779
  _DELETEIMAGEMETADATA._serialized_end=818
  _IMAGESERVICE._serialized_start=821
  _IMAGESERVICE._serialized_end=1343
# @@protoc_insertion_point(module_scope)
