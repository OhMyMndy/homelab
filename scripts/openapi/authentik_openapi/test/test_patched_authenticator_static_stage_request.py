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

from authentik_openapi.models.patched_authenticator_static_stage_request import PatchedAuthenticatorStaticStageRequest

class TestPatchedAuthenticatorStaticStageRequest(unittest.TestCase):
    """PatchedAuthenticatorStaticStageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedAuthenticatorStaticStageRequest:
        """Test PatchedAuthenticatorStaticStageRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedAuthenticatorStaticStageRequest`
        """
        model = PatchedAuthenticatorStaticStageRequest()
        if include_optional:
            return PatchedAuthenticatorStaticStageRequest(
                name = '0',
                flow_set = [
                    authentik_openapi.models.flow_set_request.FlowSetRequest(
                        name = '0', 
                        slug = 'z0', 
                        title = '0', 
                        designation = null, 
                        policy_engine_mode = 'all', 
                        compatibility_mode = True, 
                        layout = 'stacked', 
                        denied_action = null, )
                    ],
                configure_flow = '',
                friendly_name = '0',
                token_count = 0,
                token_length = 0
            )
        else:
            return PatchedAuthenticatorStaticStageRequest(
        )
        """

    def testPatchedAuthenticatorStaticStageRequest(self):
        """Test PatchedAuthenticatorStaticStageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()