# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt, StrictStr

from typing import Optional

from mlp_api.models.data_image_info_data import DataImageInfoData
from mlp_api.models.paged_data_image_info_data import PagedDataImageInfoData

from mlp_api.api_client import ApiClient
from mlp_api.api_response import ApiResponse
from mlp_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DataImageEndpointApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_data_image(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], data_image_info_data : DataImageInfoData, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> DataImageInfoData:  # noqa: E501
        """create_data_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_data_image(account, data_image_info_data, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param data_image_info_data: (required)
        :type data_image_info_data: DataImageInfoData
        :param mlp_api_key: token to use instead of a session
        :type mlp_api_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DataImageInfoData
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_data_image_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_data_image_with_http_info(account, data_image_info_data, mlp_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def create_data_image_with_http_info(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], data_image_info_data : DataImageInfoData, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """create_data_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_data_image_with_http_info(account, data_image_info_data, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param data_image_info_data: (required)
        :type data_image_info_data: DataImageInfoData
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
        :rtype: tuple(DataImageInfoData, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'account',
            'data_image_info_data',
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
                    " to method create_data_image" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account']:
            _path_params['account'] = _params['account']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['mlp_api_key']:
            _header_params['MLP-API-KEY'] = _params['mlp_api_key']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['data_image_info_data'] is not None:
            _body_params = _params['data_image_info_data']

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
            '200': "DataImageInfoData",
        }

        return self.api_client.call_api(
            '/api/mlpgate/account/{account}/data-image', 'POST',
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
    def delete_data_image(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], image_id : StrictInt, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> None:  # noqa: E501
        """delete_data_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_data_image(account, image_id, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param image_id: (required)
        :type image_id: int
        :param mlp_api_key: token to use instead of a session
        :type mlp_api_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_data_image_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_data_image_with_http_info(account, image_id, mlp_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_data_image_with_http_info(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], image_id : StrictInt, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """delete_data_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_data_image_with_http_info(account, image_id, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param image_id: (required)
        :type image_id: int
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
            'image_id',
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
                    " to method delete_data_image" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account']:
            _path_params['account'] = _params['account']

        if _params['image_id']:
            _path_params['imageId'] = _params['image_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['mlp_api_key']:
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
            '/api/mlpgate/account/{account}/data-image/{imageId}', 'DELETE',
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
    def get_data_image(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], image_id : StrictInt, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> DataImageInfoData:  # noqa: E501
        """get_data_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_data_image(account, image_id, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param image_id: (required)
        :type image_id: int
        :param mlp_api_key: token to use instead of a session
        :type mlp_api_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DataImageInfoData
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_data_image_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_data_image_with_http_info(account, image_id, mlp_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def get_data_image_with_http_info(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], image_id : StrictInt, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_data_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_data_image_with_http_info(account, image_id, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param image_id: (required)
        :type image_id: int
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
        :rtype: tuple(DataImageInfoData, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'account',
            'image_id',
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
                    " to method get_data_image" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account']:
            _path_params['account'] = _params['account']

        if _params['image_id']:
            _path_params['imageId'] = _params['image_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['mlp_api_key']:
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
            '200': "DataImageInfoData",
        }

        return self.api_client.call_api(
            '/api/mlpgate/account/{account}/data-image/{imageId}', 'GET',
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
    def get_paged_data_images(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], name : Optional[StrictStr] = None, only_my : Optional[StrictBool] = None, page : Optional[StrictInt] = None, size : Optional[StrictInt] = None, sort : Optional[StrictStr] = None, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> PagedDataImageInfoData:  # noqa: E501
        """get_paged_data_images  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_paged_data_images(account, name, only_my, page, size, sort, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param name:
        :type name: str
        :param only_my:
        :type only_my: bool
        :param page:
        :type page: int
        :param size:
        :type size: int
        :param sort:
        :type sort: str
        :param mlp_api_key: token to use instead of a session
        :type mlp_api_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PagedDataImageInfoData
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_paged_data_images_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_paged_data_images_with_http_info(account, name, only_my, page, size, sort, mlp_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def get_paged_data_images_with_http_info(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], name : Optional[StrictStr] = None, only_my : Optional[StrictBool] = None, page : Optional[StrictInt] = None, size : Optional[StrictInt] = None, sort : Optional[StrictStr] = None, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_paged_data_images  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_paged_data_images_with_http_info(account, name, only_my, page, size, sort, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param name:
        :type name: str
        :param only_my:
        :type only_my: bool
        :param page:
        :type page: int
        :param size:
        :type size: int
        :param sort:
        :type sort: str
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
        :rtype: tuple(PagedDataImageInfoData, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'account',
            'name',
            'only_my',
            'page',
            'size',
            'sort',
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
                    " to method get_paged_data_images" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account']:
            _path_params['account'] = _params['account']


        # process the query parameters
        _query_params = []
        if _params.get('name') is not None:  # noqa: E501
            _query_params.append(('name', _params['name']))

        if _params.get('only_my') is not None:  # noqa: E501
            _query_params.append(('onlyMy', _params['only_my']))

        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('size') is not None:  # noqa: E501
            _query_params.append(('size', _params['size']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['mlp_api_key']:
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
            '200': "PagedDataImageInfoData",
        }

        return self.api_client.call_api(
            '/api/mlpgate/account/{account}/data-image', 'GET',
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
    def update_data_image(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], image_id : StrictInt, data_image_info_data : DataImageInfoData, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> DataImageInfoData:  # noqa: E501
        """update_data_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_data_image(account, image_id, data_image_info_data, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param image_id: (required)
        :type image_id: int
        :param data_image_info_data: (required)
        :type data_image_info_data: DataImageInfoData
        :param mlp_api_key: token to use instead of a session
        :type mlp_api_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DataImageInfoData
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_data_image_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_data_image_with_http_info(account, image_id, data_image_info_data, mlp_api_key, **kwargs)  # noqa: E501

    @validate_arguments
    def update_data_image_with_http_info(self, account : Annotated[StrictStr, Field(..., description="Account id or account name")], image_id : StrictInt, data_image_info_data : DataImageInfoData, mlp_api_key : Annotated[Optional[StrictStr], Field(description="token to use instead of a session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """update_data_image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_data_image_with_http_info(account, image_id, data_image_info_data, mlp_api_key, async_req=True)
        >>> result = thread.get()

        :param account: Account id or account name (required)
        :type account: str
        :param image_id: (required)
        :type image_id: int
        :param data_image_info_data: (required)
        :type data_image_info_data: DataImageInfoData
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
        :rtype: tuple(DataImageInfoData, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'account',
            'image_id',
            'data_image_info_data',
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
                    " to method update_data_image" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['account']:
            _path_params['account'] = _params['account']

        if _params['image_id']:
            _path_params['imageId'] = _params['image_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['mlp_api_key']:
            _header_params['MLP-API-KEY'] = _params['mlp_api_key']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['data_image_info_data'] is not None:
            _body_params = _params['data_image_info_data']

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
            '200': "DataImageInfoData",
        }

        return self.api_client.call_api(
            '/api/mlpgate/account/{account}/data-image/{imageId}', 'POST',
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
