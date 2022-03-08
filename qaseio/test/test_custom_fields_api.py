# coding: utf-8

"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@qase.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import qaseio
from qaseio.api.custom_fields_api import CustomFieldsApi  # noqa: E501
from qaseio.rest import ApiException


class TestCustomFieldsApi(unittest.TestCase):
    """CustomFieldsApi unit test stubs"""

    def setUp(self):
        self.api = CustomFieldsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_custom_field(self):
        """Test case for create_custom_field

        Create new Custom Field.  # noqa: E501
        """
        pass

    def test_delete_custom_field(self):
        """Test case for delete_custom_field

        Delete Custom Field by id.  # noqa: E501
        """
        pass

    def test_get_custom_field(self):
        """Test case for get_custom_field

        Get Custom Field by id.  # noqa: E501
        """
        pass

    def test_get_custom_fields(self):
        """Test case for get_custom_fields

        Get all Custom Fields.  # noqa: E501
        """
        pass

    def test_update_custom_field(self):
        """Test case for update_custom_field

        Update Custom Field by id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
