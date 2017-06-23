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


class SupplierApi(object):
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

    def suppliers_get(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.suppliers_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Search of the supplier.
        :param list[str] search_on: Search on of the supplier.
        :param list[str] sort_by: Sort by of the supplier.
        :param int page: Page of the supplier.
        :param int page_size: Page size of the supplier.
        :return: ListSupplier
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.suppliers_get_with_http_info(**kwargs)
        else:
            (data) = self.suppliers_get_with_http_info(**kwargs)
            return data

    def suppliers_get_with_http_info(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.suppliers_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Search of the supplier.
        :param list[str] search_on: Search on of the supplier.
        :param list[str] sort_by: Sort by of the supplier.
        :param int page: Page of the supplier.
        :param int page_size: Page size of the supplier.
        :return: ListSupplier
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
                    " to method suppliers_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/suppliers'.replace('{format}', 'json')
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
                                            response_type='ListSupplier',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def suppliers_post(self, company, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.suppliers_post(company, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Supplier company:  (required)
        :return: Supplier
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.suppliers_post_with_http_info(company, **kwargs)
        else:
            (data) = self.suppliers_post_with_http_info(company, **kwargs)
            return data

    def suppliers_post_with_http_info(self, company, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.suppliers_post_with_http_info(company, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Supplier company:  (required)
        :return: Supplier
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method suppliers_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'company' is set
        if ('company' not in params) or (params['company'] is None):
            raise ValueError("Missing the required parameter `company` when calling `suppliers_post`")

        resource_path = '/suppliers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'company' in params:
            body_params = params['company']

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
                                            response_type='Supplier',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def suppliers_supplier_id_delete(self, supplier_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.suppliers_supplier_id_delete(supplier_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str supplier_id: ID of the supplier. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.suppliers_supplier_id_delete_with_http_info(supplier_id, **kwargs)
        else:
            (data) = self.suppliers_supplier_id_delete_with_http_info(supplier_id, **kwargs)
            return data

    def suppliers_supplier_id_delete_with_http_info(self, supplier_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.suppliers_supplier_id_delete_with_http_info(supplier_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str supplier_id: ID of the supplier. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['supplier_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method suppliers_supplier_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'supplier_id' is set
        if ('supplier_id' not in params) or (params['supplier_id'] is None):
            raise ValueError("Missing the required parameter `supplier_id` when calling `suppliers_supplier_id_delete`")

        resource_path = '/suppliers/{supplierID}'.replace('{format}', 'json')
        path_params = {}
        if 'supplier_id' in params:
            path_params['supplierID'] = params['supplier_id']

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

    def suppliers_supplier_id_get(self, supplier_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.suppliers_supplier_id_get(supplier_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str supplier_id: ID of the supplier. (required)
        :return: Supplier
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.suppliers_supplier_id_get_with_http_info(supplier_id, **kwargs)
        else:
            (data) = self.suppliers_supplier_id_get_with_http_info(supplier_id, **kwargs)
            return data

    def suppliers_supplier_id_get_with_http_info(self, supplier_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.suppliers_supplier_id_get_with_http_info(supplier_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str supplier_id: ID of the supplier. (required)
        :return: Supplier
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['supplier_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method suppliers_supplier_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'supplier_id' is set
        if ('supplier_id' not in params) or (params['supplier_id'] is None):
            raise ValueError("Missing the required parameter `supplier_id` when calling `suppliers_supplier_id_get`")

        resource_path = '/suppliers/{supplierID}'.replace('{format}', 'json')
        path_params = {}
        if 'supplier_id' in params:
            path_params['supplierID'] = params['supplier_id']

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
                                            response_type='Supplier',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def suppliers_supplier_id_patch(self, supplier_id, company, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.suppliers_supplier_id_patch(supplier_id, company, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str supplier_id: ID of the supplier. (required)
        :param Supplier company:  (required)
        :return: Supplier
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.suppliers_supplier_id_patch_with_http_info(supplier_id, company, **kwargs)
        else:
            (data) = self.suppliers_supplier_id_patch_with_http_info(supplier_id, company, **kwargs)
            return data

    def suppliers_supplier_id_patch_with_http_info(self, supplier_id, company, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.suppliers_supplier_id_patch_with_http_info(supplier_id, company, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str supplier_id: ID of the supplier. (required)
        :param Supplier company:  (required)
        :return: Supplier
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['supplier_id', 'company']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method suppliers_supplier_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'supplier_id' is set
        if ('supplier_id' not in params) or (params['supplier_id'] is None):
            raise ValueError("Missing the required parameter `supplier_id` when calling `suppliers_supplier_id_patch`")
        # verify the required parameter 'company' is set
        if ('company' not in params) or (params['company'] is None):
            raise ValueError("Missing the required parameter `company` when calling `suppliers_supplier_id_patch`")

        resource_path = '/suppliers/{supplierID}'.replace('{format}', 'json')
        path_params = {}
        if 'supplier_id' in params:
            path_params['supplierID'] = params['supplier_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'company' in params:
            body_params = params['company']

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
                                            response_type='Supplier',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def suppliers_supplier_id_put(self, supplier_id, company, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.suppliers_supplier_id_put(supplier_id, company, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str supplier_id: ID of the supplier. (required)
        :param Supplier company:  (required)
        :return: Supplier
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.suppliers_supplier_id_put_with_http_info(supplier_id, company, **kwargs)
        else:
            (data) = self.suppliers_supplier_id_put_with_http_info(supplier_id, company, **kwargs)
            return data

    def suppliers_supplier_id_put_with_http_info(self, supplier_id, company, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.suppliers_supplier_id_put_with_http_info(supplier_id, company, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str supplier_id: ID of the supplier. (required)
        :param Supplier company:  (required)
        :return: Supplier
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['supplier_id', 'company']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method suppliers_supplier_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'supplier_id' is set
        if ('supplier_id' not in params) or (params['supplier_id'] is None):
            raise ValueError("Missing the required parameter `supplier_id` when calling `suppliers_supplier_id_put`")
        # verify the required parameter 'company' is set
        if ('company' not in params) or (params['company'] is None):
            raise ValueError("Missing the required parameter `company` when calling `suppliers_supplier_id_put`")

        resource_path = '/suppliers/{supplierID}'.replace('{format}', 'json')
        path_params = {}
        if 'supplier_id' in params:
            path_params['supplierID'] = params['supplier_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'company' in params:
            body_params = params['company']

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
                                            response_type='Supplier',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
