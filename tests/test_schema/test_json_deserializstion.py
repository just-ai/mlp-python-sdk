from decimal import Decimal
from typing import List

from mlp_sdk.types import (
    ChatCompletionRequest,
    ChatCompletionResult,
    ChatCompletionRole,
    ChatMessage,
    FunctionCall,
    ImageContentPart,
    ImageUrl,
    NamedToolChoice,
    NamedToolChoiceFunction,
    TextContentPart,
    ToolCall,
    ToolChoiceEnum,
    ToolType,
)


def test_deserialize_simple_chatgpt_request():
    body = """
    {
        "model": "gpt-4o",
        "messages": [
          {
            "role": "system",
            "content": "You are a helpful assistant."
          },
          {
            "role": "user",
            "content": "Hello!"
          }
        ]
      }
    """.strip()

    try:
        chat_completion_request = ChatCompletionRequest.parse_raw(body)
    except Exception as e:
        raise AssertionError(e)  # noqa: B904

    for message in chat_completion_request.messages:
        assert isinstance(message.content, str)


def test_deserialize_function_chatgpt_request():
    body = """
        {
          "model": "gpt-4-turbo",
          "messages": [
            {
              "role": "user",
              "content": "What's the weather like in Boston today?"
            },
            {
              "tool_call_id": "123456",
              "role": "tool",
              "name": "get_current_time",
              "content": "time_response"
            },
            {
              "role": "assistant",
              "tool_calls": [
                {
                  "id": "call_abc123",
                  "type": "function",
                  "function": {
                    "name": "get_current_weather",
                    "arguments": "{\\n\\"location\\": \\"Boston, MA\\"\\n}"
                  }
                }
              ]
            }
          ],
          "tools": [
            {
              "type": "function",
              "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                  "type": "object",
                  "properties": {
                    "location": {
                      "type": "string",
                      "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                      "type": "string",
                      "enum": [
                        "celsius",
                        "fahrenheit"
                      ]
                    }
                  },
                  "required": [
                    "location"
                  ]
                }
              }
            }
          ],
          "tool_choice": "auto"
        }
    """.strip()

    try:
        chat_completion_request = ChatCompletionRequest.parse_raw(body)
    except Exception as e:
        raise AssertionError(e)  # noqa: B904

    assert chat_completion_request.tool_choice == ToolChoiceEnum.auto

    user_message = chat_completion_request.messages[0]
    assert user_message.content == "What's the weather like in Boston today?"

    tool_message = chat_completion_request.messages[1]
    expected_tool_message = ChatMessage(
        role=ChatCompletionRole.TOOL, tool_call_id="123456", name="get_current_time", content="time_response"
    )
    assert tool_message == expected_tool_message

    assistant_message = chat_completion_request.messages[2]
    expected_assistant_message = ChatMessage(
        role=ChatCompletionRole.ASSISTANT,
        content=None,
        tool_calls=[
            ToolCall(
                id="call_abc123",
                type=ToolType.function,
                function=FunctionCall(name="get_current_weather", arguments='{\n"location": "Boston, MA"\n}'),
            )
        ],
    )
    assert assistant_message == expected_assistant_message

    assert chat_completion_request.tools is not None
    tool = chat_completion_request.tools[0]

    assert tool.type == ToolType.function

    function = tool.function
    assert function.name == "get_current_weather"
    assert function.description == "Get the current weather in a given location"

    parameters = function.parameters
    assert parameters["type"] == "object"

    properties = parameters["properties"]
    location = properties["location"]
    assert location["type"] == "string"
    assert location["description"] == "The city and state, e.g. San Francisco, CA"

    unit = properties["unit"]
    assert unit["type"] == "string"
    assert unit["enum"] == ["celsius", "fahrenheit"]


def test_deserialize_image_chatgpt_request():
    body = """
                {
                  "model": "gpt-4-turbo",
                  "messages": [
                    {
                      "role": "user",
                      "content": [
                        {
                          "type": "text",
                          "text": "What's in this image?"
                        },
                        {
                          "type": "image_url",
                          "image_url": {
                            "url": "https://example.com/image.jpg"
                          }
                        }
                      ]
                    }
                  ],
                  "max_tokens": 300
                }
        """.strip()

    try:
        chat_completion_request = ChatCompletionRequest.parse_raw(body)
    except Exception as e:
        raise AssertionError(e)  # noqa: B904

    message = chat_completion_request.messages[0]
    message_content = message.content
    assert message_content is not None
    assert isinstance(message_content, List)

    text_content_part = message_content[0]
    assert isinstance(text_content_part, TextContentPart)
    assert text_content_part.text == "What's in this image?"

    image_content_part = message_content[1]
    assert isinstance(image_content_part, ImageContentPart)
    assert image_content_part.image_url == ImageUrl(url="https://example.com/image.jpg")


def test_deserialize_image_chatgpt_response():
    response = """
            {
              "id": "chatcmpl-123",
              "object": "chat.completion",
              "created": 1677652288,
              "model": "gpt-3.5-turbo-0125",
              "system_fingerprint": "fp_44709d6fcb",
              "choices": [{
                "index": 0,
                "message": {
                  "role": "assistant",
                  "content": "\\n\\nThis image shows a wooden boardwalk extending through a lush green marshland."
                },
                "logprobs": null,
                "finish_reason": "stop"
              }],
              "usage": {
                "prompt_tokens": 9,
                "completion_tokens": 12,
                "total_tokens": 21
              }
            }
        """.strip()

    try:
        chat_completion_response = ChatCompletionResult.parse_raw(response)
    except Exception as e:
        raise AssertionError(e)  # noqa: B904

    message_content = chat_completion_response.choices[0].message.content
    assert message_content == "\n\nThis image shows a wooden boardwalk extending through a lush green marshland."


def test_deserialize_logprobs_chatgpt_request_and_response():
    body = """
            {
              "model": "gpt-4o",
              "messages": [
                {
                  "role": "user",
                  "content": "Hello!"
                }
              ],
              "logprobs": true,
              "top_logprobs": 2
            }
        """.strip()

    try:
        chat_completion_request = ChatCompletionRequest.parse_raw(body)
    except Exception as e:
        raise AssertionError(e)  # noqa: B904

    assert chat_completion_request.messages[0] == ChatMessage(role=ChatCompletionRole.USER, content="Hello!")
    assert chat_completion_request.logprobs
    assert chat_completion_request.top_logprobs == 2

    response = """
            {
              "id": "chatcmpl-123",
              "object": "chat.completion",
              "created": 1702685778,
              "model": "gpt-3.5-turbo-0125",
              "choices": [
                {
                  "index": 0,
                  "message": {
                    "role": "assistant",
                    "content": "Hello! How can I assist you today?"
                  },
                  "logprobs": {
                    "content": [
                      {
                        "token": "Hello",
                        "logprob": -0.31725305,
                        "bytes": [72, 101, 108, 108, 111],
                        "top_logprobs": [
                          {
                            "token": "Hello",
                            "logprob": -0.31725305,
                            "bytes": [72, 101, 108, 108, 111]
                          },
                          {
                            "token": "Hi",
                            "logprob": -1.3190403,
                            "bytes": [72, 105]
                          }
                        ]
                      },
                      {
                        "token": "!",
                        "logprob": -0.02380986,
                        "bytes": [
                          33
                        ],
                        "top_logprobs": [
                          {
                            "token": "!",
                            "logprob": -0.02380986,
                            "bytes": [33]
                          },
                          {
                            "token": " there",
                            "logprob": -3.787621,
                            "bytes": [32, 116, 104, 101, 114, 101]
                          }
                        ]
                      },
                      {
                        "token": " How",
                        "logprob": -0.000054669687,
                        "bytes": [32, 72, 111, 119],
                        "top_logprobs": [
                          {
                            "token": " How",
                            "logprob": -0.000054669687,
                            "bytes": [32, 72, 111, 119]
                          },
                          {
                            "token": "<|end|>",
                            "logprob": -10.953937,
                            "bytes": null
                          }
                        ]
                      },
                      {
                        "token": " can",
                        "logprob": -0.015801601,
                        "bytes": [32, 99, 97, 110],
                        "top_logprobs": [
                          {
                            "token": " can",
                            "logprob": -0.015801601,
                            "bytes": [32, 99, 97, 110]
                          },
                          {
                            "token": " may",
                            "logprob": -4.161023,
                            "bytes": [32, 109, 97, 121]
                          }
                        ]
                      },
                      {
                        "token": " I",
                        "logprob": -3.7697225e-6,
                        "bytes": [
                          32,
                          73
                        ],
                        "top_logprobs": [
                          {
                            "token": " I",
                            "logprob": -3.7697225e-6,
                            "bytes": [32, 73]
                          },
                          {
                            "token": " assist",
                            "logprob": -13.596657,
                            "bytes": [32, 97, 115, 115, 105, 115, 116]
                          }
                        ]
                      },
                      {
                        "token": " assist",
                        "logprob": -0.04571125,
                        "bytes": [32, 97, 115, 115, 105, 115, 116],
                        "top_logprobs": [
                          {
                            "token": " assist",
                            "logprob": -0.04571125,
                            "bytes": [32, 97, 115, 115, 105, 115, 116]
                          },
                          {
                            "token": " help",
                            "logprob": -3.1089056,
                            "bytes": [32, 104, 101, 108, 112]
                          }
                        ]
                      },
                      {
                        "token": " you",
                        "logprob": -5.4385737e-6,
                        "bytes": [32, 121, 111, 117],
                        "top_logprobs": [
                          {
                            "token": " you",
                            "logprob": -5.4385737e-6,
                            "bytes": [32, 121, 111, 117]
                          },
                          {
                            "token": " today",
                            "logprob": -12.807695,
                            "bytes": [32, 116, 111, 100, 97, 121]
                          }
                        ]
                      },
                      {
                        "token": " today",
                        "logprob": -0.0040071653,
                        "bytes": [32, 116, 111, 100, 97, 121],
                        "top_logprobs": [
                          {
                            "token": " today",
                            "logprob": -0.0040071653,
                            "bytes": [32, 116, 111, 100, 97, 121]
                          },
                          {
                            "token": "?",
                            "logprob": -5.5247097,
                            "bytes": [63]
                          }
                        ]
                      },
                      {
                        "token": "?",
                        "logprob": -0.0008108172,
                        "bytes": [63],
                        "top_logprobs": [
                          {
                            "token": "?",
                            "logprob": -0.0008108172,
                            "bytes": [63]
                          },
                          {
                            "token": "?\\n",
                            "logprob": -7.184561,
                            "bytes": [63, 10]
                          }
                        ]
                      }
                    ]
                  },
                  "finish_reason": "stop"
                }
              ],
              "usage": {
                "prompt_tokens": 9,
                "completion_tokens": 9,
                "total_tokens": 18
              },
              "system_fingerprint": null
            }
        """.strip()
    try:
        chat_completion_response = ChatCompletionResult.parse_raw(response)
    except Exception as e:
        raise AssertionError(e)  # noqa: B904

    choice = chat_completion_response.choices[0]
    message_content = choice.message.content
    assert message_content == "Hello! How can I assist you today?"

    assert choice.logprobs is not None
    assert len(choice.logprobs.content) == 9
    assert choice.logprobs.content[0].logprob == Decimal("-0.31725305")


def test_deserialize_named_function_call_chatgpt_request():
    body = """
            {
              "model": "Qwen/Qwen2-7B-Instruct",
              "messages": [
                {
                  "role": "user",
                  "content": "What's the weather like in Boston today?"
                }
              ],
              "tools": [
                {
                  "type": "function",
                  "function": {
                    "name": "get_current_weather",
                    "description": "Get the current weather in a given location",
                    "parameters": {
                      "type": "object",
                      "properties": {
                        "location": {
                          "type": "string",
                          "description": "The city and state, e.g. San Francisco, CA"
                        },
                        "unit": {
                          "type": "string",
                          "enum": [
                            "celsius",
                            "fahrenheit"
                          ]
                        }
                      },
                      "required": [
                        "location"
                      ]
                    }
                  }
                }
              ],
              "tool_choice": {
                "type": "function",
                "function": {
                  "name": "get_current_weather"
                }
              }
            }
        """.strip()

    try:
        chat_completion_request = ChatCompletionRequest.parse_raw(body)
    except Exception as e:
        raise AssertionError(e)  # noqa: B904

    assert chat_completion_request.tool_choice == NamedToolChoice(
        type=ToolType.function, function=NamedToolChoiceFunction(name="get_current_weather")
    )
