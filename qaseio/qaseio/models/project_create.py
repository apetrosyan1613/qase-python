# coding: utf-8

"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@qase.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProjectCreate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'title': 'str',
        'code': 'str',
        'description': 'str',
        'access': 'str',
        'group': 'str'
    }

    attribute_map = {
        'title': 'title',
        'code': 'code',
        'description': 'description',
        'access': 'access',
        'group': 'group'
    }

    def __init__(self, title=None, code=None, description=None, access=None, group=None):  # noqa: E501
        """ProjectCreate - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._code = None
        self._description = None
        self._access = None
        self._group = None
        self.discriminator = None
        self.title = title
        self.code = code
        if description is not None:
            self.description = description
        if access is not None:
            self.access = access
        if group is not None:
            self.group = group

    @property
    def title(self):
        """Gets the title of this ProjectCreate.  # noqa: E501

        Project title.  # noqa: E501

        :return: The title of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProjectCreate.

        Project title.  # noqa: E501

        :param title: The title of this ProjectCreate.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def code(self):
        """Gets the code of this ProjectCreate.  # noqa: E501

        Project code. Unique for team. Digits and special characters are not allowed.  # noqa: E501

        :return: The code of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ProjectCreate.

        Project code. Unique for team. Digits and special characters are not allowed.  # noqa: E501

        :param code: The code of this ProjectCreate.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def description(self):
        """Gets the description of this ProjectCreate.  # noqa: E501

        Project description.  # noqa: E501

        :return: The description of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectCreate.

        Project description.  # noqa: E501

        :param description: The description of this ProjectCreate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def access(self):
        """Gets the access of this ProjectCreate.  # noqa: E501


        :return: The access of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this ProjectCreate.


        :param access: The access of this ProjectCreate.  # noqa: E501
        :type: str
        """
        allowed_values = ["all", "group", "none"]  # noqa: E501
        if access not in allowed_values:
            raise ValueError(
                "Invalid value for `access` ({0}), must be one of {1}"  # noqa: E501
                .format(access, allowed_values)
            )

        self._access = access

    @property
    def group(self):
        """Gets the group of this ProjectCreate.  # noqa: E501

        Team group hash. Required if access param is set to group.  # noqa: E501

        :return: The group of this ProjectCreate.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ProjectCreate.

        Team group hash. Required if access param is set to group.  # noqa: E501

        :param group: The group of this ProjectCreate.  # noqa: E501
        :type: str
        """

        self._group = group

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ProjectCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
