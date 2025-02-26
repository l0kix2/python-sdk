# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/greenplum/v1/cluster_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.mdb.greenplum.v1 import cluster_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_cluster__pb2
from yandex.cloud.mdb.greenplum.v1 import maintenance_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_maintenance__pb2
from yandex.cloud.mdb.greenplum.v1 import config_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_config__pb2
from yandex.cloud.mdb.greenplum.v1 import host_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_host__pb2
from yandex.cloud.mdb.greenplum.v1 import backup_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_backup__pb2
from yandex.cloud.mdb.greenplum.v1 import pxf_pb2 as yandex_dot_cloud_dot_mdb_dot_greenplum_dot_v1_dot_pxf__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3yandex/cloud/mdb/greenplum/v1/cluster_service.proto\x12\x1dyandex.cloud.mdb.greenplum.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a+yandex/cloud/mdb/greenplum/v1/cluster.proto\x1a/yandex/cloud/mdb/greenplum/v1/maintenance.proto\x1a*yandex/cloud/mdb/greenplum/v1/config.proto\x1a(yandex/cloud/mdb/greenplum/v1/host.proto\x1a*yandex/cloud/mdb/greenplum/v1/backup.proto\x1a\'yandex/cloud/mdb/greenplum/v1/pxf.proto\"5\n\x11GetClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\x90\x01\n\x13ListClustersRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"i\n\x14ListClustersResponse\x12\x38\n\x08\x63lusters\x18\x01 \x03(\x0b\x32&.yandex.cloud.mdb.greenplum.v1.Cluster\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xcc\x08\n\x14\x43reateClusterRequest\x12\x1f\n\tfolder_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12,\n\x04name\x18\x02 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8c\x01\n\x06labels\x18\x04 \x03(\x0b\x32?.yandex.cloud.mdb.greenplum.v1.CreateClusterRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04<=63\x12M\n\x0b\x65nvironment\x18\x05 \x01(\x0e\x32\x32.yandex.cloud.mdb.greenplum.v1.Cluster.EnvironmentB\x04\xe8\xc7\x31\x01\x12>\n\x06\x63onfig\x18\x06 \x01(\x0b\x32..yandex.cloud.mdb.greenplum.v1.GreenplumConfig\x12P\n\rmaster_config\x18\x07 \x01(\x0b\x32\x39.yandex.cloud.mdb.greenplum.v1.MasterSubclusterConfigSpec\x12R\n\x0esegment_config\x18\x08 \x01(\x0b\x32:.yandex.cloud.mdb.greenplum.v1.SegmentSubclusterConfigSpec\x12\x19\n\x11master_host_count\x18\t \x01(\x03\x12\x17\n\x0fsegment_in_host\x18\n \x01(\x03\x12\x1a\n\x12segment_host_count\x18\x0b \x01(\x03\x12\x17\n\tuser_name\x18\x0c \x01(\tB\x04\xe8\xc7\x31\x01\x12$\n\ruser_password\x18\r \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x38-128\x12 \n\nnetwork_id\x18\x0e \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1a\n\x12security_group_ids\x18\x0f \x03(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x10 \x01(\x08\x12\x16\n\x0ehost_group_ids\x18\x11 \x03(\t\x12L\n\x12maintenance_window\x18\x13 \x01(\x0b\x32\x30.yandex.cloud.mdb.greenplum.v1.MaintenanceWindow\x12>\n\x0b\x63onfig_spec\x18\x14 \x01(\x0b\x32).yandex.cloud.mdb.greenplum.v1.ConfigSpec\x12\x42\n\rcloud_storage\x18\x15 \x01(\x0b\x32+.yandex.cloud.mdb.greenplum.v1.CloudStorage\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8b\x06\n\nConfigSpec\x12i\n\x15greenplum_config_6_17\x18\x01 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_17H\x00R\x14greenplumConfig_6_17\x12i\n\x15greenplum_config_6_19\x18\x02 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_19H\x00R\x14greenplumConfig_6_19\x12i\n\x15greenplum_config_6_21\x18\x04 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_21H\x00R\x14greenplumConfig_6_21\x12i\n\x15greenplum_config_6_22\x18\x05 \x01(\x0b\x32\x32.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6_22H\x00R\x14greenplumConfig_6_22\x12`\n\x12greenplum_config_6\x18\t \x01(\x0b\x32/.yandex.cloud.mdb.greenplum.v1.GreenplumConfig6H\x00R\x11greenplumConfig_6\x12\x43\n\x04pool\x18\x03 \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.ConnectionPoolerConfig\x12X\n\x15\x62\x61\x63kground_activities\x18\x06 \x01(\x0b\x32\x39.yandex.cloud.mdb.greenplum.v1.BackgroundActivitiesConfig\x12<\n\npxf_config\x18\x08 \x01(\x0b\x32(.yandex.cloud.mdb.greenplum.v1.PXFConfigB\x12\n\x10greenplum_config\"+\n\x15\x43reateClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"\x88\x07\n\x14UpdateClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8c\x01\n\x06labels\x18\x04 \x03(\x0b\x32?.yandex.cloud.mdb.greenplum.v1.UpdateClusterRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04<=63\x12(\n\x04name\x18\x05 \x01(\tB\x1a\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x12>\n\x06\x63onfig\x18\x06 \x01(\x0b\x32..yandex.cloud.mdb.greenplum.v1.GreenplumConfig\x12P\n\rmaster_config\x18\x07 \x01(\x0b\x32\x39.yandex.cloud.mdb.greenplum.v1.MasterSubclusterConfigSpec\x12R\n\x0esegment_config\x18\x08 \x01(\x0b\x32:.yandex.cloud.mdb.greenplum.v1.SegmentSubclusterConfigSpec\x12$\n\ruser_password\x18\r \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x38-128\x12L\n\x12maintenance_window\x18\x0f \x01(\x0b\x32\x30.yandex.cloud.mdb.greenplum.v1.MaintenanceWindow\x12\x1a\n\x12security_group_ids\x18\x11 \x03(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x12 \x01(\x08\x12>\n\x0b\x63onfig_spec\x18\x13 \x01(\x0b\x32).yandex.cloud.mdb.greenplum.v1.ConfigSpec\x12\x42\n\rcloud_storage\x18\x14 \x01(\x0b\x32+.yandex.cloud.mdb.greenplum.v1.CloudStorage\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x15UpdateClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"-\n\x17\x41\x64\x64\x43lusterHostsMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"\x84\x01\n\rExpandRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1a\n\x12segment_host_count\x18\x02 \x01(\x03\x12#\n\x1b\x61\x64\x64_segments_per_host_count\x18\x03 \x01(\x03\x12\x10\n\x08\x64uration\x18\x04 \x01(\x03\"8\n\x14\x44\x65leteClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"+\n\x15\x44\x65leteClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"7\n\x13StartClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"*\n\x14StartClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"6\n\x12StopClusterRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\")\n\x13StopClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\"~\n\x1cListClusterOperationsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"o\n\x1dListClusterOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"y\n\x17ListClusterHostsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"g\n\x18ListClusterHostsResponse\x12\x32\n\x05hosts\x18\x01 \x03(\x0b\x32#.yandex.cloud.mdb.greenplum.v1.Host\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"Y\n\x1aMasterSubclusterConfigSpec\x12;\n\tresources\x18\x01 \x01(\x0b\x32(.yandex.cloud.mdb.greenplum.v1.Resources\"Z\n\x1bSegmentSubclusterConfigSpec\x12;\n\tresources\x18\x01 \x01(\x0b\x32(.yandex.cloud.mdb.greenplum.v1.Resources\"j\n\x17ListClusterLogsResponse\x12\x36\n\x04logs\x18\x01 \x03(\x0b\x32(.yandex.cloud.mdb.greenplum.v1.LogRecord\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xb2\x01\n\tLogRecord\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x46\n\x07message\x18\x02 \x03(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.LogRecord.MessageEntry\x1a.\n\x0cMessageEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe5\x03\n\x16ListClusterLogsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x15\n\rcolumn_filter\x18\x02 \x03(\t\x12W\n\x0cservice_type\x18\x03 \x01(\x0e\x32\x41.yandex.cloud.mdb.greenplum.v1.ListClusterLogsRequest.ServiceType\x12-\n\tfrom_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07to_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1d\n\tpage_size\x18\x06 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x07 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1e\n\x16\x61lways_next_page_token\x18\x08 \x01(\x08\x12\x1a\n\x06\x66ilter\x18\t \x01(\tB\n\x8a\xc8\x31\x06<=1000\"c\n\x0bServiceType\x12\x1c\n\x18SERVICE_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tGREENPLUM\x10\x01\x12\x14\n\x10GREENPLUM_POOLER\x10\x02\x12\x11\n\rGREENPLUM_PXF\x10\x03\"{\n\x19ListClusterBackupsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"f\n\x0fStreamLogRecord\x12\x38\n\x06record\x18\x01 \x01(\x0b\x32(.yandex.cloud.mdb.greenplum.v1.LogRecord\x12\x19\n\x11next_record_token\x18\x02 \x01(\t\"\xac\x03\n\x18StreamClusterLogsRequest\x12 \n\ncluster_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x15\n\rcolumn_filter\x18\x02 \x03(\t\x12Y\n\x0cservice_type\x18\x03 \x01(\x0e\x32\x43.yandex.cloud.mdb.greenplum.v1.StreamClusterLogsRequest.ServiceType\x12-\n\tfrom_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07to_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1f\n\x0crecord_token\x18\x06 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x07 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"c\n\x0bServiceType\x12\x1c\n\x18SERVICE_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tGREENPLUM\x10\x01\x12\x14\n\x10GREENPLUM_POOLER\x10\x02\x12\x11\n\rGREENPLUM_PXF\x10\x03\"m\n\x1aListClusterBackupsResponse\x12\x36\n\x07\x62\x61\x63kups\x18\x01 \x03(\x0b\x32%.yandex.cloud.mdb.greenplum.v1.Backup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xb9\x07\n\x15RestoreClusterRequest\x12\x17\n\tbackup_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12(\n\x04time\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1f\n\tfolder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12,\n\x04name\x18\x03 \x01(\tB\x1e\xe8\xc7\x31\x01\xf2\xc7\x31\x0e[a-zA-Z0-9_-]*\x8a\xc8\x31\x04<=63\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x8d\x01\n\x06labels\x18\x05 \x03(\x0b\x32@.yandex.cloud.mdb.greenplum.v1.RestoreClusterRequest.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04<=63\x12M\n\x0b\x65nvironment\x18\x06 \x01(\x0e\x32\x32.yandex.cloud.mdb.greenplum.v1.Cluster.EnvironmentB\x04\xe8\xc7\x31\x01\x12\x45\n\x06\x63onfig\x18\x07 \x01(\x0b\x32\x35.yandex.cloud.mdb.greenplum.v1.GreenplumRestoreConfig\x12\x42\n\x10master_resources\x18\x08 \x01(\x0b\x32(.yandex.cloud.mdb.greenplum.v1.Resources\x12\x43\n\x11segment_resources\x18\t \x01(\x0b\x32(.yandex.cloud.mdb.greenplum.v1.Resources\x12 \n\nnetwork_id\x18\n \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1a\n\x12security_group_ids\x18\x0b \x03(\t\x12\x1b\n\x13\x64\x65letion_protection\x18\x0c \x01(\x08\x12\x16\n\x0ehost_group_ids\x18\r \x03(\t\x12\x1a\n\x12placement_group_id\x18\x0e \x01(\t\x12L\n\x12maintenance_window\x18\x0f \x01(\x0b\x32\x30.yandex.cloud.mdb.greenplum.v1.MaintenanceWindow\x12\x1a\n\x12segment_host_count\x18\x11 \x01(\x03\x12\x17\n\x0fsegment_in_host\x18\x12 \x01(\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"?\n\x16RestoreClusterMetadata\x12\x12\n\ncluster_id\x18\x01 \x01(\t\x12\x11\n\tbackup_id\x18\x02 \x01(\t2\x85\x16\n\x0e\x43lusterService\x12\x94\x01\n\x03Get\x12\x30.yandex.cloud.mdb.greenplum.v1.GetClusterRequest\x1a&.yandex.cloud.mdb.greenplum.v1.Cluster\"3\x82\xd3\xe4\x93\x02-\x12+/managed-greenplum/v1/clusters/{cluster_id}\x12\x97\x01\n\x04List\x12\x32.yandex.cloud.mdb.greenplum.v1.ListClustersRequest\x1a\x33.yandex.cloud.mdb.greenplum.v1.ListClustersResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/managed-greenplum/v1/clusters\x12\xaf\x01\n\x06\x43reate\x12\x33.yandex.cloud.mdb.greenplum.v1.CreateClusterRequest\x1a!.yandex.cloud.operation.Operation\"M\xb2\xd2* \n\x15\x43reateClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02#\"\x1e/managed-greenplum/v1/clusters:\x01*\x12\xbc\x01\n\x06Update\x12\x33.yandex.cloud.mdb.greenplum.v1.UpdateClusterRequest\x1a!.yandex.cloud.operation.Operation\"Z\xb2\xd2* \n\x15UpdateClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x30\x32+/managed-greenplum/v1/clusters/{cluster_id}:\x01*\x12\xbe\x01\n\x06\x45xpand\x12,.yandex.cloud.mdb.greenplum.v1.ExpandRequest\x1a!.yandex.cloud.operation.Operation\"c\xb2\xd2*\"\n\x17\x41\x64\x64\x43lusterHostsMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x37\"2/managed-greenplum/v1/clusters/{cluster_id}/expand:\x01*\x12\xc7\x01\n\x06\x44\x65lete\x12\x33.yandex.cloud.mdb.greenplum.v1.DeleteClusterRequest\x1a!.yandex.cloud.operation.Operation\"e\xb2\xd2*.\n\x15\x44\x65leteClusterMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02-*+/managed-greenplum/v1/clusters/{cluster_id}\x12\xbc\x01\n\x05Start\x12\x32.yandex.cloud.mdb.greenplum.v1.StartClusterRequest\x1a!.yandex.cloud.operation.Operation\"\\\xb2\xd2*\x1f\n\x14StartClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x33\"1/managed-greenplum/v1/clusters/{cluster_id}:start\x12\xb8\x01\n\x04Stop\x12\x31.yandex.cloud.mdb.greenplum.v1.StopClusterRequest\x1a!.yandex.cloud.operation.Operation\"Z\xb2\xd2*\x1e\n\x13StopClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02\x32\"0/managed-greenplum/v1/clusters/{cluster_id}:stop\x12\xcb\x01\n\x0eListOperations\x12;.yandex.cloud.mdb.greenplum.v1.ListClusterOperationsRequest\x1a<.yandex.cloud.mdb.greenplum.v1.ListClusterOperationsResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/managed-greenplum/v1/clusters/{cluster_id}/operations\x12\xc4\x01\n\x0fListMasterHosts\x12\x36.yandex.cloud.mdb.greenplum.v1.ListClusterHostsRequest\x1a\x37.yandex.cloud.mdb.greenplum.v1.ListClusterHostsResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/managed-greenplum/v1/clusters/{cluster_id}/master-hosts\x12\xc6\x01\n\x10ListSegmentHosts\x12\x36.yandex.cloud.mdb.greenplum.v1.ListClusterHostsRequest\x1a\x37.yandex.cloud.mdb.greenplum.v1.ListClusterHostsResponse\"A\x82\xd3\xe4\x93\x02;\x12\x39/managed-greenplum/v1/clusters/{cluster_id}/segment-hosts\x12\xb3\x01\n\x08ListLogs\x12\x35.yandex.cloud.mdb.greenplum.v1.ListClusterLogsRequest\x1a\x36.yandex.cloud.mdb.greenplum.v1.ListClusterLogsResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/managed-greenplum/v1/clusters/{cluster_id}:logs\x12\xb8\x01\n\nStreamLogs\x12\x37.yandex.cloud.mdb.greenplum.v1.StreamClusterLogsRequest\x1a..yandex.cloud.mdb.greenplum.v1.StreamLogRecord\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/managed-greenplum/v1/clusters/{cluster_id}:stream_logs0\x01\x12\xbf\x01\n\x0bListBackups\x12\x38.yandex.cloud.mdb.greenplum.v1.ListClusterBackupsRequest\x1a\x39.yandex.cloud.mdb.greenplum.v1.ListClusterBackupsResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/managed-greenplum/v1/clusters/{cluster_id}/backups\x12\xba\x01\n\x07Restore\x12\x34.yandex.cloud.mdb.greenplum.v1.RestoreClusterRequest\x1a!.yandex.cloud.operation.Operation\"V\xb2\xd2*!\n\x16RestoreClusterMetadata\x12\x07\x43luster\x82\xd3\xe4\x93\x02+\"&/managed-greenplum/v1/clusters:restore:\x01*Bp\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplumb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.mdb.greenplum.v1.cluster_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!yandex.cloud.api.mdb.greenplum.v1ZKgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/greenplum/v1;greenplum'
  _GETCLUSTERREQUEST.fields_by_name['cluster_id']._options = None
  _GETCLUSTERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTCLUSTERSREQUEST.fields_by_name['folder_id']._options = None
  _LISTCLUSTERSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTCLUSTERSREQUEST.fields_by_name['page_size']._options = None
  _LISTCLUSTERSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTCLUSTERSREQUEST.fields_by_name['page_token']._options = None
  _LISTCLUSTERSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTCLUSTERSREQUEST.fields_by_name['filter']._options = None
  _LISTCLUSTERSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _CREATECLUSTERREQUEST_LABELSENTRY._options = None
  _CREATECLUSTERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATECLUSTERREQUEST.fields_by_name['folder_id']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATECLUSTERREQUEST.fields_by_name['name']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _CREATECLUSTERREQUEST.fields_by_name['description']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATECLUSTERREQUEST.fields_by_name['labels']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\004<=63'
  _CREATECLUSTERREQUEST.fields_by_name['environment']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['environment']._serialized_options = b'\350\3071\001'
  _CREATECLUSTERREQUEST.fields_by_name['user_name']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['user_name']._serialized_options = b'\350\3071\001'
  _CREATECLUSTERREQUEST.fields_by_name['user_password']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['user_password']._serialized_options = b'\350\3071\001\212\3101\0058-128'
  _CREATECLUSTERREQUEST.fields_by_name['network_id']._options = None
  _CREATECLUSTERREQUEST.fields_by_name['network_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATECLUSTERREQUEST_LABELSENTRY._options = None
  _UPDATECLUSTERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATECLUSTERREQUEST.fields_by_name['cluster_id']._options = None
  _UPDATECLUSTERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATECLUSTERREQUEST.fields_by_name['description']._options = None
  _UPDATECLUSTERREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATECLUSTERREQUEST.fields_by_name['labels']._options = None
  _UPDATECLUSTERREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\004<=63'
  _UPDATECLUSTERREQUEST.fields_by_name['name']._options = None
  _UPDATECLUSTERREQUEST.fields_by_name['name']._serialized_options = b'\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _UPDATECLUSTERREQUEST.fields_by_name['user_password']._options = None
  _UPDATECLUSTERREQUEST.fields_by_name['user_password']._serialized_options = b'\350\3071\001\212\3101\0058-128'
  _EXPANDREQUEST.fields_by_name['cluster_id']._options = None
  _EXPANDREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETECLUSTERREQUEST.fields_by_name['cluster_id']._options = None
  _DELETECLUSTERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _STARTCLUSTERREQUEST.fields_by_name['cluster_id']._options = None
  _STARTCLUSTERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _STOPCLUSTERREQUEST.fields_by_name['cluster_id']._options = None
  _STOPCLUSTERREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['cluster_id']._options = None
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTCLUSTEROPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTCLUSTERHOSTSREQUEST.fields_by_name['cluster_id']._options = None
  _LISTCLUSTERHOSTSREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTCLUSTERHOSTSREQUEST.fields_by_name['page_size']._options = None
  _LISTCLUSTERHOSTSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTCLUSTERHOSTSREQUEST.fields_by_name['page_token']._options = None
  _LISTCLUSTERHOSTSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LOGRECORD_MESSAGEENTRY._options = None
  _LOGRECORD_MESSAGEENTRY._serialized_options = b'8\001'
  _LISTCLUSTERLOGSREQUEST.fields_by_name['cluster_id']._options = None
  _LISTCLUSTERLOGSREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTCLUSTERLOGSREQUEST.fields_by_name['page_size']._options = None
  _LISTCLUSTERLOGSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTCLUSTERLOGSREQUEST.fields_by_name['page_token']._options = None
  _LISTCLUSTERLOGSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _LISTCLUSTERLOGSREQUEST.fields_by_name['filter']._options = None
  _LISTCLUSTERLOGSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTCLUSTERBACKUPSREQUEST.fields_by_name['cluster_id']._options = None
  _LISTCLUSTERBACKUPSREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTCLUSTERBACKUPSREQUEST.fields_by_name['page_size']._options = None
  _LISTCLUSTERBACKUPSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTCLUSTERBACKUPSREQUEST.fields_by_name['page_token']._options = None
  _LISTCLUSTERBACKUPSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _STREAMCLUSTERLOGSREQUEST.fields_by_name['cluster_id']._options = None
  _STREAMCLUSTERLOGSREQUEST.fields_by_name['cluster_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _STREAMCLUSTERLOGSREQUEST.fields_by_name['record_token']._options = None
  _STREAMCLUSTERLOGSREQUEST.fields_by_name['record_token']._serialized_options = b'\212\3101\005<=100'
  _STREAMCLUSTERLOGSREQUEST.fields_by_name['filter']._options = None
  _STREAMCLUSTERLOGSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _RESTORECLUSTERREQUEST_LABELSENTRY._options = None
  _RESTORECLUSTERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _RESTORECLUSTERREQUEST.fields_by_name['backup_id']._options = None
  _RESTORECLUSTERREQUEST.fields_by_name['backup_id']._serialized_options = b'\350\3071\001'
  _RESTORECLUSTERREQUEST.fields_by_name['folder_id']._options = None
  _RESTORECLUSTERREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _RESTORECLUSTERREQUEST.fields_by_name['name']._options = None
  _RESTORECLUSTERREQUEST.fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\016[a-zA-Z0-9_-]*\212\3101\004<=63'
  _RESTORECLUSTERREQUEST.fields_by_name['description']._options = None
  _RESTORECLUSTERREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _RESTORECLUSTERREQUEST.fields_by_name['labels']._options = None
  _RESTORECLUSTERREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\004<=63'
  _RESTORECLUSTERREQUEST.fields_by_name['environment']._options = None
  _RESTORECLUSTERREQUEST.fields_by_name['environment']._serialized_options = b'\350\3071\001'
  _RESTORECLUSTERREQUEST.fields_by_name['network_id']._options = None
  _RESTORECLUSTERREQUEST.fields_by_name['network_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CLUSTERSERVICE.methods_by_name['Get']._options = None
  _CLUSTERSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002-\022+/managed-greenplum/v1/clusters/{cluster_id}'
  _CLUSTERSERVICE.methods_by_name['List']._options = None
  _CLUSTERSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002 \022\036/managed-greenplum/v1/clusters'
  _CLUSTERSERVICE.methods_by_name['Create']._options = None
  _CLUSTERSERVICE.methods_by_name['Create']._serialized_options = b'\262\322* \n\025CreateClusterMetadata\022\007Cluster\202\323\344\223\002#\"\036/managed-greenplum/v1/clusters:\001*'
  _CLUSTERSERVICE.methods_by_name['Update']._options = None
  _CLUSTERSERVICE.methods_by_name['Update']._serialized_options = b'\262\322* \n\025UpdateClusterMetadata\022\007Cluster\202\323\344\223\00202+/managed-greenplum/v1/clusters/{cluster_id}:\001*'
  _CLUSTERSERVICE.methods_by_name['Expand']._options = None
  _CLUSTERSERVICE.methods_by_name['Expand']._serialized_options = b'\262\322*\"\n\027AddClusterHostsMetadata\022\007Cluster\202\323\344\223\0027\"2/managed-greenplum/v1/clusters/{cluster_id}/expand:\001*'
  _CLUSTERSERVICE.methods_by_name['Delete']._options = None
  _CLUSTERSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*.\n\025DeleteClusterMetadata\022\025google.protobuf.Empty\202\323\344\223\002-*+/managed-greenplum/v1/clusters/{cluster_id}'
  _CLUSTERSERVICE.methods_by_name['Start']._options = None
  _CLUSTERSERVICE.methods_by_name['Start']._serialized_options = b'\262\322*\037\n\024StartClusterMetadata\022\007Cluster\202\323\344\223\0023\"1/managed-greenplum/v1/clusters/{cluster_id}:start'
  _CLUSTERSERVICE.methods_by_name['Stop']._options = None
  _CLUSTERSERVICE.methods_by_name['Stop']._serialized_options = b'\262\322*\036\n\023StopClusterMetadata\022\007Cluster\202\323\344\223\0022\"0/managed-greenplum/v1/clusters/{cluster_id}:stop'
  _CLUSTERSERVICE.methods_by_name['ListOperations']._options = None
  _CLUSTERSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0028\0226/managed-greenplum/v1/clusters/{cluster_id}/operations'
  _CLUSTERSERVICE.methods_by_name['ListMasterHosts']._options = None
  _CLUSTERSERVICE.methods_by_name['ListMasterHosts']._serialized_options = b'\202\323\344\223\002:\0228/managed-greenplum/v1/clusters/{cluster_id}/master-hosts'
  _CLUSTERSERVICE.methods_by_name['ListSegmentHosts']._options = None
  _CLUSTERSERVICE.methods_by_name['ListSegmentHosts']._serialized_options = b'\202\323\344\223\002;\0229/managed-greenplum/v1/clusters/{cluster_id}/segment-hosts'
  _CLUSTERSERVICE.methods_by_name['ListLogs']._options = None
  _CLUSTERSERVICE.methods_by_name['ListLogs']._serialized_options = b'\202\323\344\223\0022\0220/managed-greenplum/v1/clusters/{cluster_id}:logs'
  _CLUSTERSERVICE.methods_by_name['StreamLogs']._options = None
  _CLUSTERSERVICE.methods_by_name['StreamLogs']._serialized_options = b'\202\323\344\223\0029\0227/managed-greenplum/v1/clusters/{cluster_id}:stream_logs'
  _CLUSTERSERVICE.methods_by_name['ListBackups']._options = None
  _CLUSTERSERVICE.methods_by_name['ListBackups']._serialized_options = b'\202\323\344\223\0025\0223/managed-greenplum/v1/clusters/{cluster_id}/backups'
  _CLUSTERSERVICE.methods_by_name['Restore']._options = None
  _CLUSTERSERVICE.methods_by_name['Restore']._serialized_options = b'\262\322*!\n\026RestoreClusterMetadata\022\007Cluster\202\323\344\223\002+\"&/managed-greenplum/v1/clusters:restore:\001*'
  _globals['_GETCLUSTERREQUEST']._serialized_start=553
  _globals['_GETCLUSTERREQUEST']._serialized_end=606
  _globals['_LISTCLUSTERSREQUEST']._serialized_start=609
  _globals['_LISTCLUSTERSREQUEST']._serialized_end=753
  _globals['_LISTCLUSTERSRESPONSE']._serialized_start=755
  _globals['_LISTCLUSTERSRESPONSE']._serialized_end=860
  _globals['_CREATECLUSTERREQUEST']._serialized_start=863
  _globals['_CREATECLUSTERREQUEST']._serialized_end=1963
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._serialized_start=1918
  _globals['_CREATECLUSTERREQUEST_LABELSENTRY']._serialized_end=1963
  _globals['_CONFIGSPEC']._serialized_start=1966
  _globals['_CONFIGSPEC']._serialized_end=2745
  _globals['_CREATECLUSTERMETADATA']._serialized_start=2747
  _globals['_CREATECLUSTERMETADATA']._serialized_end=2790
  _globals['_UPDATECLUSTERREQUEST']._serialized_start=2793
  _globals['_UPDATECLUSTERREQUEST']._serialized_end=3697
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._serialized_start=1918
  _globals['_UPDATECLUSTERREQUEST_LABELSENTRY']._serialized_end=1963
  _globals['_UPDATECLUSTERMETADATA']._serialized_start=3699
  _globals['_UPDATECLUSTERMETADATA']._serialized_end=3742
  _globals['_ADDCLUSTERHOSTSMETADATA']._serialized_start=3744
  _globals['_ADDCLUSTERHOSTSMETADATA']._serialized_end=3789
  _globals['_EXPANDREQUEST']._serialized_start=3792
  _globals['_EXPANDREQUEST']._serialized_end=3924
  _globals['_DELETECLUSTERREQUEST']._serialized_start=3926
  _globals['_DELETECLUSTERREQUEST']._serialized_end=3982
  _globals['_DELETECLUSTERMETADATA']._serialized_start=3984
  _globals['_DELETECLUSTERMETADATA']._serialized_end=4027
  _globals['_STARTCLUSTERREQUEST']._serialized_start=4029
  _globals['_STARTCLUSTERREQUEST']._serialized_end=4084
  _globals['_STARTCLUSTERMETADATA']._serialized_start=4086
  _globals['_STARTCLUSTERMETADATA']._serialized_end=4128
  _globals['_STOPCLUSTERREQUEST']._serialized_start=4130
  _globals['_STOPCLUSTERREQUEST']._serialized_end=4184
  _globals['_STOPCLUSTERMETADATA']._serialized_start=4186
  _globals['_STOPCLUSTERMETADATA']._serialized_end=4227
  _globals['_LISTCLUSTEROPERATIONSREQUEST']._serialized_start=4229
  _globals['_LISTCLUSTEROPERATIONSREQUEST']._serialized_end=4355
  _globals['_LISTCLUSTEROPERATIONSRESPONSE']._serialized_start=4357
  _globals['_LISTCLUSTEROPERATIONSRESPONSE']._serialized_end=4468
  _globals['_LISTCLUSTERHOSTSREQUEST']._serialized_start=4470
  _globals['_LISTCLUSTERHOSTSREQUEST']._serialized_end=4591
  _globals['_LISTCLUSTERHOSTSRESPONSE']._serialized_start=4593
  _globals['_LISTCLUSTERHOSTSRESPONSE']._serialized_end=4696
  _globals['_MASTERSUBCLUSTERCONFIGSPEC']._serialized_start=4698
  _globals['_MASTERSUBCLUSTERCONFIGSPEC']._serialized_end=4787
  _globals['_SEGMENTSUBCLUSTERCONFIGSPEC']._serialized_start=4789
  _globals['_SEGMENTSUBCLUSTERCONFIGSPEC']._serialized_end=4879
  _globals['_LISTCLUSTERLOGSRESPONSE']._serialized_start=4881
  _globals['_LISTCLUSTERLOGSRESPONSE']._serialized_end=4987
  _globals['_LOGRECORD']._serialized_start=4990
  _globals['_LOGRECORD']._serialized_end=5168
  _globals['_LOGRECORD_MESSAGEENTRY']._serialized_start=5122
  _globals['_LOGRECORD_MESSAGEENTRY']._serialized_end=5168
  _globals['_LISTCLUSTERLOGSREQUEST']._serialized_start=5171
  _globals['_LISTCLUSTERLOGSREQUEST']._serialized_end=5656
  _globals['_LISTCLUSTERLOGSREQUEST_SERVICETYPE']._serialized_start=5557
  _globals['_LISTCLUSTERLOGSREQUEST_SERVICETYPE']._serialized_end=5656
  _globals['_LISTCLUSTERBACKUPSREQUEST']._serialized_start=5658
  _globals['_LISTCLUSTERBACKUPSREQUEST']._serialized_end=5781
  _globals['_STREAMLOGRECORD']._serialized_start=5783
  _globals['_STREAMLOGRECORD']._serialized_end=5885
  _globals['_STREAMCLUSTERLOGSREQUEST']._serialized_start=5888
  _globals['_STREAMCLUSTERLOGSREQUEST']._serialized_end=6316
  _globals['_STREAMCLUSTERLOGSREQUEST_SERVICETYPE']._serialized_start=5557
  _globals['_STREAMCLUSTERLOGSREQUEST_SERVICETYPE']._serialized_end=5656
  _globals['_LISTCLUSTERBACKUPSRESPONSE']._serialized_start=6318
  _globals['_LISTCLUSTERBACKUPSRESPONSE']._serialized_end=6427
  _globals['_RESTORECLUSTERREQUEST']._serialized_start=6430
  _globals['_RESTORECLUSTERREQUEST']._serialized_end=7383
  _globals['_RESTORECLUSTERREQUEST_LABELSENTRY']._serialized_start=1918
  _globals['_RESTORECLUSTERREQUEST_LABELSENTRY']._serialized_end=1963
  _globals['_RESTORECLUSTERMETADATA']._serialized_start=7385
  _globals['_RESTORECLUSTERMETADATA']._serialized_end=7448
  _globals['_CLUSTERSERVICE']._serialized_start=7451
  _globals['_CLUSTERSERVICE']._serialized_end=10272
# @@protoc_insertion_point(module_scope)
