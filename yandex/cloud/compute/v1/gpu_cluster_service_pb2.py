# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/gpu_cluster_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.compute.v1 import instance_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_instance__pb2
from yandex.cloud.compute.v1 import gpu_cluster_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_gpu__cluster__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1yandex/cloud/compute/v1/gpu_cluster_service.proto\x12\x17yandex.cloud.compute.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/compute/v1/instance.proto\x1a)yandex/cloud/compute/v1/gpu_cluster.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\".\n\x14GetGpuClusterRequest\x12\x16\n\x0egpu_cluster_id\x18\x01 \x01(\t\"\xb0\x01\n\x16ListGpuClustersRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1b\n\x08order_by\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=100\"m\n\x17ListGpuClustersResponse\x12\x39\n\x0cgpu_clusters\x18\x01 \x03(\x0b\x32#.yandex.cloud.compute.v1.GpuCluster\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xa6\x02\n\x17\x43reateGpuClusterRequest\x12\x11\n\tfolder_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12L\n\x06labels\x18\x04 \x03(\x0b\x32<.yandex.cloud.compute.v1.CreateGpuClusterRequest.LabelsEntry\x12\x0f\n\x07zone_id\x18\x05 \x01(\t\x12G\n\x11interconnect_type\x18\x06 \x01(\x0e\x32,.yandex.cloud.compute.v1.GpuInterconnectType\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"2\n\x18\x43reateGpuClusterMetadata\x12\x16\n\x0egpu_cluster_id\x18\x01 \x01(\t\"\x82\x02\n\x17UpdateGpuClusterRequest\x12\x16\n\x0egpu_cluster_id\x18\x01 \x01(\t\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12L\n\x06labels\x18\x05 \x03(\x0b\x32<.yandex.cloud.compute.v1.UpdateGpuClusterRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"2\n\x18UpdateGpuClusterMetadata\x12\x16\n\x0egpu_cluster_id\x18\x01 \x01(\t\"1\n\x17\x44\x65leteGpuClusterRequest\x12\x16\n\x0egpu_cluster_id\x18\x01 \x01(\t\"2\n\x18\x44\x65leteGpuClusterMetadata\x12\x16\n\x0egpu_cluster_id\x18\x01 \x01(\t\"`\n\x1fListGpuClusterOperationsRequest\x12\x16\n\x0egpu_cluster_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\"r\n ListGpuClusterOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"o\n\x1eListGpuClusterInstancesRequest\x12\x16\n\x0egpu_cluster_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x03\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\"p\n\x1fListGpuClusterInstancesResponse\x12\x34\n\tinstances\x18\x01 \x03(\x0b\x32!.yandex.cloud.compute.v1.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xe8\t\n\x11GpuClusterService\x12\x8b\x01\n\x03Get\x12-.yandex.cloud.compute.v1.GetGpuClusterRequest\x1a#.yandex.cloud.compute.v1.GpuCluster\"0\x82\xd3\xe4\x93\x02*\x12(/compute/v1/gpuClusters/{gpu_cluster_id}\x12\x8a\x01\n\x04List\x12/.yandex.cloud.compute.v1.ListGpuClustersRequest\x1a\x30.yandex.cloud.compute.v1.ListGpuClustersResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/compute/v1/gpuClusters\x12\xab\x01\n\x06\x43reate\x12\x30.yandex.cloud.compute.v1.CreateGpuClusterRequest\x1a!.yandex.cloud.operation.Operation\"L\xb2\xd2*&\n\x18\x43reateGpuClusterMetadata\x12\nGpuCluster\x82\xd3\xe4\x93\x02\x1c\"\x17/compute/v1/gpuClusters:\x01*\x12\xbc\x01\n\x06Update\x12\x30.yandex.cloud.compute.v1.UpdateGpuClusterRequest\x1a!.yandex.cloud.operation.Operation\"]\xb2\xd2*&\n\x18UpdateGpuClusterMetadata\x12\nGpuCluster\x82\xd3\xe4\x93\x02-2(/compute/v1/gpuClusters/{gpu_cluster_id}:\x01*\x12\xc4\x01\n\x06\x44\x65lete\x12\x30.yandex.cloud.compute.v1.DeleteGpuClusterRequest\x1a!.yandex.cloud.operation.Operation\"e\xb2\xd2*1\n\x18\x44\x65leteGpuClusterMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02**(/compute/v1/gpuClusters/{gpu_cluster_id}\x12\xc2\x01\n\x0eListOperations\x12\x38.yandex.cloud.compute.v1.ListGpuClusterOperationsRequest\x1a\x39.yandex.cloud.compute.v1.ListGpuClusterOperationsResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/compute/v1/gpuClusters/{gpu_cluster_id}/operations\x12\xbe\x01\n\rListInstances\x12\x37.yandex.cloud.compute.v1.ListGpuClusterInstancesRequest\x1a\x38.yandex.cloud.compute.v1.ListGpuClusterInstancesResponse\":\x82\xd3\xe4\x93\x02\x34\x12\x32/compute/v1/gpuClusters/{gpu_cluster_id}/instancesBb\n\x1byandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;computeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.compute.v1.gpu_cluster_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033yandex.cloud.api.compute.v1ZCgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1;compute'
  _LISTGPUCLUSTERSREQUEST.fields_by_name['folder_id']._options = None
  _LISTGPUCLUSTERSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTGPUCLUSTERSREQUEST.fields_by_name['page_size']._options = None
  _LISTGPUCLUSTERSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTGPUCLUSTERSREQUEST.fields_by_name['page_token']._options = None
  _LISTGPUCLUSTERSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTGPUCLUSTERSREQUEST.fields_by_name['filter']._options = None
  _LISTGPUCLUSTERSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTGPUCLUSTERSREQUEST.fields_by_name['order_by']._options = None
  _LISTGPUCLUSTERSREQUEST.fields_by_name['order_by']._serialized_options = b'\212\3101\005<=100'
  _CREATEGPUCLUSTERREQUEST_LABELSENTRY._options = None
  _CREATEGPUCLUSTERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATEGPUCLUSTERREQUEST_LABELSENTRY._options = None
  _UPDATEGPUCLUSTERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _GPUCLUSTERSERVICE.methods_by_name['Get']._options = None
  _GPUCLUSTERSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002*\022(/compute/v1/gpuClusters/{gpu_cluster_id}'
  _GPUCLUSTERSERVICE.methods_by_name['List']._options = None
  _GPUCLUSTERSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\031\022\027/compute/v1/gpuClusters'
  _GPUCLUSTERSERVICE.methods_by_name['Create']._options = None
  _GPUCLUSTERSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*&\n\030CreateGpuClusterMetadata\022\nGpuCluster\202\323\344\223\002\034\"\027/compute/v1/gpuClusters:\001*'
  _GPUCLUSTERSERVICE.methods_by_name['Update']._options = None
  _GPUCLUSTERSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*&\n\030UpdateGpuClusterMetadata\022\nGpuCluster\202\323\344\223\002-2(/compute/v1/gpuClusters/{gpu_cluster_id}:\001*'
  _GPUCLUSTERSERVICE.methods_by_name['Delete']._options = None
  _GPUCLUSTERSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*1\n\030DeleteGpuClusterMetadata\022\025google.protobuf.Empty\202\323\344\223\002**(/compute/v1/gpuClusters/{gpu_cluster_id}'
  _GPUCLUSTERSERVICE.methods_by_name['ListOperations']._options = None
  _GPUCLUSTERSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0025\0223/compute/v1/gpuClusters/{gpu_cluster_id}/operations'
  _GPUCLUSTERSERVICE.methods_by_name['ListInstances']._options = None
  _GPUCLUSTERSERVICE.methods_by_name['ListInstances']._serialized_options = b'\202\323\344\223\0024\0222/compute/v1/gpuClusters/{gpu_cluster_id}/instances'
  _globals['_GETGPUCLUSTERREQUEST']._serialized_start=330
  _globals['_GETGPUCLUSTERREQUEST']._serialized_end=376
  _globals['_LISTGPUCLUSTERSREQUEST']._serialized_start=379
  _globals['_LISTGPUCLUSTERSREQUEST']._serialized_end=555
  _globals['_LISTGPUCLUSTERSRESPONSE']._serialized_start=557
  _globals['_LISTGPUCLUSTERSRESPONSE']._serialized_end=666
  _globals['_CREATEGPUCLUSTERREQUEST']._serialized_start=669
  _globals['_CREATEGPUCLUSTERREQUEST']._serialized_end=963
  _globals['_CREATEGPUCLUSTERREQUEST_LABELSENTRY']._serialized_start=918
  _globals['_CREATEGPUCLUSTERREQUEST_LABELSENTRY']._serialized_end=963
  _globals['_CREATEGPUCLUSTERMETADATA']._serialized_start=965
  _globals['_CREATEGPUCLUSTERMETADATA']._serialized_end=1015
  _globals['_UPDATEGPUCLUSTERREQUEST']._serialized_start=1018
  _globals['_UPDATEGPUCLUSTERREQUEST']._serialized_end=1276
  _globals['_UPDATEGPUCLUSTERREQUEST_LABELSENTRY']._serialized_start=918
  _globals['_UPDATEGPUCLUSTERREQUEST_LABELSENTRY']._serialized_end=963
  _globals['_UPDATEGPUCLUSTERMETADATA']._serialized_start=1278
  _globals['_UPDATEGPUCLUSTERMETADATA']._serialized_end=1328
  _globals['_DELETEGPUCLUSTERREQUEST']._serialized_start=1330
  _globals['_DELETEGPUCLUSTERREQUEST']._serialized_end=1379
  _globals['_DELETEGPUCLUSTERMETADATA']._serialized_start=1381
  _globals['_DELETEGPUCLUSTERMETADATA']._serialized_end=1431
  _globals['_LISTGPUCLUSTEROPERATIONSREQUEST']._serialized_start=1433
  _globals['_LISTGPUCLUSTEROPERATIONSREQUEST']._serialized_end=1529
  _globals['_LISTGPUCLUSTEROPERATIONSRESPONSE']._serialized_start=1531
  _globals['_LISTGPUCLUSTEROPERATIONSRESPONSE']._serialized_end=1645
  _globals['_LISTGPUCLUSTERINSTANCESREQUEST']._serialized_start=1647
  _globals['_LISTGPUCLUSTERINSTANCESREQUEST']._serialized_end=1758
  _globals['_LISTGPUCLUSTERINSTANCESRESPONSE']._serialized_start=1760
  _globals['_LISTGPUCLUSTERINSTANCESRESPONSE']._serialized_end=1872
  _globals['_GPUCLUSTERSERVICE']._serialized_start=1875
  _globals['_GPUCLUSTERSERVICE']._serialized_end=3131
# @@protoc_insertion_point(module_scope)
