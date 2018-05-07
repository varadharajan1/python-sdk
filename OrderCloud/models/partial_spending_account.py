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


class PartialSpendingAccount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, balance=None, allow_as_payment_method=None, redemption_code=None, start_date=None, end_date=None, xp=None):
        """
        PartialSpendingAccount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'balance': 'float',
            'allow_as_payment_method': 'bool',
            'redemption_code': 'str',
            'start_date': 'str',
            'end_date': 'str',
            'xp': 'object'
        }

        self.attribute_map = {
            'id': 'ID',
            'name': 'Name',
            'balance': 'Balance',
            'allow_as_payment_method': 'AllowAsPaymentMethod',
            'redemption_code': 'RedemptionCode',
            'start_date': 'StartDate',
            'end_date': 'EndDate',
            'xp': 'xp'
        }

        self._id = id
        self._name = name
        self._balance = balance
        self._allow_as_payment_method = allow_as_payment_method
        self._redemption_code = redemption_code
        self._start_date = start_date
        self._end_date = end_date
        self._xp = xp

    @property
    def id(self):
        """
        Gets the id of this PartialSpendingAccount.


        :return: The id of this PartialSpendingAccount.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PartialSpendingAccount.


        :param id: The id of this PartialSpendingAccount.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PartialSpendingAccount.


        :return: The name of this PartialSpendingAccount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PartialSpendingAccount.


        :param name: The name of this PartialSpendingAccount.
        :type: str
        """

        self._name = name

    @property
    def balance(self):
        """
        Gets the balance of this PartialSpendingAccount.


        :return: The balance of this PartialSpendingAccount.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """
        Sets the balance of this PartialSpendingAccount.


        :param balance: The balance of this PartialSpendingAccount.
        :type: float
        """

        self._balance = balance

    @property
    def allow_as_payment_method(self):
        """
        Gets the allow_as_payment_method of this PartialSpendingAccount.


        :return: The allow_as_payment_method of this PartialSpendingAccount.
        :rtype: bool
        """
        return self._allow_as_payment_method

    @allow_as_payment_method.setter
    def allow_as_payment_method(self, allow_as_payment_method):
        """
        Sets the allow_as_payment_method of this PartialSpendingAccount.


        :param allow_as_payment_method: The allow_as_payment_method of this PartialSpendingAccount.
        :type: bool
        """

        self._allow_as_payment_method = allow_as_payment_method

    @property
    def redemption_code(self):
        """
        Gets the redemption_code of this PartialSpendingAccount.


        :return: The redemption_code of this PartialSpendingAccount.
        :rtype: str
        """
        return self._redemption_code

    @redemption_code.setter
    def redemption_code(self, redemption_code):
        """
        Sets the redemption_code of this PartialSpendingAccount.


        :param redemption_code: The redemption_code of this PartialSpendingAccount.
        :type: str
        """

        self._redemption_code = redemption_code

    @property
    def start_date(self):
        """
        Gets the start_date of this PartialSpendingAccount.


        :return: The start_date of this PartialSpendingAccount.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this PartialSpendingAccount.


        :param start_date: The start_date of this PartialSpendingAccount.
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this PartialSpendingAccount.


        :return: The end_date of this PartialSpendingAccount.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this PartialSpendingAccount.


        :param end_date: The end_date of this PartialSpendingAccount.
        :type: str
        """

        self._end_date = end_date

    @property
    def xp(self):
        """
        Gets the xp of this PartialSpendingAccount.


        :return: The xp of this PartialSpendingAccount.
        :rtype: object
        """
        return self._xp

    @xp.setter
    def xp(self, xp):
        """
        Sets the xp of this PartialSpendingAccount.


        :param xp: The xp of this PartialSpendingAccount.
        :type: object
        """

        self._xp = xp

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