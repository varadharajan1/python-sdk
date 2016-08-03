# coding: utf-8

"""
    OrderCloud

    A full ecommerce backend as a service.

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


class LineItemSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, spec_id=None, name=None, option_id=None, value=None):
        """
        LineItemSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'spec_id': 'str',
            'name': 'str',
            'option_id': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'spec_id': 'SpecID',
            'name': 'Name',
            'option_id': 'OptionID',
            'value': 'Value'
        }

        self._spec_id = spec_id
        self._name = name
        self._option_id = option_id
        self._value = value

    @property
    def spec_id(self):
        """
        Gets the spec_id of this LineItemSpec.


        :return: The spec_id of this LineItemSpec.
        :rtype: str
        """
        return self._spec_id

    @spec_id.setter
    def spec_id(self, spec_id):
        """
        Sets the spec_id of this LineItemSpec.


        :param spec_id: The spec_id of this LineItemSpec.
        :type: str
        """

        self._spec_id = spec_id

    @property
    def name(self):
        """
        Gets the name of this LineItemSpec.


        :return: The name of this LineItemSpec.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LineItemSpec.


        :param name: The name of this LineItemSpec.
        :type: str
        """

        self._name = name

    @property
    def option_id(self):
        """
        Gets the option_id of this LineItemSpec.


        :return: The option_id of this LineItemSpec.
        :rtype: str
        """
        return self._option_id

    @option_id.setter
    def option_id(self, option_id):
        """
        Sets the option_id of this LineItemSpec.


        :param option_id: The option_id of this LineItemSpec.
        :type: str
        """

        self._option_id = option_id

    @property
    def value(self):
        """
        Gets the value of this LineItemSpec.


        :return: The value of this LineItemSpec.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this LineItemSpec.


        :param value: The value of this LineItemSpec.
        :type: str
        """

        self._value = value

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
