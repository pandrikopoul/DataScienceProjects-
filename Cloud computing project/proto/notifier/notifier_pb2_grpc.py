# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import proto.notifier.notifier_pb2 as notifier__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class NotifierServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendNotification = channel.unary_unary(
            "/NotifierService/SendNotification",
            request_serializer=notifier__pb2.NotifierRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class NotifierServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendNotification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_NotifierServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "SendNotification": grpc.unary_unary_rpc_method_handler(
            servicer.SendNotification,
            request_deserializer=notifier__pb2.NotifierRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "NotifierService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class NotifierService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendNotification(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/NotifierService/SendNotification",
            notifier__pb2.NotifierRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
