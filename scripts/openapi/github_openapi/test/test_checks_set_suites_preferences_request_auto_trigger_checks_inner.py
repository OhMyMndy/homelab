# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.checks_set_suites_preferences_request_auto_trigger_checks_inner import ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner

class TestChecksSetSuitesPreferencesRequestAutoTriggerChecksInner(unittest.TestCase):
    """ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner:
        """Test ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner`
        """
        model = ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner()
        if include_optional:
            return ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner(
                app_id = 56,
                setting = True
            )
        else:
            return ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner(
                app_id = 56,
                setting = True,
        )
        """

    def testChecksSetSuitesPreferencesRequestAutoTriggerChecksInner(self):
        """Test ChecksSetSuitesPreferencesRequestAutoTriggerChecksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
