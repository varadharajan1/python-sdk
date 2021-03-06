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


class MessageSenderApi(object):
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

    def delete_assignment(self, message_sender_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_assignment(message_sender_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str message_sender_id: ID of the message sender. (required)
        :param str buyer_id: ID of the buyer.
        :param str user_id: ID of the user.
        :param str user_group_id: ID of the user group.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_assignment_with_http_info(message_sender_id, **kwargs)
        else:
            (data) = self.delete_assignment_with_http_info(message_sender_id, **kwargs)
            return data

    def delete_assignment_with_http_info(self, message_sender_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_assignment_with_http_info(message_sender_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str message_sender_id: ID of the message sender. (required)
        :param str buyer_id: ID of the buyer.
        :param str user_id: ID of the user.
        :param str user_group_id: ID of the user group.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_sender_id', 'buyer_id', 'user_id', 'user_group_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_sender_id' is set
        if ('message_sender_id' not in params) or (params['message_sender_id'] is None):
            raise ValueError("Missing the required parameter `message_sender_id` when calling `delete_assignment`")

        resource_path = '/messagesenders/{messageSenderID}/assignments'.replace('{format}', 'json')
        path_params = {}
        if 'message_sender_id' in params:
            path_params['messageSenderID'] = params['message_sender_id']

        query_params = {}
        if 'buyer_id' in params:
            query_params['buyerID'] = params['buyer_id']
        if 'user_id' in params:
            query_params['userID'] = params['user_id']
        if 'user_group_id' in params:
            query_params['userGroupID'] = params['user_group_id']

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

    def get(self, message_sender_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get(message_sender_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str message_sender_id: ID of the message sender. (required)
        :return: MessageSender
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(message_sender_id, **kwargs)
        else:
            (data) = self.get_with_http_info(message_sender_id, **kwargs)
            return data

    def get_with_http_info(self, message_sender_id, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_with_http_info(message_sender_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str message_sender_id: ID of the message sender. (required)
        :return: MessageSender
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_sender_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_sender_id' is set
        if ('message_sender_id' not in params) or (params['message_sender_id'] is None):
            raise ValueError("Missing the required parameter `message_sender_id` when calling `get`")

        resource_path = '/messagesenders/{messageSenderID}'.replace('{format}', 'json')
        path_params = {}
        if 'message_sender_id' in params:
            path_params['messageSenderID'] = params['message_sender_id']

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
                                            response_type='MessageSender',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Word or phrase to search for.
        :param str search_on: Comma-delimited list of fields to search on.
        :param str sort_by: Comma-delimited list of fields to sort by.
        :param int page: Page of results to return. Default: 1
        :param int page_size: Number of results to return per page. Default: 20, max: 100.
        :param dict(str, str) filters: Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'
        :return: ListMessageSender
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(**kwargs)
        else:
            (data) = self.list_with_http_info(**kwargs)
            return data

    def list_with_http_info(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Word or phrase to search for.
        :param str search_on: Comma-delimited list of fields to search on.
        :param str sort_by: Comma-delimited list of fields to sort by.
        :param int page: Page of results to return. Default: 1
        :param int page_size: Number of results to return per page. Default: 20, max: 100.
        :param dict(str, str) filters: Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'
        :return: ListMessageSender
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'search_on', 'sort_by', 'page', 'page_size', 'filters']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/messagesenders'.replace('{format}', 'json')
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
        if 'filters' in params:
            query_params['filters'] = params['filters']

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
                                            response_type='ListMessageSender',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list_assignments(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_assignments(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer.
        :param str message_sender_id: ID of the message sender.
        :param str user_id: ID of the user.
        :param str user_group_id: ID of the user group.
        :param str level: Level of the message sender assignment. Possible values: User, Group, Company.
        :param int page: Page of results to return. Default: 1
        :param int page_size: Number of results to return per page. Default: 20, max: 100.
        :return: ListMessageSenderAssignment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_assignments_with_http_info(**kwargs)
        else:
            (data) = self.list_assignments_with_http_info(**kwargs)
            return data

    def list_assignments_with_http_info(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_assignments_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str buyer_id: ID of the buyer.
        :param str message_sender_id: ID of the message sender.
        :param str user_id: ID of the user.
        :param str user_group_id: ID of the user group.
        :param str level: Level of the message sender assignment. Possible values: User, Group, Company.
        :param int page: Page of results to return. Default: 1
        :param int page_size: Number of results to return per page. Default: 20, max: 100.
        :return: ListMessageSenderAssignment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['buyer_id', 'message_sender_id', 'user_id', 'user_group_id', 'level', 'page', 'page_size']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_assignments" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/messagesenders/assignments'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'buyer_id' in params:
            query_params['buyerID'] = params['buyer_id']
        if 'message_sender_id' in params:
            query_params['messageSenderID'] = params['message_sender_id']
        if 'user_id' in params:
            query_params['userID'] = params['user_id']
        if 'user_group_id' in params:
            query_params['userGroupID'] = params['user_group_id']
        if 'level' in params:
            query_params['level'] = params['level']
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
                                            response_type='ListMessageSenderAssignment',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list_cc_listener_assignments(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_cc_listener_assignments(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Word or phrase to search for.
        :param str search_on: Comma-delimited list of fields to search on.
        :param str sort_by: Comma-delimited list of fields to sort by.
        :param int page: Page of results to return. Default: 1
        :param int page_size: Number of results to return per page. Default: 20, max: 100.
        :param dict(str, str) filters: Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'
        :return: ListMessageCCListenerAssignment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_cc_listener_assignments_with_http_info(**kwargs)
        else:
            (data) = self.list_cc_listener_assignments_with_http_info(**kwargs)
            return data

    def list_cc_listener_assignments_with_http_info(self, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_cc_listener_assignments_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search: Word or phrase to search for.
        :param str search_on: Comma-delimited list of fields to search on.
        :param str sort_by: Comma-delimited list of fields to sort by.
        :param int page: Page of results to return. Default: 1
        :param int page_size: Number of results to return per page. Default: 20, max: 100.
        :param dict(str, str) filters: Any additional key/value pairs passed in the query string are interpretted as filters. Valid keys are top-level properties of the returned model or 'xp.???'
        :return: ListMessageCCListenerAssignment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'search_on', 'sort_by', 'page', 'page_size', 'filters']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_cc_listener_assignments" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/messagesenders/CCListenerAssignments'.replace('{format}', 'json')
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
        if 'filters' in params:
            query_params['filters'] = params['filters']

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
                                            response_type='ListMessageCCListenerAssignment',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def save_assignment(self, message_sender_assignment, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.save_assignment(message_sender_assignment, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MessageSenderAssignment message_sender_assignment:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.save_assignment_with_http_info(message_sender_assignment, **kwargs)
        else:
            (data) = self.save_assignment_with_http_info(message_sender_assignment, **kwargs)
            return data

    def save_assignment_with_http_info(self, message_sender_assignment, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.save_assignment_with_http_info(message_sender_assignment, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MessageSenderAssignment message_sender_assignment:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_sender_assignment']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_sender_assignment' is set
        if ('message_sender_assignment' not in params) or (params['message_sender_assignment'] is None):
            raise ValueError("Missing the required parameter `message_sender_assignment` when calling `save_assignment`")

        resource_path = '/messagesenders/assignments'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'message_sender_assignment' in params:
            body_params = params['message_sender_assignment']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def save_cc_listener_assignment(self, message_cc_listener_assignment, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.save_cc_listener_assignment(message_cc_listener_assignment, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MessageCCListenerAssignment message_cc_listener_assignment:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.save_cc_listener_assignment_with_http_info(message_cc_listener_assignment, **kwargs)
        else:
            (data) = self.save_cc_listener_assignment_with_http_info(message_cc_listener_assignment, **kwargs)
            return data

    def save_cc_listener_assignment_with_http_info(self, message_cc_listener_assignment, **kwargs):
        """
        
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.save_cc_listener_assignment_with_http_info(message_cc_listener_assignment, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MessageCCListenerAssignment message_cc_listener_assignment:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_cc_listener_assignment']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_cc_listener_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_cc_listener_assignment' is set
        if ('message_cc_listener_assignment' not in params) or (params['message_cc_listener_assignment'] is None):
            raise ValueError("Missing the required parameter `message_cc_listener_assignment` when calling `save_cc_listener_assignment`")

        resource_path = '/messagesenders/CCListenerAssignments'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'message_cc_listener_assignment' in params:
            body_params = params['message_cc_listener_assignment']

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
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
