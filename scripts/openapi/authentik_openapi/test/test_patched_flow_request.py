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

from authentik_openapi.models.patched_flow_request import PatchedFlowRequest

class TestPatchedFlowRequest(unittest.TestCase):
    """PatchedFlowRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedFlowRequest:
        """Test PatchedFlowRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedFlowRequest`
        """
        model = PatchedFlowRequest()
        if include_optional:
            return PatchedFlowRequest(
                name = '0',
                slug = 'z0',
                title = '0',
                designation = 'authentication',
                policy_engine_mode = 'all',
                compatibility_mode = True,
                layout = 'stacked',
                denied_action = 'message_continue',
                authentication = 'none'
            )
        else:
            return PatchedFlowRequest(
        )
        """

    def testPatchedFlowRequest(self):
        """Test PatchedFlowRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()