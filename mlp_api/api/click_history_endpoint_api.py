# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictStr, conlist

from typing import Optional

from mlp_api.models.click_history_data import ClickHistoryData

from mlp_api.api_client import ApiClient
from mlp_api.api_response import ApiResponse
from mlp_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ClickHistoryEndpointApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def save_click(self, click_history_data : conlist(ClickHistoryData), visitor_id : Optional[StrictStr] = None, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> None:  # noqa: E501
        """save_click  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.save_click(click_history_data, visitor_id, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param click_history_data: (required)
        :type click_history_data: List[ClickHistoryData]
        :param visitor_id:
        :type visitor_id: str
        :param mlp_api_key: token to use instead of a session
        :type mlp_api_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the save_click_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.save_click_with_http_info(click_history_data, visitor_id, mlp_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def save_click_with_http_info(self, click_history_data : conlist(ClickHistoryData), visitor_id : Optional[StrictStr] = None, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """save_click  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.save_click_with_http_info(click_history_data, visitor_id, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param click_history_data: (required)
        :type click_history_data: List[ClickHistoryData]
        :param visitor_id:
        :type visitor_id: str
        :param mlp_api_key: token to use instead of a session
        :type mlp_api_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'click_history_data',
            'visitor_id',
            'mlp_api_key'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_click" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['mlp_api_key'] is not None:
            _header_params['MLP-API-KEY'] = _params['mlp_api_key']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['click_history_data'] is not None:
            _body_params = _params['click_history_data']

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/mlpcore/clicks', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
