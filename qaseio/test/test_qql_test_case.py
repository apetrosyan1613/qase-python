"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qaseio
from qaseio.model.attachment import Attachment
from qaseio.model.custom_field_value import CustomFieldValue
from qaseio.model.tag_value import TagValue
from qaseio.model.test_case_params import TestCaseParams
from qaseio.model.test_step import TestStep
globals()['Attachment'] = Attachment
globals()['CustomFieldValue'] = CustomFieldValue
globals()['TagValue'] = TagValue
globals()['TestCaseParams'] = TestCaseParams
globals()['TestStep'] = TestStep
from qaseio.model.qql_test_case import QqlTestCase


class TestQqlTestCase(unittest.TestCase):
    """QqlTestCase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testQqlTestCase(self):
        """Test QqlTestCase"""
        # FIXME: construct object with mandatory attributes with example values
        # model = QqlTestCase()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
