# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repos_update_status_check_protection_request import ReposUpdateStatusCheckProtectionRequest

class TestReposUpdateStatusCheckProtectionRequest(unittest.TestCase):
    """ReposUpdateStatusCheckProtectionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReposUpdateStatusCheckProtectionRequest:
        """Test ReposUpdateStatusCheckProtectionRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReposUpdateStatusCheckProtectionRequest`
        """
        model = ReposUpdateStatusCheckProtectionRequest()
        if include_optional:
            return ReposUpdateStatusCheckProtectionRequest(
                strict = True,
                contexts = [
                    ''
                    ],
                checks = [
                    github_openapi.models.repos_update_branch_protection_request_required_status_checks_checks_inner.repos_update_branch_protection_request_required_status_checks_checks_inner(
                        context = '', 
                        app_id = 56, )
                    ]
            )
        else:
            return ReposUpdateStatusCheckProtectionRequest(
        )
        """

    def testReposUpdateStatusCheckProtectionRequest(self):
        """Test ReposUpdateStatusCheckProtectionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
