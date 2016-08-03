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


class CategoryProductAssignment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, category_id=None, product_id=None, list_order=None):
        """
        CategoryProductAssignment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category_id': 'str',
            'product_id': 'str',
            'list_order': 'int'
        }

        self.attribute_map = {
            'category_id': 'CategoryID',
            'product_id': 'ProductID',
            'list_order': 'ListOrder'
        }

        self._category_id = category_id
        self._product_id = product_id
        self._list_order = list_order

    @property
    def category_id(self):
        """
        Gets the category_id of this CategoryProductAssignment.


        :return: The category_id of this CategoryProductAssignment.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """
        Sets the category_id of this CategoryProductAssignment.


        :param category_id: The category_id of this CategoryProductAssignment.
        :type: str
        """

        self._category_id = category_id

    @property
    def product_id(self):
        """
        Gets the product_id of this CategoryProductAssignment.


        :return: The product_id of this CategoryProductAssignment.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this CategoryProductAssignment.


        :param product_id: The product_id of this CategoryProductAssignment.
        :type: str
        """

        self._product_id = product_id

    @property
    def list_order(self):
        """
        Gets the list_order of this CategoryProductAssignment.


        :return: The list_order of this CategoryProductAssignment.
        :rtype: int
        """
        return self._list_order

    @list_order.setter
    def list_order(self, list_order):
        """
        Sets the list_order of this CategoryProductAssignment.


        :param list_order: The list_order of this CategoryProductAssignment.
        :type: int
        """

        self._list_order = list_order

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
