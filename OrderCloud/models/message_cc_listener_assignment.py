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


class MessageCCListenerAssignment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, message_sender_assignment=None, message_config_name=None, message_config_description=None, message_type=None, buyer_id=None, user_group_id=None, user_id=None):
        """
        MessageCCListenerAssignment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message_sender_assignment': 'MessageSenderAssignment',
            'message_config_name': 'str',
            'message_config_description': 'str',
            'message_type': 'str',
            'buyer_id': 'str',
            'user_group_id': 'str',
            'user_id': 'str'
        }

        self.attribute_map = {
            'message_sender_assignment': 'MessageSenderAssignment',
            'message_config_name': 'MessageConfigName',
            'message_config_description': 'MessageConfigDescription',
            'message_type': 'MessageType',
            'buyer_id': 'BuyerID',
            'user_group_id': 'UserGroupID',
            'user_id': 'UserID'
        }

        self._message_sender_assignment = message_sender_assignment
        self._message_config_name = message_config_name
        self._message_config_description = message_config_description
        self._message_type = message_type
        self._buyer_id = buyer_id
        self._user_group_id = user_group_id
        self._user_id = user_id

    @property
    def message_sender_assignment(self):
        """
        Gets the message_sender_assignment of this MessageCCListenerAssignment.


        :return: The message_sender_assignment of this MessageCCListenerAssignment.
        :rtype: MessageSenderAssignment
        """
        return self._message_sender_assignment

    @message_sender_assignment.setter
    def message_sender_assignment(self, message_sender_assignment):
        """
        Sets the message_sender_assignment of this MessageCCListenerAssignment.


        :param message_sender_assignment: The message_sender_assignment of this MessageCCListenerAssignment.
        :type: MessageSenderAssignment
        """

        self._message_sender_assignment = message_sender_assignment

    @property
    def message_config_name(self):
        """
        Gets the message_config_name of this MessageCCListenerAssignment.


        :return: The message_config_name of this MessageCCListenerAssignment.
        :rtype: str
        """
        return self._message_config_name

    @message_config_name.setter
    def message_config_name(self, message_config_name):
        """
        Sets the message_config_name of this MessageCCListenerAssignment.


        :param message_config_name: The message_config_name of this MessageCCListenerAssignment.
        :type: str
        """

        self._message_config_name = message_config_name

    @property
    def message_config_description(self):
        """
        Gets the message_config_description of this MessageCCListenerAssignment.


        :return: The message_config_description of this MessageCCListenerAssignment.
        :rtype: str
        """
        return self._message_config_description

    @message_config_description.setter
    def message_config_description(self, message_config_description):
        """
        Sets the message_config_description of this MessageCCListenerAssignment.


        :param message_config_description: The message_config_description of this MessageCCListenerAssignment.
        :type: str
        """

        self._message_config_description = message_config_description

    @property
    def message_type(self):
        """
        Gets the message_type of this MessageCCListenerAssignment.


        :return: The message_type of this MessageCCListenerAssignment.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """
        Sets the message_type of this MessageCCListenerAssignment.


        :param message_type: The message_type of this MessageCCListenerAssignment.
        :type: str
        """

        self._message_type = message_type

    @property
    def buyer_id(self):
        """
        Gets the buyer_id of this MessageCCListenerAssignment.


        :return: The buyer_id of this MessageCCListenerAssignment.
        :rtype: str
        """
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, buyer_id):
        """
        Sets the buyer_id of this MessageCCListenerAssignment.


        :param buyer_id: The buyer_id of this MessageCCListenerAssignment.
        :type: str
        """

        self._buyer_id = buyer_id

    @property
    def user_group_id(self):
        """
        Gets the user_group_id of this MessageCCListenerAssignment.


        :return: The user_group_id of this MessageCCListenerAssignment.
        :rtype: str
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """
        Sets the user_group_id of this MessageCCListenerAssignment.


        :param user_group_id: The user_group_id of this MessageCCListenerAssignment.
        :type: str
        """

        self._user_group_id = user_group_id

    @property
    def user_id(self):
        """
        Gets the user_id of this MessageCCListenerAssignment.


        :return: The user_id of this MessageCCListenerAssignment.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this MessageCCListenerAssignment.


        :param user_id: The user_id of this MessageCCListenerAssignment.
        :type: str
        """

        self._user_id = user_id

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
