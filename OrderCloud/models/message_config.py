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

from pprint import pformat
from six import iteritems
import re


class MessageConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, url=None, elevated_claims_list=None, shared_key=None, config_data=None):
        """
        MessageConfig - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'elevated_claims_list': 'str',
            'shared_key': 'str',
            'config_data': 'object'
        }

        self.attribute_map = {
            'url': 'URL',
            'elevated_claims_list': 'ElevatedClaimsList',
            'shared_key': 'SharedKey',
            'config_data': 'ConfigData'
        }

        self._url = url
        self._elevated_claims_list = elevated_claims_list
        self._shared_key = shared_key
        self._config_data = config_data

    @property
    def url(self):
        """
        Gets the url of this MessageConfig.


        :return: The url of this MessageConfig.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this MessageConfig.


        :param url: The url of this MessageConfig.
        :type: str
        """

        self._url = url

    @property
    def elevated_claims_list(self):
        """
        Gets the elevated_claims_list of this MessageConfig.


        :return: The elevated_claims_list of this MessageConfig.
        :rtype: str
        """
        return self._elevated_claims_list

    @elevated_claims_list.setter
    def elevated_claims_list(self, elevated_claims_list):
        """
        Sets the elevated_claims_list of this MessageConfig.


        :param elevated_claims_list: The elevated_claims_list of this MessageConfig.
        :type: str
        """

        self._elevated_claims_list = elevated_claims_list

    @property
    def shared_key(self):
        """
        Gets the shared_key of this MessageConfig.


        :return: The shared_key of this MessageConfig.
        :rtype: str
        """
        return self._shared_key

    @shared_key.setter
    def shared_key(self, shared_key):
        """
        Sets the shared_key of this MessageConfig.


        :param shared_key: The shared_key of this MessageConfig.
        :type: str
        """

        self._shared_key = shared_key

    @property
    def config_data(self):
        """
        Gets the config_data of this MessageConfig.


        :return: The config_data of this MessageConfig.
        :rtype: object
        """
        return self._config_data

    @config_data.setter
    def config_data(self, config_data):
        """
        Sets the config_data of this MessageConfig.


        :param config_data: The config_data of this MessageConfig.
        :type: object
        """

        self._config_data = config_data

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other