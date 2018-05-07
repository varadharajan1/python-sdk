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


class AddressAssignment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address_id=None, user_id=None, user_group_id=None, is_shipping=None, is_billing=None):
        """
        AddressAssignment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address_id': 'str',
            'user_id': 'str',
            'user_group_id': 'str',
            'is_shipping': 'bool',
            'is_billing': 'bool'
        }

        self.attribute_map = {
            'address_id': 'AddressID',
            'user_id': 'UserID',
            'user_group_id': 'UserGroupID',
            'is_shipping': 'IsShipping',
            'is_billing': 'IsBilling'
        }

        self._address_id = address_id
        self._user_id = user_id
        self._user_group_id = user_group_id
        self._is_shipping = is_shipping
        self._is_billing = is_billing

    @property
    def address_id(self):
        """
        Gets the address_id of this AddressAssignment.


        :return: The address_id of this AddressAssignment.
        :rtype: str
        """
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        """
        Sets the address_id of this AddressAssignment.


        :param address_id: The address_id of this AddressAssignment.
        :type: str
        """

        self._address_id = address_id

    @property
    def user_id(self):
        """
        Gets the user_id of this AddressAssignment.


        :return: The user_id of this AddressAssignment.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AddressAssignment.


        :param user_id: The user_id of this AddressAssignment.
        :type: str
        """

        self._user_id = user_id

    @property
    def user_group_id(self):
        """
        Gets the user_group_id of this AddressAssignment.


        :return: The user_group_id of this AddressAssignment.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """
        Sets the user_group_id of this AddressAssignment.


        :param user_group_id: The user_group_id of this AddressAssignment.
        :type: str
        """

        self._user_group_id = user_group_id

    @property
    def is_shipping(self):
        """
        Gets the is_shipping of this AddressAssignment.


        :return: The is_shipping of this AddressAssignment.
        :rtype: bool
        """
        return self._is_shipping

    @is_shipping.setter
    def is_shipping(self, is_shipping):
        """
        Sets the is_shipping of this AddressAssignment.


        :param is_shipping: The is_shipping of this AddressAssignment.
        :type: bool
        """

        self._is_shipping = is_shipping

    @property
    def is_billing(self):
        """
        Gets the is_billing of this AddressAssignment.


        :return: The is_billing of this AddressAssignment.
        :rtype: bool
        """
        return self._is_billing

    @is_billing.setter
    def is_billing(self, is_billing):
        """
        Sets the is_billing of this AddressAssignment.


        :param is_billing: The is_billing of this AddressAssignment.
        :type: bool
        """

        self._is_billing = is_billing

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
