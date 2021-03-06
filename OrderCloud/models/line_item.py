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


class LineItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, xp=None, id=None, product_id=None, quantity=None, date_added=None, quantity_shipped=None, unit_price=None, line_total=None, cost_center=None, date_needed=None, shipping_account=None, shipping_address_id=None, ship_from_address_id=None, product=None, shipping_address=None, ship_from_address=None, specs=None):
        """
        LineItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'xp': 'object',
            'id': 'str',
            'product_id': 'str',
            'quantity': 'int',
            'date_added': 'str',
            'quantity_shipped': 'int',
            'unit_price': 'float',
            'line_total': 'float',
            'cost_center': 'str',
            'date_needed': 'str',
            'shipping_account': 'str',
            'shipping_address_id': 'str',
            'ship_from_address_id': 'str',
            'product': 'LineItemProduct',
            'shipping_address': 'Address',
            'ship_from_address': 'Address',
            'specs': 'list[LineItemSpec]'
        }

        self.attribute_map = {
            'xp': 'xp',
            'id': 'ID',
            'product_id': 'ProductID',
            'quantity': 'Quantity',
            'date_added': 'DateAdded',
            'quantity_shipped': 'QuantityShipped',
            'unit_price': 'UnitPrice',
            'line_total': 'LineTotal',
            'cost_center': 'CostCenter',
            'date_needed': 'DateNeeded',
            'shipping_account': 'ShippingAccount',
            'shipping_address_id': 'ShippingAddressID',
            'ship_from_address_id': 'ShipFromAddressID',
            'product': 'Product',
            'shipping_address': 'ShippingAddress',
            'ship_from_address': 'ShipFromAddress',
            'specs': 'Specs'
        }

        self._xp = xp
        self._id = id
        self._product_id = product_id
        self._quantity = quantity
        self._date_added = date_added
        self._quantity_shipped = quantity_shipped
        self._unit_price = unit_price
        self._line_total = line_total
        self._cost_center = cost_center
        self._date_needed = date_needed
        self._shipping_account = shipping_account
        self._shipping_address_id = shipping_address_id
        self._ship_from_address_id = ship_from_address_id
        self._product = product
        self._shipping_address = shipping_address
        self._ship_from_address = ship_from_address
        self._specs = specs

    @property
    def xp(self):
        """
        Gets the xp of this LineItem.


        :return: The xp of this LineItem.
        :rtype: object
        """
        return self._xp

    @xp.setter
    def xp(self, xp):
        """
        Sets the xp of this LineItem.


        :param xp: The xp of this LineItem.
        :type: object
        """

        self._xp = xp

    @property
    def id(self):
        """
        Gets the id of this LineItem.


        :return: The id of this LineItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LineItem.


        :param id: The id of this LineItem.
        :type: str
        """

        self._id = id

    @property
    def product_id(self):
        """
        Gets the product_id of this LineItem.


        :return: The product_id of this LineItem.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this LineItem.


        :param product_id: The product_id of this LineItem.
        :type: str
        """

        self._product_id = product_id

    @property
    def quantity(self):
        """
        Gets the quantity of this LineItem.


        :return: The quantity of this LineItem.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this LineItem.


        :param quantity: The quantity of this LineItem.
        :type: int
        """

        self._quantity = quantity

    @property
    def date_added(self):
        """
        Gets the date_added of this LineItem.


        :return: The date_added of this LineItem.
        :rtype: str
        """
        return self._date_added

    @date_added.setter
    def date_added(self, date_added):
        """
        Sets the date_added of this LineItem.


        :param date_added: The date_added of this LineItem.
        :type: str
        """

        self._date_added = date_added

    @property
    def quantity_shipped(self):
        """
        Gets the quantity_shipped of this LineItem.


        :return: The quantity_shipped of this LineItem.
        :rtype: int
        """
        return self._quantity_shipped

    @quantity_shipped.setter
    def quantity_shipped(self, quantity_shipped):
        """
        Sets the quantity_shipped of this LineItem.


        :param quantity_shipped: The quantity_shipped of this LineItem.
        :type: int
        """

        self._quantity_shipped = quantity_shipped

    @property
    def unit_price(self):
        """
        Gets the unit_price of this LineItem.


        :return: The unit_price of this LineItem.
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """
        Sets the unit_price of this LineItem.


        :param unit_price: The unit_price of this LineItem.
        :type: float
        """

        self._unit_price = unit_price

    @property
    def line_total(self):
        """
        Gets the line_total of this LineItem.


        :return: The line_total of this LineItem.
        :rtype: float
        """
        return self._line_total

    @line_total.setter
    def line_total(self, line_total):
        """
        Sets the line_total of this LineItem.


        :param line_total: The line_total of this LineItem.
        :type: float
        """

        self._line_total = line_total

    @property
    def cost_center(self):
        """
        Gets the cost_center of this LineItem.


        :return: The cost_center of this LineItem.
        :rtype: str
        """
        return self._cost_center

    @cost_center.setter
    def cost_center(self, cost_center):
        """
        Sets the cost_center of this LineItem.


        :param cost_center: The cost_center of this LineItem.
        :type: str
        """

        self._cost_center = cost_center

    @property
    def date_needed(self):
        """
        Gets the date_needed of this LineItem.


        :return: The date_needed of this LineItem.
        :rtype: str
        """
        return self._date_needed

    @date_needed.setter
    def date_needed(self, date_needed):
        """
        Sets the date_needed of this LineItem.


        :param date_needed: The date_needed of this LineItem.
        :type: str
        """

        self._date_needed = date_needed

    @property
    def shipping_account(self):
        """
        Gets the shipping_account of this LineItem.


        :return: The shipping_account of this LineItem.
        :rtype: str
        """
        return self._shipping_account

    @shipping_account.setter
    def shipping_account(self, shipping_account):
        """
        Sets the shipping_account of this LineItem.


        :param shipping_account: The shipping_account of this LineItem.
        :type: str
        """

        self._shipping_account = shipping_account

    @property
    def shipping_address_id(self):
        """
        Gets the shipping_address_id of this LineItem.


        :return: The shipping_address_id of this LineItem.
        :rtype: str
        """
        return self._shipping_address_id

    @shipping_address_id.setter
    def shipping_address_id(self, shipping_address_id):
        """
        Sets the shipping_address_id of this LineItem.


        :param shipping_address_id: The shipping_address_id of this LineItem.
        :type: str
        """

        self._shipping_address_id = shipping_address_id

    @property
    def ship_from_address_id(self):
        """
        Gets the ship_from_address_id of this LineItem.


        :return: The ship_from_address_id of this LineItem.
        :rtype: str
        """
        return self._ship_from_address_id

    @ship_from_address_id.setter
    def ship_from_address_id(self, ship_from_address_id):
        """
        Sets the ship_from_address_id of this LineItem.


        :param ship_from_address_id: The ship_from_address_id of this LineItem.
        :type: str
        """

        self._ship_from_address_id = ship_from_address_id

    @property
    def product(self):
        """
        Gets the product of this LineItem.


        :return: The product of this LineItem.
        :rtype: LineItemProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """
        Sets the product of this LineItem.


        :param product: The product of this LineItem.
        :type: LineItemProduct
        """

        self._product = product

    @property
    def shipping_address(self):
        """
        Gets the shipping_address of this LineItem.


        :return: The shipping_address of this LineItem.
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """
        Sets the shipping_address of this LineItem.


        :param shipping_address: The shipping_address of this LineItem.
        :type: Address
        """

        self._shipping_address = shipping_address

    @property
    def ship_from_address(self):
        """
        Gets the ship_from_address of this LineItem.


        :return: The ship_from_address of this LineItem.
        :rtype: Address
        """
        return self._ship_from_address

    @ship_from_address.setter
    def ship_from_address(self, ship_from_address):
        """
        Sets the ship_from_address of this LineItem.


        :param ship_from_address: The ship_from_address of this LineItem.
        :type: Address
        """

        self._ship_from_address = ship_from_address

    @property
    def specs(self):
        """
        Gets the specs of this LineItem.


        :return: The specs of this LineItem.
        :rtype: list[LineItemSpec]
        """
        return self._specs

    @specs.setter
    def specs(self, specs):
        """
        Sets the specs of this LineItem.


        :param specs: The specs of this LineItem.
        :type: list[LineItemSpec]
        """

        self._specs = specs

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
