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


class Category(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, description=None, xp=None, list_order=None, active=None, parent_id=None, child_count=None):
        """
        Category - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'xp': 'object',
            'list_order': 'int',
            'active': 'bool',
            'parent_id': 'str',
            'child_count': 'int'
        }

        self.attribute_map = {
            'id': 'ID',
            'name': 'Name',
            'description': 'Description',
            'xp': 'xp',
            'list_order': 'ListOrder',
            'active': 'Active',
            'parent_id': 'ParentID',
            'child_count': 'ChildCount'
        }

        self._id = id
        self._name = name
        self._description = description
        self._xp = xp
        self._list_order = list_order
        self._active = active
        self._parent_id = parent_id
        self._child_count = child_count

    @property
    def id(self):
        """
        Gets the id of this Category.


        :return: The id of this Category.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Category.


        :param id: The id of this Category.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Category.


        :return: The name of this Category.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Category.


        :param name: The name of this Category.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Category.


        :return: The description of this Category.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Category.


        :param description: The description of this Category.
        :type: str
        """

        self._description = description

    @property
    def xp(self):
        """
        Gets the xp of this Category.


        :return: The xp of this Category.
        :rtype: object
        """
        return self._xp

    @xp.setter
    def xp(self, xp):
        """
        Sets the xp of this Category.


        :param xp: The xp of this Category.
        :type: object
        """

        self._xp = xp

    @property
    def list_order(self):
        """
        Gets the list_order of this Category.


        :return: The list_order of this Category.
        :rtype: int
        """
        return self._list_order

    @list_order.setter
    def list_order(self, list_order):
        """
        Sets the list_order of this Category.


        :param list_order: The list_order of this Category.
        :type: int
        """

        self._list_order = list_order

    @property
    def active(self):
        """
        Gets the active of this Category.


        :return: The active of this Category.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Category.


        :param active: The active of this Category.
        :type: bool
        """

        self._active = active

    @property
    def parent_id(self):
        """
        Gets the parent_id of this Category.


        :return: The parent_id of this Category.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this Category.


        :param parent_id: The parent_id of this Category.
        :type: str
        """

        self._parent_id = parent_id

    @property
    def child_count(self):
        """
        Gets the child_count of this Category.


        :return: The child_count of this Category.
        :rtype: int
        """
        return self._child_count

    @child_count.setter
    def child_count(self, child_count):
        """
        Sets the child_count of this Category.


        :param child_count: The child_count of this Category.
        :type: int
        """

        self._child_count = child_count

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
