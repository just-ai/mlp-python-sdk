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
from pydantic import Field, StrictInt, StrictStr

from typing import List, Optional

from mlp_api.models.config_create_update_data import ConfigCreateUpdateData
from mlp_api.models.predict_config_data import PredictConfigData

from mlp_api.api_client import ApiClient
from mlp_api.api_response import ApiResponse
from mlp_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PredictConfigEndpointApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_predict_config(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], model : Annotated[StrictStr, Field(..., description="Model id or model name")], config_create_update_data : ConfigCreateUpdateData, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> PredictConfigData:  # noqa: E501
        """create_predict_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_predict_config(account, model, config_create_update_data, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param model: Model id or model name (required)
        :type model: str
        :param config_create_update_data: (required)
        :type config_create_update_data: ConfigCreateUpdateData
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
        :rtype: PredictConfigData
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_predict_config_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.create_predict_config_with_http_info(account, model, config_create_update_data, mlp_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def create_predict_config_with_http_info(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], model : Annotated[StrictStr, Field(..., description="Model id or model name")], config_create_update_data : ConfigCreateUpdateData, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """create_predict_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_predict_config_with_http_info(account, model, config_create_update_data, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param model: Model id or model name (required)
        :type model: str
        :param config_create_update_data: (required)
        :type config_create_update_data: ConfigCreateUpdateData
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
        :rtype: tuple(PredictConfigData, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'account',
            'model',
            'config_create_update_data',
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
                    " to method create_predict_config" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account'] is not None:
            _path_params['account'] = _params['account']

        if _params['model'] is not None:
            _path_params['model'] = _params['model']


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
        if _params['config_create_update_data'] is not None:
            _body_params = _params['config_create_update_data']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "PredictConfigData",
        }

        return self.api_client.call_api(
            '/api/mlpcore/account/{account}/model/{model}/predict-config', 'POST',
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

    @validate_arguments
    def delete_predict_config(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], model : Annotated[StrictStr, Field(..., description="Model id or model name")], config_id : StrictInt, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> None:  # noqa: E501
        """delete_predict_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_predict_config(account, model, config_id, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param model: Model id or model name (required)
        :type model: str
        :param config_id: (required)
        :type config_id: int
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
            message = "Error! Please call the delete_predict_config_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.delete_predict_config_with_http_info(account, model, config_id, mlp_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_predict_config_with_http_info(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], model : Annotated[StrictStr, Field(..., description="Model id or model name")], config_id : StrictInt, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """delete_predict_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_predict_config_with_http_info(account, model, config_id, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param model: Model id or model name (required)
        :type model: str
        :param config_id: (required)
        :type config_id: int
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
            'account',
            'model',
            'config_id',
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
                    " to method delete_predict_config" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account'] is not None:
            _path_params['account'] = _params['account']

        if _params['model'] is not None:
            _path_params['model'] = _params['model']

        if _params['config_id'] is not None:
            _path_params['configId'] = _params['config_id']


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
        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/mlpcore/account/{account}/model/{model}/predict-config/{configId}', 'DELETE',
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

    @validate_arguments
    def get_predict_config(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], model : Annotated[StrictStr, Field(..., description="Model id or model name")], config_id : StrictInt, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> PredictConfigData:  # noqa: E501
        """get_predict_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_predict_config(account, model, config_id, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param model: Model id or model name (required)
        :type model: str
        :param config_id: (required)
        :type config_id: int
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
        :rtype: PredictConfigData
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_predict_config_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_predict_config_with_http_info(account, model, config_id, mlp_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def get_predict_config_with_http_info(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], model : Annotated[StrictStr, Field(..., description="Model id or model name")], config_id : StrictInt, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_predict_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_predict_config_with_http_info(account, model, config_id, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param model: Model id or model name (required)
        :type model: str
        :param config_id: (required)
        :type config_id: int
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
        :rtype: tuple(PredictConfigData, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'account',
            'model',
            'config_id',
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
                    " to method get_predict_config" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account'] is not None:
            _path_params['account'] = _params['account']

        if _params['model'] is not None:
            _path_params['model'] = _params['model']

        if _params['config_id'] is not None:
            _path_params['configId'] = _params['config_id']


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
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "PredictConfigData",
        }

        return self.api_client.call_api(
            '/api/mlpcore/account/{account}/model/{model}/predict-config/{configId}', 'GET',
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

    @validate_arguments
    def list_predict_configs(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], model : Annotated[StrictStr, Field(..., description="Model id or model name")], mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> List[PredictConfigData]:  # noqa: E501
        """list_predict_configs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_predict_configs(account, model, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param model: Model id or model name (required)
        :type model: str
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
        :rtype: List[PredictConfigData]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_predict_configs_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.list_predict_configs_with_http_info(account, model, mlp_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def list_predict_configs_with_http_info(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], model : Annotated[StrictStr, Field(..., description="Model id or model name")], mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """list_predict_configs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_predict_configs_with_http_info(account, model, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param model: Model id or model name (required)
        :type model: str
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
        :rtype: tuple(List[PredictConfigData], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'account',
            'model',
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
                    " to method list_predict_configs" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account'] is not None:
            _path_params['account'] = _params['account']

        if _params['model'] is not None:
            _path_params['model'] = _params['model']


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
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "List[PredictConfigData]",
        }

        return self.api_client.call_api(
            '/api/mlpcore/account/{account}/model/{model}/predict-config', 'GET',
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

    @validate_arguments
    def update_predict_config(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], model : Annotated[StrictStr, Field(..., description="Model id or model name")], config_id : StrictInt, config_create_update_data : ConfigCreateUpdateData, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> PredictConfigData:  # noqa: E501
        """update_predict_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_predict_config(account, model, config_id, config_create_update_data, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param model: Model id or model name (required)
        :type model: str
        :param config_id: (required)
        :type config_id: int
        :param config_create_update_data: (required)
        :type config_create_update_data: ConfigCreateUpdateData
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
        :rtype: PredictConfigData
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the update_predict_config_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.update_predict_config_with_http_info(account, model, config_id, config_create_update_data, mlp_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def update_predict_config_with_http_info(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], model : Annotated[StrictStr, Field(..., description="Model id or model name")], config_id : StrictInt, config_create_update_data : ConfigCreateUpdateData, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """update_predict_config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_predict_config_with_http_info(account, model, config_id, config_create_update_data, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param model: Model id or model name (required)
        :type model: str
        :param config_id: (required)
        :type config_id: int
        :param config_create_update_data: (required)
        :type config_create_update_data: ConfigCreateUpdateData
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
        :rtype: tuple(PredictConfigData, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'account',
            'model',
            'config_id',
            'config_create_update_data',
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
                    " to method update_predict_config" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account'] is not None:
            _path_params['account'] = _params['account']

        if _params['model'] is not None:
            _path_params['model'] = _params['model']

        if _params['config_id'] is not None:
            _path_params['configId'] = _params['config_id']


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
        if _params['config_create_update_data'] is not None:
            _body_params = _params['config_create_update_data']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "PredictConfigData",
        }

        return self.api_client.call_api(
            '/api/mlpcore/account/{account}/model/{model}/predict-config/{configId}', 'POST',
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
