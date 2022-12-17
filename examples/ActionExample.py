from caila_sdk.transport.CailaActionSDK import CailaActionSDK
from caila_sdk.grpc import mpl_grpc_pb2
from pydantic import BaseModel

class QuestionRequest:
    context: str
    answer: str

class QuestionResponse:
    question: str


class MyService:
    def get_schema(self):
        return {"main.proto": "content of a file"}

    def get_descriptor(self):
        return mpl_grpc_pb2.ActionDescriptorProto(
            name="question-generator",
            fittable=False,
            methods={"predict": mpl_grpc_pb2.MethodDescriptorProto(
                input={
                    "data": mpl_grpc_pb2.ParamDescriptorProto(type="QuestionRequest"),
                    "config": mpl_grpc_pb2.ParamDescriptorProto(type="QuestionRequest"),
                },
                output=mpl_grpc_pb2.ParamDescriptorProto(type="QuestionResponse"),
            )}
        )

    def predict(self, data: QuestionRequest, config: None):
        return QuestionResponse(question=data.context + "-" + data.answer)


caila = CailaActionSDK()
caila.register_impl(MyService())
caila.start()
caila.block_until_shutdown()
