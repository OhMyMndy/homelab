# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2024.6.4
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from authentik_openapi.models.policy_test_request import PolicyTestRequest

class TestPolicyTestRequest(unittest.TestCase):
    """PolicyTestRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PolicyTestRequest:
        """Test PolicyTestRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PolicyTestRequest`
        """
        model = PolicyTestRequest()
        if include_optional:
            return PolicyTestRequest(
                user = 56,
                context = {
                    'key' : null
                    }
            )
        else:
            return PolicyTestRequest(
                user = 56,
        )
        """

    def testPolicyTestRequest(self):
        """Test PolicyTestRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
