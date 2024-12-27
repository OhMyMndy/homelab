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

from authentik_openapi.models.policy_request import PolicyRequest

class TestPolicyRequest(unittest.TestCase):
    """PolicyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PolicyRequest:
        """Test PolicyRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PolicyRequest`
        """
        model = PolicyRequest()
        if include_optional:
            return PolicyRequest(
                name = '0',
                execution_logging = True
            )
        else:
            return PolicyRequest(
                name = '0',
        )
        """

    def testPolicyRequest(self):
        """Test PolicyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()