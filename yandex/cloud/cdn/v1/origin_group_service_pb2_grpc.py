# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.cdn.v1 import origin_group_pb2 as yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__pb2
from yandex.cloud.cdn.v1 import origin_group_service_pb2 as yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class OriginGroupServiceStub(object):
    """
    Origin Groups management service.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.cdn.v1.OriginGroupService/Get',
                request_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.GetOriginGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__pb2.OriginGroup.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.cdn.v1.OriginGroupService/List',
                request_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.ListOriginGroupsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.ListOriginGroupsResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.cdn.v1.OriginGroupService/Create',
                request_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.CreateOriginGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.cdn.v1.OriginGroupService/Update',
                request_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.UpdateOriginGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.cdn.v1.OriginGroupService/Delete',
                request_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.DeleteOriginGroupRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class OriginGroupServiceServicer(object):
    """
    Origin Groups management service.

    """

    def Get(self, request, context):
        """Gets origin group with specified origin group id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Lists origins of origin group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates origin group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates origin group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes origin group with specified origin group id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OriginGroupServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.GetOriginGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__pb2.OriginGroup.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.ListOriginGroupsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.ListOriginGroupsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.CreateOriginGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.UpdateOriginGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.DeleteOriginGroupRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.cdn.v1.OriginGroupService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OriginGroupService(object):
    """
    Origin Groups management service.

    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cdn.v1.OriginGroupService/Get',
            yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.GetOriginGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__pb2.OriginGroup.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cdn.v1.OriginGroupService/List',
            yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.ListOriginGroupsRequest.SerializeToString,
            yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.ListOriginGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cdn.v1.OriginGroupService/Create',
            yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.CreateOriginGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cdn.v1.OriginGroupService/Update',
            yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.UpdateOriginGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.cdn.v1.OriginGroupService/Delete',
            yandex_dot_cloud_dot_cdn_dot_v1_dot_origin__group__service__pb2.DeleteOriginGroupRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
