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

from authentik_openapi.models.patched_reputation_policy_request import PatchedReputationPolicyRequest

class TestPatchedReputationPolicyRequest(unittest.TestCase):
    """PatchedReputationPolicyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedReputationPolicyRequest:
        """Test PatchedReputationPolicyRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedReputationPolicyRequest`
        """
        model = PatchedReputationPolicyRequest()
        if include_optional:
            return PatchedReputationPolicyRequest(
                name = '0',
                execution_logging = True,
                check_ip = True,
                check_username = True,
                threshold = -2147483648
            )
        else:
            return PatchedReputationPolicyRequest(
        )
        """

    def testPatchedReputationPolicyRequest(self):
        """Test PatchedReputationPolicyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()