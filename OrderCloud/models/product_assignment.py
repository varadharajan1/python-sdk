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


class ProductAssignment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, product_id=None, standard_price_schedule_id=None, replenishment_price_schedule_id=None, user_id=None, user_group_id=None, buyer_id=None):
        """
        ProductAssignment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'product_id': 'str',
            'standard_price_schedule_id': 'str',
            'replenishment_price_schedule_id': 'str',
            'user_id': 'str',
            'user_group_id': 'str',
            'buyer_id': 'str'
        }

        self.attribute_map = {
            'product_id': 'ProductID',
            'standard_price_schedule_id': 'StandardPriceScheduleID',
            'replenishment_price_schedule_id': 'ReplenishmentPriceScheduleID',
            'user_id': 'UserID',
            'user_group_id': 'UserGroupID',
            'buyer_id': 'BuyerID'
        }

        self._product_id = product_id
        self._standard_price_schedule_id = standard_price_schedule_id
        self._replenishment_price_schedule_id = replenishment_price_schedule_id
        self._user_id = user_id
        self._user_group_id = user_group_id
        self._buyer_id = buyer_id

    @property
    def product_id(self):
        """
        Gets the product_id of this ProductAssignment.


        :return: The product_id of this ProductAssignment.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this ProductAssignment.


        :param product_id: The product_id of this ProductAssignment.
        :type: str
        """

        self._product_id = product_id

    @property
    def standard_price_schedule_id(self):
        """
        Gets the standard_price_schedule_id of this ProductAssignment.


        :return: The standard_price_schedule_id of this ProductAssignment.
        :rtype: str
        """
        return self._standard_price_schedule_id

    @standard_price_schedule_id.setter
    def standard_price_schedule_id(self, standard_price_schedule_id):
        """
        Sets the standard_price_schedule_id of this ProductAssignment.


        :param standard_price_schedule_id: The standard_price_schedule_id of this ProductAssignment.
        :type: str
        """

        self._standard_price_schedule_id = standard_price_schedule_id

    @property
    def replenishment_price_schedule_id(self):
        """
        Gets the replenishment_price_schedule_id of this ProductAssignment.


        :return: The replenishment_price_schedule_id of this ProductAssignment.
        :rtype: str
        """
        return self._replenishment_price_schedule_id

    @replenishment_price_schedule_id.setter
    def replenishment_price_schedule_id(self, replenishment_price_schedule_id):
        """
        Sets the replenishment_price_schedule_id of this ProductAssignment.


        :param replenishment_price_schedule_id: The replenishment_price_schedule_id of this ProductAssignment.
        :type: str
        """

        self._replenishment_price_schedule_id = replenishment_price_schedule_id

    @property
    def user_id(self):
        """
        Gets the user_id of this ProductAssignment.


        :return: The user_id of this ProductAssignment.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ProductAssignment.


        :param user_id: The user_id of this ProductAssignment.
        :type: str
        """

        self._user_id = user_id

    @property
    def user_group_id(self):
        """
        Gets the user_group_id of this ProductAssignment.


        :return: The user_group_id of this ProductAssignment.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """
        Sets the user_group_id of this ProductAssignment.


        :param user_group_id: The user_group_id of this ProductAssignment.
        :type: str
        """

        self._user_group_id = user_group_id

    @property
    def buyer_id(self):
        """
        Gets the buyer_id of this ProductAssignment.


        :return: The buyer_id of this ProductAssignment.
        :rtype: str
        """
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, buyer_id):
        """
        Sets the buyer_id of this ProductAssignment.


        :param buyer_id: The buyer_id of this ProductAssignment.
        :type: str
        """

        self._buyer_id = buyer_id

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
