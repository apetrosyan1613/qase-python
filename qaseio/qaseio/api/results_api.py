"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from qaseio.api_client import ApiClient, Endpoint as _Endpoint
from qaseio.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from qaseio.model.create_result200_response import CreateResult200Response
from qaseio.model.get_results_filters_parameter import GetResultsFiltersParameter
from qaseio.model.hash_response import HashResponse
from qaseio.model.response import Response
from qaseio.model.result_create import ResultCreate
from qaseio.model.result_create_bulk import ResultCreateBulk
from qaseio.model.result_list_response import ResultListResponse
from qaseio.model.result_response import ResultResponse
from qaseio.model.result_update import ResultUpdate


class ResultsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_result_endpoint = _Endpoint(
            settings={
                'response_type': (CreateResult200Response,),
                'auth': [
                    'TokenAuth'
                ],
                'endpoint_path': '/result/{code}/{id}',
                'operation_id': 'create_result',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'code',
                    'id',
                    'result_create',
                ],
                'required': [
                    'code',
                    'id',
                    'result_create',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'code',
                ]
            },
            root_map={
                'validations': {
                    ('code',): {
                        'max_length': 10,
                        'min_length': 2,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'code':
                        (str,),
                    'id':
                        (int,),
                    'result_create':
                        (ResultCreate,),
                },
                'attribute_map': {
                    'code': 'code',
                    'id': 'id',
                },
                'location_map': {
                    'code': 'path',
                    'id': 'path',
                    'result_create': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_result_bulk_endpoint = _Endpoint(
            settings={
                'response_type': (Response,),
                'auth': [
                    'TokenAuth'
                ],
                'endpoint_path': '/result/{code}/{id}/bulk',
                'operation_id': 'create_result_bulk',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'code',
                    'id',
                    'result_create_bulk',
                ],
                'required': [
                    'code',
                    'id',
                    'result_create_bulk',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'code',
                ]
            },
            root_map={
                'validations': {
                    ('code',): {
                        'max_length': 10,
                        'min_length': 2,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'code':
                        (str,),
                    'id':
                        (int,),
                    'result_create_bulk':
                        (ResultCreateBulk,),
                },
                'attribute_map': {
                    'code': 'code',
                    'id': 'id',
                },
                'location_map': {
                    'code': 'path',
                    'id': 'path',
                    'result_create_bulk': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_result_endpoint = _Endpoint(
            settings={
                'response_type': (HashResponse,),
                'auth': [
                    'TokenAuth'
                ],
                'endpoint_path': '/result/{code}/{id}/{hash}',
                'operation_id': 'delete_result',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'code',
                    'id',
                    'hash',
                ],
                'required': [
                    'code',
                    'id',
                    'hash',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'code',
                ]
            },
            root_map={
                'validations': {
                    ('code',): {
                        'max_length': 10,
                        'min_length': 2,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'code':
                        (str,),
                    'id':
                        (int,),
                    'hash':
                        (str,),
                },
                'attribute_map': {
                    'code': 'code',
                    'id': 'id',
                    'hash': 'hash',
                },
                'location_map': {
                    'code': 'path',
                    'id': 'path',
                    'hash': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_result_endpoint = _Endpoint(
            settings={
                'response_type': (ResultResponse,),
                'auth': [
                    'TokenAuth'
                ],
                'endpoint_path': '/result/{code}/{hash}',
                'operation_id': 'get_result',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'code',
                    'hash',
                ],
                'required': [
                    'code',
                    'hash',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'code',
                ]
            },
            root_map={
                'validations': {
                    ('code',): {
                        'max_length': 10,
                        'min_length': 2,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'code':
                        (str,),
                    'hash':
                        (str,),
                },
                'attribute_map': {
                    'code': 'code',
                    'hash': 'hash',
                },
                'location_map': {
                    'code': 'path',
                    'hash': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_results_endpoint = _Endpoint(
            settings={
                'response_type': (ResultListResponse,),
                'auth': [
                    'TokenAuth'
                ],
                'endpoint_path': '/result/{code}',
                'operation_id': 'get_results',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'code',
                    'filters',
                    'limit',
                    'offset',
                ],
                'required': [
                    'code',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'code',
                    'limit',
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('code',): {
                        'max_length': 10,
                        'min_length': 2,
                    },
                    ('limit',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                    ('offset',): {

                        'inclusive_maximum': 100000,
                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'code':
                        (str,),
                    'filters':
                        (GetResultsFiltersParameter,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'code': 'code',
                    'filters': 'filters',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'code': 'path',
                    'filters': 'query',
                    'limit': 'query',
                    'offset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_result_endpoint = _Endpoint(
            settings={
                'response_type': (HashResponse,),
                'auth': [
                    'TokenAuth'
                ],
                'endpoint_path': '/result/{code}/{id}/{hash}',
                'operation_id': 'update_result',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'code',
                    'id',
                    'hash',
                    'result_update',
                ],
                'required': [
                    'code',
                    'id',
                    'hash',
                    'result_update',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'code',
                ]
            },
            root_map={
                'validations': {
                    ('code',): {
                        'max_length': 10,
                        'min_length': 2,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'code':
                        (str,),
                    'id':
                        (int,),
                    'hash':
                        (str,),
                    'result_update':
                        (ResultUpdate,),
                },
                'attribute_map': {
                    'code': 'code',
                    'id': 'id',
                    'hash': 'hash',
                },
                'location_map': {
                    'code': 'path',
                    'id': 'path',
                    'hash': 'path',
                    'result_update': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def create_result(
        self,
        code,
        id,
        result_create,
        **kwargs
    ):
        """Create test run result.  # noqa: E501

        This method allows to create test run result by Run Id.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_result(code, id, result_create, async_req=True)
        >>> result = thread.get()

        Args:
            code (str): Code of project, where to search entities.
            id (int): Identifier.
            result_create (ResultCreate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CreateResult200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['code'] = \
            code
        kwargs['id'] = \
            id
        kwargs['result_create'] = \
            result_create
        return self.create_result_endpoint.call_with_http_info(**kwargs)

    def create_result_bulk(
        self,
        code,
        id,
        result_create_bulk,
        **kwargs
    ):
        """Bulk create test run result.  # noqa: E501

        This method allows to create a lot of test run result at once.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_result_bulk(code, id, result_create_bulk, async_req=True)
        >>> result = thread.get()

        Args:
            code (str): Code of project, where to search entities.
            id (int): Identifier.
            result_create_bulk (ResultCreateBulk):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['code'] = \
            code
        kwargs['id'] = \
            id
        kwargs['result_create_bulk'] = \
            result_create_bulk
        return self.create_result_bulk_endpoint.call_with_http_info(**kwargs)

    def delete_result(
        self,
        code,
        id,
        hash,
        **kwargs
    ):
        """Delete test run result.  # noqa: E501

        This method allows to delete test run result.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_result(code, id, hash, async_req=True)
        >>> result = thread.get()

        Args:
            code (str): Code of project, where to search entities.
            id (int): Identifier.
            hash (str): Hash.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            HashResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['code'] = \
            code
        kwargs['id'] = \
            id
        kwargs['hash'] = \
            hash
        return self.delete_result_endpoint.call_with_http_info(**kwargs)

    def get_result(
        self,
        code,
        hash,
        **kwargs
    ):
        """Get test run result by code.  # noqa: E501

        This method allows to retrieve a specific test run result by Hash.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_result(code, hash, async_req=True)
        >>> result = thread.get()

        Args:
            code (str): Code of project, where to search entities.
            hash (str): Hash.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ResultResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['code'] = \
            code
        kwargs['hash'] = \
            hash
        return self.get_result_endpoint.call_with_http_info(**kwargs)

    def get_results(
        self,
        code,
        **kwargs
    ):
        """Get all test run results.  # noqa: E501

        This method allows to retrieve all test run results stored in selected project.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_results(code, async_req=True)
        >>> result = thread.get()

        Args:
            code (str): Code of project, where to search entities.

        Keyword Args:
            filters (GetResultsFiltersParameter): [optional]
            limit (int): A number of entities in result set.. [optional] if omitted the server will use the default value of 10
            offset (int): How many entities should be skipped.. [optional] if omitted the server will use the default value of 0
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ResultListResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['code'] = \
            code
        return self.get_results_endpoint.call_with_http_info(**kwargs)

    def update_result(
        self,
        code,
        id,
        hash,
        result_update,
        **kwargs
    ):
        """Update test run result.  # noqa: E501

        This method allows to update test run result.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_result(code, id, hash, result_update, async_req=True)
        >>> result = thread.get()

        Args:
            code (str): Code of project, where to search entities.
            id (int): Identifier.
            hash (str): Hash.
            result_update (ResultUpdate):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            HashResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['code'] = \
            code
        kwargs['id'] = \
            id
        kwargs['hash'] = \
            hash
        kwargs['result_update'] = \
            result_update
        return self.update_result_endpoint.call_with_http_info(**kwargs)

