# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.security_and_analysis_advanced_security import SecurityAndAnalysisAdvancedSecurity

class TestSecurityAndAnalysisAdvancedSecurity(unittest.TestCase):
    """SecurityAndAnalysisAdvancedSecurity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SecurityAndAnalysisAdvancedSecurity:
        """Test SecurityAndAnalysisAdvancedSecurity
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SecurityAndAnalysisAdvancedSecurity`
        """
        model = SecurityAndAnalysisAdvancedSecurity()
        if include_optional:
            return SecurityAndAnalysisAdvancedSecurity(
                status = 'enabled'
            )
        else:
            return SecurityAndAnalysisAdvancedSecurity(
        )
        """

    def testSecurityAndAnalysisAdvancedSecurity(self):
        """Test SecurityAndAnalysisAdvancedSecurity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
