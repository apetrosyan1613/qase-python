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
from qaseio.model.environment_create import EnvironmentCreate
from qaseio.model.environment_list_response import EnvironmentListResponse
from qaseio.model.environment_response import EnvironmentResponse
from qaseio.model.environment_update import EnvironmentUpdate
from qaseio.model.id_response import IdResponse


class EnvironmentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_environment_endpoint = _Endpoint(
            settings={
                'response_type': (IdResponse,),
                'auth': [
                    'TokenAuth'
                ],
                'endpoint_path': '/environment/{code}',
                'operation_id': 'create_environment',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'code',
                    'environment_create',
                ],
                'required': [
                    'code',
                    'environment_create',
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
                    'environment_create':
                        (EnvironmentCreate,),
                },
                'attribute_map': {
                    'code': 'code',
                },
                'location_map': {
                    'code': 'path',
                    'environment_create': 'body',
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
        self.delete_environment_endpoint = _Endpoint(
            settings={
                'response_type': (IdResponse,),
                'auth': [
                    'TokenAuth'
                ],
                'endpoint_path': '/environment/{code}/{id}',
                'operation_id': 'delete_environment',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'code',
                    'id',
                ],
                'required': [
                    'code',
                    'id',
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
                },
                'attribute_map': {
                    'code': 'code',
                    'id': 'id',
                },
                'location_map': {
                    'code': 'path',
                    'id': 'path',
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
        self.get_environment_endpoint = _Endpoint(
            settings={
                'response_type': (EnvironmentResponse,),
                'auth': [
                    'TokenAuth'
                ],
                'endpoint_path': '/environment/{code}/{id}',
                'operation_id': 'get_environment',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'code',
                    'id',
                ],
                'required': [
                    'code',
                    'id',
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
                },
                'attribute_map': {
                    'code': 'code',
                    'id': 'id',
                },
                'location_map': {
                    'code': 'path',
                    'id': 'path',
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
        self.get_environments_endpoint = _Endpoint(
            settings={
                'response_type': (EnvironmentListResponse,),
                'auth': [
                    'TokenAuth'
                ],
                'endpoint_path': '/environment/{code}',
                'operation_id': 'get_environments',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'code',
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
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'code': 'code',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'code': 'path',
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
        self.update_environment_endpoint = _Endpoint(
            settings={
                'response_type': (IdResponse,),
                'auth': [
                    'TokenAuth'
                ],
                'endpoint_path': '/environment/{code}/{id}',
                'operation_id': 'update_environment',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'code',
                    'id',
                    'environment_update',
                ],
                'required': [
                    'code',
                    'id',
                    'environment_update',
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
                    'environment_update':
                        (EnvironmentUpdate,),
                },
                'attribute_map': {
                    'code': 'code',
                    'id': 'id',
                },
                'location_map': {
                    'code': 'path',
                    'id': 'path',
                    'environment_update': 'body',
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

    def create_environment(
        self,
        code,
        environment_create,
        **kwargs
    ):
        """Create a new environment.  # noqa: E501

        This method allows to create an environment in selected project.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_environment(code, environment_create, async_req=True)
        >>> result = thread.get()

        Args:
            code (str): Code of project, where to search entities.
            environment_create (EnvironmentCreate):

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
            async_req (bool): execute request asynchronously

        Returns:
            IdResponse
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
        kwargs['code'] = \
            code
        kwargs['environment_create'] = \
            environment_create
        return self.create_environment_endpoint.call_with_http_info(**kwargs)

    def delete_environment(
        self,
        code,
        id,
        **kwargs
    ):
        """Delete environment.  # noqa: E501

        This method completely deletes an environment from repository.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_environment(code, id, async_req=True)
        >>> result = thread.get()

        Args:
            code (str): Code of project, where to search entities.
            id (int): Identifier.

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
            async_req (bool): execute request asynchronously

        Returns:
            IdResponse
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
        kwargs['code'] = \
            code
        kwargs['id'] = \
            id
        return self.delete_environment_endpoint.call_with_http_info(**kwargs)

    def get_environment(
        self,
        code,
        id,
        **kwargs
    ):
        """Get a specific environment.  # noqa: E501

        This method allows to retrieve a specific environment.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_environment(code, id, async_req=True)
        >>> result = thread.get()

        Args:
            code (str): Code of project, where to search entities.
            id (int): Identifier.

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
            async_req (bool): execute request asynchronously

        Returns:
            EnvironmentResponse
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
        kwargs['code'] = \
            code
        kwargs['id'] = \
            id
        return self.get_environment_endpoint.call_with_http_info(**kwargs)

    def get_environments(
        self,
        code,
        **kwargs
    ):
        """Get all environments.  # noqa: E501

        This method allows to retrieve all environments stored in selected project.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_environments(code, async_req=True)
        >>> result = thread.get()

        Args:
            code (str): Code of project, where to search entities.

        Keyword Args:
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
            async_req (bool): execute request asynchronously

        Returns:
            EnvironmentListResponse
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
        kwargs['code'] = \
            code
        return self.get_environments_endpoint.call_with_http_info(**kwargs)

    def update_environment(
        self,
        code,
        id,
        environment_update,
        **kwargs
    ):
        """Update environment.  # noqa: E501

        This method updates an environment.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_environment(code, id, environment_update, async_req=True)
        >>> result = thread.get()

        Args:
            code (str): Code of project, where to search entities.
            id (int): Identifier.
            environment_update (EnvironmentUpdate):

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
            async_req (bool): execute request asynchronously

        Returns:
            IdResponse
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
        kwargs['code'] = \
            code
        kwargs['id'] = \
            id
        kwargs['environment_update'] = \
            environment_update
        return self.update_environment_endpoint.call_with_http_info(**kwargs)

