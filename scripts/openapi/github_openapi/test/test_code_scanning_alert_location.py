# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.code_scanning_alert_location import CodeScanningAlertLocation

class TestCodeScanningAlertLocation(unittest.TestCase):
    """CodeScanningAlertLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CodeScanningAlertLocation:
        """Test CodeScanningAlertLocation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodeScanningAlertLocation`
        """
        model = CodeScanningAlertLocation()
        if include_optional:
            return CodeScanningAlertLocation(
                path = '',
                start_line = 56,
                end_line = 56,
                start_column = 56,
                end_column = 56
            )
        else:
            return CodeScanningAlertLocation(
        )
        """

    def testCodeScanningAlertLocation(self):
        """Test CodeScanningAlertLocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
