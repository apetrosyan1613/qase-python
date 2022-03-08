# coding: utf-8

"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@qase.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from qaseio.api_client import ApiClient


class CustomFieldsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_custom_field(self, body, **kwargs):  # noqa: E501
        """Create new Custom Field.  # noqa: E501

        This method allows to create custom field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_custom_field(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomFieldCreate body: (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_custom_field_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_custom_field_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_custom_field_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create new Custom Field.  # noqa: E501

        This method allows to create custom field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_custom_field_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomFieldCreate body: (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_custom_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_custom_field`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/custom_field', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_custom_field(self, id, **kwargs):  # noqa: E501
        """Delete Custom Field by id.  # noqa: E501

        This method allows to delete custom field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_custom_field(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifier. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_custom_field_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_custom_field_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_custom_field_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete Custom Field by id.  # noqa: E501

        This method allows to delete custom field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_custom_field_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifier. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_custom_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_custom_field`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/custom_field/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Response',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_custom_field(self, id, **kwargs):  # noqa: E501
        """Get Custom Field by id.  # noqa: E501

        This method allows to retrieve custom field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_field(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifier. (required)
        :return: CustomFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_custom_field_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_custom_field_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_custom_field_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Custom Field by id.  # noqa: E501

        This method allows to retrieve custom field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_field_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Identifier. (required)
        :return: CustomFieldResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_custom_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_custom_field`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/custom_field/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomFieldResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_custom_fields(self, **kwargs):  # noqa: E501
        """Get all Custom Fields.  # noqa: E501

        This method allows to retrieve and filter custom fields.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_fields(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Filters1 filters:
        :param int limit: A number of entities in result set.
        :param int offset: How many entities should be skipped.
        :return: CustomFieldsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_custom_fields_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_custom_fields_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_custom_fields_with_http_info(self, **kwargs):  # noqa: E501
        """Get all Custom Fields.  # noqa: E501

        This method allows to retrieve and filter custom fields.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_fields_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Filters1 filters:
        :param int limit: A number of entities in result set.
        :param int offset: How many entities should be skipped.
        :return: CustomFieldsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filters', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_custom_fields" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filters' in params:
            query_params.append(('filters', params['filters']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/custom_field', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomFieldsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_custom_field(self, body, id, **kwargs):  # noqa: E501
        """Update Custom Field by id.  # noqa: E501

        This method allows to update custom field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_custom_field(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomFieldUpdate body: (required)
        :param int id: Identifier. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_custom_field_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_custom_field_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def update_custom_field_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update Custom Field by id.  # noqa: E501

        This method allows to update custom field.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_custom_field_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CustomFieldUpdate body: (required)
        :param int id: Identifier. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_custom_field" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_custom_field`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_custom_field`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/custom_field/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Response',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
