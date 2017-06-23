# coding: utf-8

"""
    OrderCloud

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    Contact: ordercloud@four51.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ImpersonationConfigApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def impersonationconfig_get(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.impersonationconfig_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Search of the impersonation config.
        :param list[str] search_on: Search on of the impersonation config.
        :param list[str] sort_by: Sort by of the impersonation config.
        :param int page: Page of the impersonation config.
        :param int page_size: Page size of the impersonation config.
        :return: ListImpersonationConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.impersonationconfig_get_with_http_info(**kwargs)
        else:
            (data) = self.impersonationconfig_get_with_http_info(**kwargs)
            return data

    def impersonationconfig_get_with_http_info(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.impersonationconfig_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Search of the impersonation config.
        :param list[str] search_on: Search on of the impersonation config.
        :param list[str] sort_by: Sort by of the impersonation config.
        :param int page: Page of the impersonation config.
        :param int page_size: Page size of the impersonation config.
        :return: ListImpersonationConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'search_on', 'sort_by', 'page', 'page_size']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method impersonationconfig_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/impersonationconfig'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'search' in params:
            query_params['search'] = params['search']
        if 'search_on' in params:
            query_params['searchOn'] = params['search_on']
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ListImpersonationConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def impersonationconfig_impersonation_config_id_delete(self, impersonation_config_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.impersonationconfig_impersonation_config_id_delete(impersonation_config_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str impersonation_config_id: ID of the impersonation config. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.impersonationconfig_impersonation_config_id_delete_with_http_info(impersonation_config_id, **kwargs)
        else:
            (data) = self.impersonationconfig_impersonation_config_id_delete_with_http_info(impersonation_config_id, **kwargs)
            return data

    def impersonationconfig_impersonation_config_id_delete_with_http_info(self, impersonation_config_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.impersonationconfig_impersonation_config_id_delete_with_http_info(impersonation_config_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str impersonation_config_id: ID of the impersonation config. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['impersonation_config_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method impersonationconfig_impersonation_config_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'impersonation_config_id' is set
        if ('impersonation_config_id' not in params) or (params['impersonation_config_id'] is None):
            raise ValueError("Missing the required parameter `impersonation_config_id` when calling `impersonationconfig_impersonation_config_id_delete`")

        resource_path = '/impersonationconfig/{impersonationConfigID}'.replace('{format}', 'json')
        path_params = {}
        if 'impersonation_config_id' in params:
            path_params['impersonationConfigID'] = params['impersonation_config_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def impersonationconfig_impersonation_config_id_get(self, impersonation_config_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.impersonationconfig_impersonation_config_id_get(impersonation_config_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str impersonation_config_id: ID of the impersonation config. (required)
        :return: ImpersonationConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.impersonationconfig_impersonation_config_id_get_with_http_info(impersonation_config_id, **kwargs)
        else:
            (data) = self.impersonationconfig_impersonation_config_id_get_with_http_info(impersonation_config_id, **kwargs)
            return data

    def impersonationconfig_impersonation_config_id_get_with_http_info(self, impersonation_config_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.impersonationconfig_impersonation_config_id_get_with_http_info(impersonation_config_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str impersonation_config_id: ID of the impersonation config. (required)
        :return: ImpersonationConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['impersonation_config_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method impersonationconfig_impersonation_config_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'impersonation_config_id' is set
        if ('impersonation_config_id' not in params) or (params['impersonation_config_id'] is None):
            raise ValueError("Missing the required parameter `impersonation_config_id` when calling `impersonationconfig_impersonation_config_id_get`")

        resource_path = '/impersonationconfig/{impersonationConfigID}'.replace('{format}', 'json')
        path_params = {}
        if 'impersonation_config_id' in params:
            path_params['impersonationConfigID'] = params['impersonation_config_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ImpersonationConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def impersonationconfig_impersonation_config_id_patch(self, impersonation_config_id, impersonation_config, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.impersonationconfig_impersonation_config_id_patch(impersonation_config_id, impersonation_config, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str impersonation_config_id: ID of the impersonation config. (required)
        :param ImpersonationConfig impersonation_config:  (required)
        :return: ImpersonationConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.impersonationconfig_impersonation_config_id_patch_with_http_info(impersonation_config_id, impersonation_config, **kwargs)
        else:
            (data) = self.impersonationconfig_impersonation_config_id_patch_with_http_info(impersonation_config_id, impersonation_config, **kwargs)
            return data

    def impersonationconfig_impersonation_config_id_patch_with_http_info(self, impersonation_config_id, impersonation_config, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.impersonationconfig_impersonation_config_id_patch_with_http_info(impersonation_config_id, impersonation_config, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str impersonation_config_id: ID of the impersonation config. (required)
        :param ImpersonationConfig impersonation_config:  (required)
        :return: ImpersonationConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['impersonation_config_id', 'impersonation_config']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method impersonationconfig_impersonation_config_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'impersonation_config_id' is set
        if ('impersonation_config_id' not in params) or (params['impersonation_config_id'] is None):
            raise ValueError("Missing the required parameter `impersonation_config_id` when calling `impersonationconfig_impersonation_config_id_patch`")
        # verify the required parameter 'impersonation_config' is set
        if ('impersonation_config' not in params) or (params['impersonation_config'] is None):
            raise ValueError("Missing the required parameter `impersonation_config` when calling `impersonationconfig_impersonation_config_id_patch`")

        resource_path = '/impersonationconfig/{impersonationConfigID}'.replace('{format}', 'json')
        path_params = {}
        if 'impersonation_config_id' in params:
            path_params['impersonationConfigID'] = params['impersonation_config_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'impersonation_config' in params:
            body_params = params['impersonation_config']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ImpersonationConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def impersonationconfig_impersonation_config_id_put(self, impersonation_config_id, impersonation_config, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.impersonationconfig_impersonation_config_id_put(impersonation_config_id, impersonation_config, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str impersonation_config_id: ID of the impersonation config. (required)
        :param ImpersonationConfig impersonation_config:  (required)
        :return: ImpersonationConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.impersonationconfig_impersonation_config_id_put_with_http_info(impersonation_config_id, impersonation_config, **kwargs)
        else:
            (data) = self.impersonationconfig_impersonation_config_id_put_with_http_info(impersonation_config_id, impersonation_config, **kwargs)
            return data

    def impersonationconfig_impersonation_config_id_put_with_http_info(self, impersonation_config_id, impersonation_config, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.impersonationconfig_impersonation_config_id_put_with_http_info(impersonation_config_id, impersonation_config, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str impersonation_config_id: ID of the impersonation config. (required)
        :param ImpersonationConfig impersonation_config:  (required)
        :return: ImpersonationConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['impersonation_config_id', 'impersonation_config']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method impersonationconfig_impersonation_config_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'impersonation_config_id' is set
        if ('impersonation_config_id' not in params) or (params['impersonation_config_id'] is None):
            raise ValueError("Missing the required parameter `impersonation_config_id` when calling `impersonationconfig_impersonation_config_id_put`")
        # verify the required parameter 'impersonation_config' is set
        if ('impersonation_config' not in params) or (params['impersonation_config'] is None):
            raise ValueError("Missing the required parameter `impersonation_config` when calling `impersonationconfig_impersonation_config_id_put`")

        resource_path = '/impersonationconfig/{impersonationConfigID}'.replace('{format}', 'json')
        path_params = {}
        if 'impersonation_config_id' in params:
            path_params['impersonationConfigID'] = params['impersonation_config_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'impersonation_config' in params:
            body_params = params['impersonation_config']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ImpersonationConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def impersonationconfig_post(self, impersonation_config, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.impersonationconfig_post(impersonation_config, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ImpersonationConfig impersonation_config:  (required)
        :return: ImpersonationConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.impersonationconfig_post_with_http_info(impersonation_config, **kwargs)
        else:
            (data) = self.impersonationconfig_post_with_http_info(impersonation_config, **kwargs)
            return data

    def impersonationconfig_post_with_http_info(self, impersonation_config, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.impersonationconfig_post_with_http_info(impersonation_config, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ImpersonationConfig impersonation_config:  (required)
        :return: ImpersonationConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['impersonation_config']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method impersonationconfig_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'impersonation_config' is set
        if ('impersonation_config' not in params) or (params['impersonation_config'] is None):
            raise ValueError("Missing the required parameter `impersonation_config` when calling `impersonationconfig_post`")

        resource_path = '/impersonationconfig'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'impersonation_config' in params:
            body_params = params['impersonation_config']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ImpersonationConfig',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
