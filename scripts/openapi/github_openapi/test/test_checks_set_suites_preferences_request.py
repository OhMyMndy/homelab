# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.checks_set_suites_preferences_request import ChecksSetSuitesPreferencesRequest

class TestChecksSetSuitesPreferencesRequest(unittest.TestCase):
    """ChecksSetSuitesPreferencesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecksSetSuitesPreferencesRequest:
        """Test ChecksSetSuitesPreferencesRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecksSetSuitesPreferencesRequest`
        """
        model = ChecksSetSuitesPreferencesRequest()
        if include_optional:
            return ChecksSetSuitesPreferencesRequest(
                auto_trigger_checks = [
                    github_openapi.models.checks_set_suites_preferences_request_auto_trigger_checks_inner.checks_set_suites_preferences_request_auto_trigger_checks_inner(
                        app_id = 56, 
                        setting = True, )
                    ]
            )
        else:
            return ChecksSetSuitesPreferencesRequest(
        )
        """

    def testChecksSetSuitesPreferencesRequest(self):
        """Test ChecksSetSuitesPreferencesRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
