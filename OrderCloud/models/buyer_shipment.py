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


class BuyerShipment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, shipper=None, date_shipped=None, date_delivered=None, tracking_number=None, cost=None, xp=None, account=None, from_address_id=None, to_address_id=None, from_address=None, to_address=None):
        """
        BuyerShipment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'shipper': 'str',
            'date_shipped': 'str',
            'date_delivered': 'str',
            'tracking_number': 'str',
            'cost': 'float',
            'xp': 'object',
            'account': 'str',
            'from_address_id': 'str',
            'to_address_id': 'str',
            'from_address': 'Address',
            'to_address': 'Address'
        }

        self.attribute_map = {
            'id': 'ID',
            'shipper': 'Shipper',
            'date_shipped': 'DateShipped',
            'date_delivered': 'DateDelivered',
            'tracking_number': 'TrackingNumber',
            'cost': 'Cost',
            'xp': 'xp',
            'account': 'Account',
            'from_address_id': 'FromAddressID',
            'to_address_id': 'ToAddressID',
            'from_address': 'FromAddress',
            'to_address': 'ToAddress'
        }

        self._id = id
        self._shipper = shipper
        self._date_shipped = date_shipped
        self._date_delivered = date_delivered
        self._tracking_number = tracking_number
        self._cost = cost
        self._xp = xp
        self._account = account
        self._from_address_id = from_address_id
        self._to_address_id = to_address_id
        self._from_address = from_address
        self._to_address = to_address

    @property
    def id(self):
        """
        Gets the id of this BuyerShipment.


        :return: The id of this BuyerShipment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuyerShipment.


        :param id: The id of this BuyerShipment.
        :type: str
        """

        self._id = id

    @property
    def shipper(self):
        """
        Gets the shipper of this BuyerShipment.


        :return: The shipper of this BuyerShipment.
        :rtype: str
        """
        return self._shipper

    @shipper.setter
    def shipper(self, shipper):
        """
        Sets the shipper of this BuyerShipment.


        :param shipper: The shipper of this BuyerShipment.
        :type: str
        """

        self._shipper = shipper

    @property
    def date_shipped(self):
        """
        Gets the date_shipped of this BuyerShipment.


        :return: The date_shipped of this BuyerShipment.
        :rtype: str
        """
        return self._date_shipped

    @date_shipped.setter
    def date_shipped(self, date_shipped):
        """
        Sets the date_shipped of this BuyerShipment.


        :param date_shipped: The date_shipped of this BuyerShipment.
        :type: str
        """

        self._date_shipped = date_shipped

    @property
    def date_delivered(self):
        """
        Gets the date_delivered of this BuyerShipment.


        :return: The date_delivered of this BuyerShipment.
        :rtype: str
        """
        return self._date_delivered

    @date_delivered.setter
    def date_delivered(self, date_delivered):
        """
        Sets the date_delivered of this BuyerShipment.


        :param date_delivered: The date_delivered of this BuyerShipment.
        :type: str
        """

        self._date_delivered = date_delivered

    @property
    def tracking_number(self):
        """
        Gets the tracking_number of this BuyerShipment.


        :return: The tracking_number of this BuyerShipment.
        :rtype: str
        """
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        """
        Sets the tracking_number of this BuyerShipment.


        :param tracking_number: The tracking_number of this BuyerShipment.
        :type: str
        """

        self._tracking_number = tracking_number

    @property
    def cost(self):
        """
        Gets the cost of this BuyerShipment.


        :return: The cost of this BuyerShipment.
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this BuyerShipment.


        :param cost: The cost of this BuyerShipment.
        :type: float
        """

        self._cost = cost

    @property
    def xp(self):
        """
        Gets the xp of this BuyerShipment.


        :return: The xp of this BuyerShipment.
        :rtype: object
        """
        return self._xp

    @xp.setter
    def xp(self, xp):
        """
        Sets the xp of this BuyerShipment.


        :param xp: The xp of this BuyerShipment.
        :type: object
        """

        self._xp = xp

    @property
    def account(self):
        """
        Gets the account of this BuyerShipment.


        :return: The account of this BuyerShipment.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this BuyerShipment.


        :param account: The account of this BuyerShipment.
        :type: str
        """

        self._account = account

    @property
    def from_address_id(self):
        """
        Gets the from_address_id of this BuyerShipment.


        :return: The from_address_id of this BuyerShipment.
        :rtype: str
        """
        return self._from_address_id

    @from_address_id.setter
    def from_address_id(self, from_address_id):
        """
        Sets the from_address_id of this BuyerShipment.


        :param from_address_id: The from_address_id of this BuyerShipment.
        :type: str
        """

        self._from_address_id = from_address_id

    @property
    def to_address_id(self):
        """
        Gets the to_address_id of this BuyerShipment.


        :return: The to_address_id of this BuyerShipment.
        :rtype: str
        """
        return self._to_address_id

    @to_address_id.setter
    def to_address_id(self, to_address_id):
        """
        Sets the to_address_id of this BuyerShipment.


        :param to_address_id: The to_address_id of this BuyerShipment.
        :type: str
        """

        self._to_address_id = to_address_id

    @property
    def from_address(self):
        """
        Gets the from_address of this BuyerShipment.


        :return: The from_address of this BuyerShipment.
        :rtype: Address
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """
        Sets the from_address of this BuyerShipment.


        :param from_address: The from_address of this BuyerShipment.
        :type: Address
        """

        self._from_address = from_address

    @property
    def to_address(self):
        """
        Gets the to_address of this BuyerShipment.


        :return: The to_address of this BuyerShipment.
        :rtype: Address
        """
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        """
        Sets the to_address of this BuyerShipment.


        :param to_address: The to_address of this BuyerShipment.
        :type: Address
        """

        self._to_address = to_address

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
