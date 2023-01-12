# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mlp_sdk.grpc.mlp_grpc_pb2 as mlp__grpc__pb2


class GateStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.healthCheck = channel.unary_unary(
                '/com.mlp.gate.Gate/healthCheck',
                request_serializer=mlp__grpc__pb2.HeartBeatProto.SerializeToString,
                response_deserializer=mlp__grpc__pb2.HeartBeatProto.FromString,
                )
        self.processAsync = channel.stream_stream(
                '/com.mlp.gate.Gate/processAsync',
                request_serializer=mlp__grpc__pb2.ActionToGateProto.SerializeToString,
                response_deserializer=mlp__grpc__pb2.GateToActionProto.FromString,
                )
        self.process = channel.unary_unary(
                '/com.mlp.gate.Gate/process',
                request_serializer=mlp__grpc__pb2.ClientRequestProto.SerializeToString,
                response_deserializer=mlp__grpc__pb2.ClientResponseProto.FromString,
                )


class GateServicer(object):
    """Missing associated documentation comment in .proto file."""

    def healthCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def processAsync(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def process(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GateServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'healthCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.healthCheck,
                    request_deserializer=mlp__grpc__pb2.HeartBeatProto.FromString,
                    response_serializer=mlp__grpc__pb2.HeartBeatProto.SerializeToString,
            ),
            'processAsync': grpc.stream_stream_rpc_method_handler(
                    servicer.processAsync,
                    request_deserializer=mlp__grpc__pb2.ActionToGateProto.FromString,
                    response_serializer=mlp__grpc__pb2.GateToActionProto.SerializeToString,
            ),
            'process': grpc.unary_unary_rpc_method_handler(
                    servicer.process,
                    request_deserializer=mlp__grpc__pb2.ClientRequestProto.FromString,
                    response_serializer=mlp__grpc__pb2.ClientResponseProto.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.mlp.gate.Gate', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Gate(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def healthCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mlp.gate.Gate/healthCheck',
            mlp__grpc__pb2.HeartBeatProto.SerializeToString,
            mlp__grpc__pb2.HeartBeatProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def processAsync(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/com.mlp.gate.Gate/processAsync',
            mlp__grpc__pb2.ActionToGateProto.SerializeToString,
            mlp__grpc__pb2.GateToActionProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def process(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mlp.gate.Gate/process',
            mlp__grpc__pb2.ClientRequestProto.SerializeToString,
            mlp__grpc__pb2.ClientResponseProto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
