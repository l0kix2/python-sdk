# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/containerregistry/v1/image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud.containerregistry.v1 import blob_pb2 as yandex_dot_cloud_dot_containerregistry_dot_v1_dot_blob__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-yandex/cloud/containerregistry/v1/image.proto\x12!yandex.cloud.containerregistry.v1\x1a,yandex/cloud/containerregistry/v1/blob.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfa\x01\n\x05Image\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x64igest\x18\x03 \x01(\t\x12\x17\n\x0f\x63ompressed_size\x18\x04 \x01(\x03\x12\x37\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\'.yandex.cloud.containerregistry.v1.Blob\x12\x37\n\x06layers\x18\x06 \x03(\x0b\x32\'.yandex.cloud.containerregistry.v1.Blob\x12\x0c\n\x04tags\x18\x07 \x03(\t\x12.\n\ncreated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x80\x01\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistryb\x06proto3')



_IMAGE = DESCRIPTOR.message_types_by_name['Image']
Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'yandex.cloud.containerregistry.v1.image_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.containerregistry.v1.Image)
  })
_sym_db.RegisterMessage(Image)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%yandex.cloud.api.containerregistry.v1ZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/containerregistry/v1;containerregistry'
  _IMAGE._serialized_start=164
  _IMAGE._serialized_end=414
# @@protoc_insertion_point(module_scope)
