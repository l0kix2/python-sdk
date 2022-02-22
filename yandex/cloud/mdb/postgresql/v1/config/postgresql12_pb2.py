# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/mdb/postgresql/v1/config/postgresql12.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8yandex/cloud/mdb/postgresql/v1/config/postgresql12.proto\x12%yandex.cloud.mdb.postgresql.v1.config\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dyandex/cloud/validation.proto\"\xbeS\n\x12PostgresqlConfig12\x12\x34\n\x0fmax_connections\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x33\n\x0eshared_buffers\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x0ctemp_buffers\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x19max_prepared_transactions\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12-\n\x08work_mem\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x14maintenance_work_mem\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x13\x61utovacuum_work_mem\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x34\n\x0ftemp_file_limit\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x11vacuum_cost_delay\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x14vacuum_cost_page_hit\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12:\n\x15vacuum_cost_page_miss\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16vacuum_cost_page_dirty\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x11vacuum_cost_limit\x18\r \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x41\n\x0e\x62gwriter_delay\x18\x0e \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08\x31\x30-10000\x12:\n\x15\x62gwriter_lru_maxpages\x18\x0f \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12=\n\x17\x62gwriter_lru_multiplier\x18\x10 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x45\n\x14\x62gwriter_flush_after\x18\x11 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x30-2048\x12\x44\n\x13\x62\x61\x63kend_flush_after\x18\x12 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x30-2048\x12L\n\x16old_snapshot_threshold\x18\x13 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0f\xfa\xc7\x31\x0b-1-86400000\x12U\n\twal_level\x18\x14 \x01(\x0e\x32\x42.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.WalLevel\x12g\n\x12synchronous_commit\x18\x15 \x01(\x0e\x32K.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.SynchronousCommit\x12K\n\x12\x63heckpoint_timeout\x18\x16 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x12\xfa\xc7\x31\x0e\x33\x30\x30\x30\x30-86400000\x12\x42\n\x1c\x63heckpoint_completion_target\x18\x17 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12G\n\x16\x63heckpoint_flush_after\x18\x18 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x30-2048\x12\x31\n\x0cmax_wal_size\x18\x19 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x0cmin_wal_size\x18\x1a \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12@\n\x1bmax_standby_streaming_delay\x18\x1b \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x19\x64\x65\x66\x61ult_statistics_target\x18\x1c \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12k\n\x14\x63onstraint_exclusion\x18\x1d \x01(\x0e\x32M.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.ConstraintExclusion\x12;\n\x15\x63ursor_tuple_fraction\x18\x1e \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12J\n\x13\x66rom_collapse_limit\x18\x1f \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x10\xfa\xc7\x31\x0c\x31-2147483647\x12J\n\x13join_collapse_limit\x18  \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x10\xfa\xc7\x31\x0c\x31-2147483647\x12h\n\x13\x66orce_parallel_mode\x18! \x01(\x0e\x32K.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.ForceParallelMode\x12_\n\x13\x63lient_min_messages\x18\" \x01(\x0e\x32\x42.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.LogLevel\x12\\\n\x10log_min_messages\x18# \x01(\x0e\x32\x42.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.LogLevel\x12\x63\n\x17log_min_error_statement\x18$ \x01(\x0e\x32\x42.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.LogLevel\x12?\n\x1alog_min_duration_statement\x18% \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x33\n\x0flog_checkpoints\x18& \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0flog_connections\x18\' \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x36\n\x12log_disconnections\x18( \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\x0clog_duration\x18) \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12h\n\x13log_error_verbosity\x18* \x01(\x0e\x32K.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.LogErrorVerbosity\x12\x32\n\x0elog_lock_waits\x18+ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12]\n\rlog_statement\x18, \x01(\x0e\x32\x46.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.LogStatement\x12\x33\n\x0elog_temp_files\x18- \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x13\n\x0bsearch_path\x18. \x01(\t\x12\x30\n\x0crow_security\x18/ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12u\n\x1d\x64\x65\x66\x61ult_transaction_isolation\x18\x30 \x01(\x0e\x32N.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.TransactionIsolation\x12\x36\n\x11statement_timeout\x18\x31 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x0clock_timeout\x18\x32 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12H\n#idle_in_transaction_session_timeout\x18\x33 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12[\n\x0c\x62ytea_output\x18\x34 \x01(\x0e\x32\x45.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.ByteaOutput\x12V\n\txmlbinary\x18\x35 \x01(\x0e\x32\x43.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.XmlBinary\x12V\n\txmloption\x18\x36 \x01(\x0e\x32\x43.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.XmlOption\x12;\n\x16gin_pending_list_limit\x18\x37 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x35\n\x10\x64\x65\x61\x64lock_timeout\x18\x38 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12>\n\x19max_locks_per_transaction\x18\x39 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x43\n\x1emax_pred_locks_per_transaction\x18: \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12/\n\x0b\x61rray_nulls\x18; \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x61\n\x0f\x62\x61\x63kslash_quote\x18< \x01(\x0e\x32H.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.BackslashQuote\x12\x35\n\x11\x64\x65\x66\x61ult_with_oids\x18= \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x39\n\x15\x65scape_string_warning\x18> \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x14lo_compat_privileges\x18? \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x1boperator_precedence_warning\x18@ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x39\n\x15quote_all_identifiers\x18\x41 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12?\n\x1bstandard_conforming_strings\x18\x42 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x14synchronize_seqscans\x18\x43 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x39\n\x15transform_null_equals\x18\x44 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x31\n\rexit_on_error\x18\x45 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\rseq_page_cost\x18\x46 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x36\n\x10random_page_cost\x18G \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x45\n\x16\x61utovacuum_max_workers\x18H \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x08\xfa\xc7\x31\x04\x31-32\x12M\n\x1c\x61utovacuum_vacuum_cost_delay\x18I \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06-1-100\x12O\n\x1c\x61utovacuum_vacuum_cost_limit\x18J \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0c\xfa\xc7\x31\x08-1-10000\x12J\n\x12\x61utovacuum_naptime\x18K \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x11\xfa\xc7\x31\r1000-86400000\x12H\n\x0f\x61rchive_timeout\x18L \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x12\xfa\xc7\x31\x0e\x31\x30\x30\x30\x30-86400000\x12N\n\x19track_activity_query_size\x18M \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x0e\xfa\xc7\x31\n100-102400\x12\x35\n\x11\x65nable_bitmapscan\x18P \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0e\x65nable_hashagg\x18Q \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0f\x65nable_hashjoin\x18R \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\x10\x65nable_indexscan\x18S \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x14\x65nable_indexonlyscan\x18T \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0f\x65nable_material\x18U \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\x10\x65nable_mergejoin\x18V \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0f\x65nable_nestloop\x18W \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0e\x65nable_seqscan\x18X \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\x0b\x65nable_sort\x18Y \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0e\x65nable_tidscan\x18Z \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x45\n\x14max_worker_processes\x18[ \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x30-1024\x12\x45\n\x14max_parallel_workers\x18\\ \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x30-1024\x12P\n\x1fmax_parallel_workers_per_gather\x18] \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x30-1024\x12Q\n\x1e\x61utovacuum_vacuum_scale_factor\x18^ \x01(\x0b\x32\x1c.google.protobuf.DoubleValueB\x0b\xfa\xc7\x31\x07\x30.0-1.0\x12R\n\x1f\x61utovacuum_analyze_scale_factor\x18_ \x01(\x0b\x32\x1c.google.protobuf.DoubleValueB\x0b\xfa\xc7\x31\x07\x30.0-1.0\x12\x41\n\x1d\x64\x65\x66\x61ult_transaction_read_only\x18` \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x10\n\x08timezone\x18\x61 \x01(\t\x12:\n\x16\x65nable_parallel_append\x18\x62 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x14\x65nable_parallel_hash\x18\x63 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12<\n\x18\x65nable_partition_pruning\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x42\n\x1e\x65nable_partitionwise_aggregate\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12=\n\x19\x65nable_partitionwise_join\x18\x66 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\'\n\x03jit\x18g \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12N\n max_parallel_maintenance_workers\x18h \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\xc7\x31\x03>=0\x12\x41\n\x1dparallel_leader_participation\x18i \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12^\n!vacuum_cleanup_index_scale_factor\x18j \x01(\x0b\x32\x1c.google.protobuf.DoubleValueB\x15\xfa\xc7\x31\x11\x30.0-10000000000.0\x12N\n\x1blog_transaction_sample_rate\x18k \x01(\x0b\x32\x1c.google.protobuf.DoubleValueB\x0b\xfa\xc7\x31\x07\x30.0-1.0\x12`\n\x0fplan_cache_mode\x18l \x01(\x0e\x32G.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.PlanCacheMode\x12I\n\x18\x65\x66\x66\x65\x63tive_io_concurrency\x18m \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\n\xfa\xc7\x31\x06\x30-1000\x12M\n\x14\x65\x66\x66\x65\x63tive_cache_size\x18n \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x12\xfa\xc7\x31\x0e\x30-549755813888\x12r\n\x18shared_preload_libraries\x18o \x03(\x0e\x32P.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.SharedPreloadLibraries\x12U\n\x1d\x61uto_explain_log_min_duration\x18p \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x11\xfa\xc7\x31\r-1-2147483647\x12<\n\x18\x61uto_explain_log_analyze\x18q \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12<\n\x18\x61uto_explain_log_buffers\x18r \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12;\n\x17\x61uto_explain_log_timing\x18s \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12=\n\x19\x61uto_explain_log_triggers\x18t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12<\n\x18\x61uto_explain_log_verbose\x18u \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x46\n\"auto_explain_log_nested_statements\x18v \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12K\n\x18\x61uto_explain_sample_rate\x18w \x01(\x0b\x32\x1c.google.protobuf.DoubleValueB\x0b\xfa\xc7\x31\x07\x30.0-1.0\x12<\n\x18pg_hint_plan_enable_hint\x18x \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x42\n\x1epg_hint_plan_enable_hint_table\x18y \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12p\n\x18pg_hint_plan_debug_print\x18z \x01(\x0e\x32N.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.PgHintPlanDebugPrint\x12\x66\n\x1apg_hint_plan_message_level\x18{ \x01(\x0e\x32\x42.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12.LogLevel\"S\n\x08WalLevel\x12\x19\n\x15WAL_LEVEL_UNSPECIFIED\x10\x00\x12\x15\n\x11WAL_LEVEL_REPLICA\x10\x01\x12\x15\n\x11WAL_LEVEL_LOGICAL\x10\x02\"\xd6\x01\n\x11SynchronousCommit\x12\"\n\x1eSYNCHRONOUS_COMMIT_UNSPECIFIED\x10\x00\x12\x19\n\x15SYNCHRONOUS_COMMIT_ON\x10\x01\x12\x1a\n\x16SYNCHRONOUS_COMMIT_OFF\x10\x02\x12\x1c\n\x18SYNCHRONOUS_COMMIT_LOCAL\x10\x03\x12#\n\x1fSYNCHRONOUS_COMMIT_REMOTE_WRITE\x10\x04\x12#\n\x1fSYNCHRONOUS_COMMIT_REMOTE_APPLY\x10\x05\"\x9a\x01\n\x13\x43onstraintExclusion\x12$\n CONSTRAINT_EXCLUSION_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x43ONSTRAINT_EXCLUSION_ON\x10\x01\x12\x1c\n\x18\x43ONSTRAINT_EXCLUSION_OFF\x10\x02\x12\"\n\x1e\x43ONSTRAINT_EXCLUSION_PARTITION\x10\x03\"\x92\x01\n\x11\x46orceParallelMode\x12#\n\x1f\x46ORCE_PARALLEL_MODE_UNSPECIFIED\x10\x00\x12\x1a\n\x16\x46ORCE_PARALLEL_MODE_ON\x10\x01\x12\x1b\n\x17\x46ORCE_PARALLEL_MODE_OFF\x10\x02\x12\x1f\n\x1b\x46ORCE_PARALLEL_MODE_REGRESS\x10\x03\"\x92\x02\n\x08LogLevel\x12\x19\n\x15LOG_LEVEL_UNSPECIFIED\x10\x00\x12\x14\n\x10LOG_LEVEL_DEBUG5\x10\x01\x12\x14\n\x10LOG_LEVEL_DEBUG4\x10\x02\x12\x14\n\x10LOG_LEVEL_DEBUG3\x10\x03\x12\x14\n\x10LOG_LEVEL_DEBUG2\x10\x04\x12\x14\n\x10LOG_LEVEL_DEBUG1\x10\x05\x12\x11\n\rLOG_LEVEL_LOG\x10\x06\x12\x14\n\x10LOG_LEVEL_NOTICE\x10\x07\x12\x15\n\x11LOG_LEVEL_WARNING\x10\x08\x12\x13\n\x0fLOG_LEVEL_ERROR\x10\t\x12\x13\n\x0fLOG_LEVEL_FATAL\x10\n\x12\x13\n\x0fLOG_LEVEL_PANIC\x10\x0b\"\x99\x01\n\x11LogErrorVerbosity\x12#\n\x1fLOG_ERROR_VERBOSITY_UNSPECIFIED\x10\x00\x12\x1d\n\x19LOG_ERROR_VERBOSITY_TERSE\x10\x01\x12\x1f\n\x1bLOG_ERROR_VERBOSITY_DEFAULT\x10\x02\x12\x1f\n\x1bLOG_ERROR_VERBOSITY_VERBOSE\x10\x03\"\x8a\x01\n\x0cLogStatement\x12\x1d\n\x19LOG_STATEMENT_UNSPECIFIED\x10\x00\x12\x16\n\x12LOG_STATEMENT_NONE\x10\x01\x12\x15\n\x11LOG_STATEMENT_DDL\x10\x02\x12\x15\n\x11LOG_STATEMENT_MOD\x10\x03\x12\x15\n\x11LOG_STATEMENT_ALL\x10\x04\"\xe6\x01\n\x14TransactionIsolation\x12%\n!TRANSACTION_ISOLATION_UNSPECIFIED\x10\x00\x12*\n&TRANSACTION_ISOLATION_READ_UNCOMMITTED\x10\x01\x12(\n$TRANSACTION_ISOLATION_READ_COMMITTED\x10\x02\x12)\n%TRANSACTION_ISOLATION_REPEATABLE_READ\x10\x03\x12&\n\"TRANSACTION_ISOLATION_SERIALIZABLE\x10\x04\"[\n\x0b\x42yteaOutput\x12\x1c\n\x18\x42YTEA_OUTPUT_UNSPECIFIED\x10\x00\x12\x14\n\x10\x42YTEA_OUTPUT_HEX\x10\x01\x12\x18\n\x14\x42YTEA_OUTPUT_ESCAPED\x10\x02\"R\n\tXmlBinary\x12\x1a\n\x16XML_BINARY_UNSPECIFIED\x10\x00\x12\x15\n\x11XML_BINARY_BASE64\x10\x01\x12\x12\n\x0eXML_BINARY_HEX\x10\x02\"X\n\tXmlOption\x12\x1a\n\x16XML_OPTION_UNSPECIFIED\x10\x00\x12\x17\n\x13XML_OPTION_DOCUMENT\x10\x01\x12\x16\n\x12XML_OPTION_CONTENT\x10\x02\"\x9a\x01\n\x0e\x42\x61\x63kslashQuote\x12\x1f\n\x1b\x42\x41\x43KSLASH_QUOTE_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x42\x41\x43KSLASH_QUOTE\x10\x01\x12\x16\n\x12\x42\x41\x43KSLASH_QUOTE_ON\x10\x02\x12\x17\n\x13\x42\x41\x43KSLASH_QUOTE_OFF\x10\x03\x12!\n\x1d\x42\x41\x43KSLASH_QUOTE_SAFE_ENCODING\x10\x04\"\x99\x01\n\rPlanCacheMode\x12\x1f\n\x1bPLAN_CACHE_MODE_UNSPECIFIED\x10\x00\x12\x18\n\x14PLAN_CACHE_MODE_AUTO\x10\x01\x12%\n!PLAN_CACHE_MODE_FORCE_CUSTOM_PLAN\x10\x02\x12&\n\"PLAN_CACHE_MODE_FORCE_GENERIC_PLAN\x10\x03\"\xd0\x01\n\x14PgHintPlanDebugPrint\x12(\n$PG_HINT_PLAN_DEBUG_PRINT_UNSPECIFIED\x10\x00\x12 \n\x1cPG_HINT_PLAN_DEBUG_PRINT_OFF\x10\x01\x12\x1f\n\x1bPG_HINT_PLAN_DEBUG_PRINT_ON\x10\x02\x12%\n!PG_HINT_PLAN_DEBUG_PRINT_DETAILED\x10\x03\x12$\n PG_HINT_PLAN_DEBUG_PRINT_VERBOSE\x10\x04\"\xed\x01\n\x16SharedPreloadLibraries\x12(\n$SHARED_PRELOAD_LIBRARIES_UNSPECIFIED\x10\x00\x12)\n%SHARED_PRELOAD_LIBRARIES_AUTO_EXPLAIN\x10\x01\x12)\n%SHARED_PRELOAD_LIBRARIES_PG_HINT_PLAN\x10\x02\x12(\n$SHARED_PRELOAD_LIBRARIES_TIMESCALEDB\x10\x03\x12)\n%SHARED_PRELOAD_LIBRARIES_PG_QUALSTATS\x10\x04\"\x8f\x02\n\x15PostgresqlConfigSet12\x12S\n\x10\x65\x66\x66\x65\x63tive_config\x18\x01 \x01(\x0b\x32\x39.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12\x12N\n\x0buser_config\x18\x02 \x01(\x0b\x32\x39.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12\x12Q\n\x0e\x64\x65\x66\x61ult_config\x18\x03 \x01(\x0b\x32\x39.yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12B\x81\x01\n)yandex.cloud.api.mdb.postgresql.v1.configZTgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/postgresql/v1/config;postgresqlb\x06proto3')



_POSTGRESQLCONFIG12 = DESCRIPTOR.message_types_by_name['PostgresqlConfig12']
_POSTGRESQLCONFIGSET12 = DESCRIPTOR.message_types_by_name['PostgresqlConfigSet12']
_POSTGRESQLCONFIG12_WALLEVEL = _POSTGRESQLCONFIG12.enum_types_by_name['WalLevel']
_POSTGRESQLCONFIG12_SYNCHRONOUSCOMMIT = _POSTGRESQLCONFIG12.enum_types_by_name['SynchronousCommit']
_POSTGRESQLCONFIG12_CONSTRAINTEXCLUSION = _POSTGRESQLCONFIG12.enum_types_by_name['ConstraintExclusion']
_POSTGRESQLCONFIG12_FORCEPARALLELMODE = _POSTGRESQLCONFIG12.enum_types_by_name['ForceParallelMode']
_POSTGRESQLCONFIG12_LOGLEVEL = _POSTGRESQLCONFIG12.enum_types_by_name['LogLevel']
_POSTGRESQLCONFIG12_LOGERRORVERBOSITY = _POSTGRESQLCONFIG12.enum_types_by_name['LogErrorVerbosity']
_POSTGRESQLCONFIG12_LOGSTATEMENT = _POSTGRESQLCONFIG12.enum_types_by_name['LogStatement']
_POSTGRESQLCONFIG12_TRANSACTIONISOLATION = _POSTGRESQLCONFIG12.enum_types_by_name['TransactionIsolation']
_POSTGRESQLCONFIG12_BYTEAOUTPUT = _POSTGRESQLCONFIG12.enum_types_by_name['ByteaOutput']
_POSTGRESQLCONFIG12_XMLBINARY = _POSTGRESQLCONFIG12.enum_types_by_name['XmlBinary']
_POSTGRESQLCONFIG12_XMLOPTION = _POSTGRESQLCONFIG12.enum_types_by_name['XmlOption']
_POSTGRESQLCONFIG12_BACKSLASHQUOTE = _POSTGRESQLCONFIG12.enum_types_by_name['BackslashQuote']
_POSTGRESQLCONFIG12_PLANCACHEMODE = _POSTGRESQLCONFIG12.enum_types_by_name['PlanCacheMode']
_POSTGRESQLCONFIG12_PGHINTPLANDEBUGPRINT = _POSTGRESQLCONFIG12.enum_types_by_name['PgHintPlanDebugPrint']
_POSTGRESQLCONFIG12_SHAREDPRELOADLIBRARIES = _POSTGRESQLCONFIG12.enum_types_by_name['SharedPreloadLibraries']
PostgresqlConfig12 = _reflection.GeneratedProtocolMessageType('PostgresqlConfig12', (_message.Message,), {
  'DESCRIPTOR' : _POSTGRESQLCONFIG12,
  '__module__' : 'yandex.cloud.mdb.postgresql.v1.config.postgresql12_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfig12)
  })
_sym_db.RegisterMessage(PostgresqlConfig12)

PostgresqlConfigSet12 = _reflection.GeneratedProtocolMessageType('PostgresqlConfigSet12', (_message.Message,), {
  'DESCRIPTOR' : _POSTGRESQLCONFIGSET12,
  '__module__' : 'yandex.cloud.mdb.postgresql.v1.config.postgresql12_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.mdb.postgresql.v1.config.PostgresqlConfigSet12)
  })
_sym_db.RegisterMessage(PostgresqlConfigSet12)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)yandex.cloud.api.mdb.postgresql.v1.configZTgithub.com/yandex-cloud/go-genproto/yandex/cloud/mdb/postgresql/v1/config;postgresql'
  _POSTGRESQLCONFIG12.fields_by_name['bgwriter_delay']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['bgwriter_delay']._serialized_options = b'\372\3071\01010-10000'
  _POSTGRESQLCONFIG12.fields_by_name['bgwriter_flush_after']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['bgwriter_flush_after']._serialized_options = b'\372\3071\0060-2048'
  _POSTGRESQLCONFIG12.fields_by_name['backend_flush_after']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['backend_flush_after']._serialized_options = b'\372\3071\0060-2048'
  _POSTGRESQLCONFIG12.fields_by_name['old_snapshot_threshold']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['old_snapshot_threshold']._serialized_options = b'\372\3071\013-1-86400000'
  _POSTGRESQLCONFIG12.fields_by_name['checkpoint_timeout']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['checkpoint_timeout']._serialized_options = b'\372\3071\01630000-86400000'
  _POSTGRESQLCONFIG12.fields_by_name['checkpoint_flush_after']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['checkpoint_flush_after']._serialized_options = b'\372\3071\0060-2048'
  _POSTGRESQLCONFIG12.fields_by_name['from_collapse_limit']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['from_collapse_limit']._serialized_options = b'\372\3071\0141-2147483647'
  _POSTGRESQLCONFIG12.fields_by_name['join_collapse_limit']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['join_collapse_limit']._serialized_options = b'\372\3071\0141-2147483647'
  _POSTGRESQLCONFIG12.fields_by_name['autovacuum_max_workers']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['autovacuum_max_workers']._serialized_options = b'\372\3071\0041-32'
  _POSTGRESQLCONFIG12.fields_by_name['autovacuum_vacuum_cost_delay']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['autovacuum_vacuum_cost_delay']._serialized_options = b'\372\3071\006-1-100'
  _POSTGRESQLCONFIG12.fields_by_name['autovacuum_vacuum_cost_limit']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['autovacuum_vacuum_cost_limit']._serialized_options = b'\372\3071\010-1-10000'
  _POSTGRESQLCONFIG12.fields_by_name['autovacuum_naptime']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['autovacuum_naptime']._serialized_options = b'\372\3071\r1000-86400000'
  _POSTGRESQLCONFIG12.fields_by_name['archive_timeout']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['archive_timeout']._serialized_options = b'\372\3071\01610000-86400000'
  _POSTGRESQLCONFIG12.fields_by_name['track_activity_query_size']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['track_activity_query_size']._serialized_options = b'\372\3071\n100-102400'
  _POSTGRESQLCONFIG12.fields_by_name['max_worker_processes']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['max_worker_processes']._serialized_options = b'\372\3071\0060-1024'
  _POSTGRESQLCONFIG12.fields_by_name['max_parallel_workers']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['max_parallel_workers']._serialized_options = b'\372\3071\0060-1024'
  _POSTGRESQLCONFIG12.fields_by_name['max_parallel_workers_per_gather']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['max_parallel_workers_per_gather']._serialized_options = b'\372\3071\0060-1024'
  _POSTGRESQLCONFIG12.fields_by_name['autovacuum_vacuum_scale_factor']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['autovacuum_vacuum_scale_factor']._serialized_options = b'\372\3071\0070.0-1.0'
  _POSTGRESQLCONFIG12.fields_by_name['autovacuum_analyze_scale_factor']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['autovacuum_analyze_scale_factor']._serialized_options = b'\372\3071\0070.0-1.0'
  _POSTGRESQLCONFIG12.fields_by_name['max_parallel_maintenance_workers']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['max_parallel_maintenance_workers']._serialized_options = b'\372\3071\003>=0'
  _POSTGRESQLCONFIG12.fields_by_name['vacuum_cleanup_index_scale_factor']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['vacuum_cleanup_index_scale_factor']._serialized_options = b'\372\3071\0210.0-10000000000.0'
  _POSTGRESQLCONFIG12.fields_by_name['log_transaction_sample_rate']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['log_transaction_sample_rate']._serialized_options = b'\372\3071\0070.0-1.0'
  _POSTGRESQLCONFIG12.fields_by_name['effective_io_concurrency']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['effective_io_concurrency']._serialized_options = b'\372\3071\0060-1000'
  _POSTGRESQLCONFIG12.fields_by_name['effective_cache_size']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['effective_cache_size']._serialized_options = b'\372\3071\0160-549755813888'
  _POSTGRESQLCONFIG12.fields_by_name['auto_explain_log_min_duration']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['auto_explain_log_min_duration']._serialized_options = b'\372\3071\r-1-2147483647'
  _POSTGRESQLCONFIG12.fields_by_name['auto_explain_sample_rate']._options = None
  _POSTGRESQLCONFIG12.fields_by_name['auto_explain_sample_rate']._serialized_options = b'\372\3071\0070.0-1.0'
  _POSTGRESQLCONFIG12._serialized_start=163
  _POSTGRESQLCONFIG12._serialized_end=10849
  _POSTGRESQLCONFIG12_WALLEVEL._serialized_start=8405
  _POSTGRESQLCONFIG12_WALLEVEL._serialized_end=8488
  _POSTGRESQLCONFIG12_SYNCHRONOUSCOMMIT._serialized_start=8491
  _POSTGRESQLCONFIG12_SYNCHRONOUSCOMMIT._serialized_end=8705
  _POSTGRESQLCONFIG12_CONSTRAINTEXCLUSION._serialized_start=8708
  _POSTGRESQLCONFIG12_CONSTRAINTEXCLUSION._serialized_end=8862
  _POSTGRESQLCONFIG12_FORCEPARALLELMODE._serialized_start=8865
  _POSTGRESQLCONFIG12_FORCEPARALLELMODE._serialized_end=9011
  _POSTGRESQLCONFIG12_LOGLEVEL._serialized_start=9014
  _POSTGRESQLCONFIG12_LOGLEVEL._serialized_end=9288
  _POSTGRESQLCONFIG12_LOGERRORVERBOSITY._serialized_start=9291
  _POSTGRESQLCONFIG12_LOGERRORVERBOSITY._serialized_end=9444
  _POSTGRESQLCONFIG12_LOGSTATEMENT._serialized_start=9447
  _POSTGRESQLCONFIG12_LOGSTATEMENT._serialized_end=9585
  _POSTGRESQLCONFIG12_TRANSACTIONISOLATION._serialized_start=9588
  _POSTGRESQLCONFIG12_TRANSACTIONISOLATION._serialized_end=9818
  _POSTGRESQLCONFIG12_BYTEAOUTPUT._serialized_start=9820
  _POSTGRESQLCONFIG12_BYTEAOUTPUT._serialized_end=9911
  _POSTGRESQLCONFIG12_XMLBINARY._serialized_start=9913
  _POSTGRESQLCONFIG12_XMLBINARY._serialized_end=9995
  _POSTGRESQLCONFIG12_XMLOPTION._serialized_start=9997
  _POSTGRESQLCONFIG12_XMLOPTION._serialized_end=10085
  _POSTGRESQLCONFIG12_BACKSLASHQUOTE._serialized_start=10088
  _POSTGRESQLCONFIG12_BACKSLASHQUOTE._serialized_end=10242
  _POSTGRESQLCONFIG12_PLANCACHEMODE._serialized_start=10245
  _POSTGRESQLCONFIG12_PLANCACHEMODE._serialized_end=10398
  _POSTGRESQLCONFIG12_PGHINTPLANDEBUGPRINT._serialized_start=10401
  _POSTGRESQLCONFIG12_PGHINTPLANDEBUGPRINT._serialized_end=10609
  _POSTGRESQLCONFIG12_SHAREDPRELOADLIBRARIES._serialized_start=10612
  _POSTGRESQLCONFIG12_SHAREDPRELOADLIBRARIES._serialized_end=10849
  _POSTGRESQLCONFIGSET12._serialized_start=10852
  _POSTGRESQLCONFIGSET12._serialized_end=11123
# @@protoc_insertion_point(module_scope)
