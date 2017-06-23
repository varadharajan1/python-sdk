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


class CatalogAssignment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, catalog_id=None, buyer_id=None, view_all_categories=None, view_all_products=None):
        """
        CatalogAssignment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'catalog_id': 'str',
            'buyer_id': 'str',
            'view_all_categories': 'bool',
            'view_all_products': 'bool'
        }

        self.attribute_map = {
            'catalog_id': 'CatalogID',
            'buyer_id': 'BuyerID',
            'view_all_categories': 'ViewAllCategories',
            'view_all_products': 'ViewAllProducts'
        }

        self._catalog_id = catalog_id
        self._buyer_id = buyer_id
        self._view_all_categories = view_all_categories
        self._view_all_products = view_all_products

    @property
    def catalog_id(self):
        """
        Gets the catalog_id of this CatalogAssignment.


        :return: The catalog_id of this CatalogAssignment.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """
        Sets the catalog_id of this CatalogAssignment.


        :param catalog_id: The catalog_id of this CatalogAssignment.
        :type: str
        """

        self._catalog_id = catalog_id

    @property
    def buyer_id(self):
        """
        Gets the buyer_id of this CatalogAssignment.


        :return: The buyer_id of this CatalogAssignment.
        :rtype: str
        """
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, buyer_id):
        """
        Sets the buyer_id of this CatalogAssignment.


        :param buyer_id: The buyer_id of this CatalogAssignment.
        :type: str
        """

        self._buyer_id = buyer_id

    @property
    def view_all_categories(self):
        """
        Gets the view_all_categories of this CatalogAssignment.


        :return: The view_all_categories of this CatalogAssignment.
        :rtype: bool
        """
        return self._view_all_categories

    @view_all_categories.setter
    def view_all_categories(self, view_all_categories):
        """
        Sets the view_all_categories of this CatalogAssignment.


        :param view_all_categories: The view_all_categories of this CatalogAssignment.
        :type: bool
        """

        self._view_all_categories = view_all_categories

    @property
    def view_all_products(self):
        """
        Gets the view_all_products of this CatalogAssignment.


        :return: The view_all_products of this CatalogAssignment.
        :rtype: bool
        """
        return self._view_all_products

    @view_all_products.setter
    def view_all_products(self, view_all_products):
        """
        Sets the view_all_products of this CatalogAssignment.


        :param view_all_products: The view_all_products of this CatalogAssignment.
        :type: bool
        """

        self._view_all_products = view_all_products

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
