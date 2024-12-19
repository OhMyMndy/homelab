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

from authentik_openapi.models.patched_flow_stage_binding_request import PatchedFlowStageBindingRequest

class TestPatchedFlowStageBindingRequest(unittest.TestCase):
    """PatchedFlowStageBindingRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedFlowStageBindingRequest:
        """Test PatchedFlowStageBindingRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedFlowStageBindingRequest`
        """
        model = PatchedFlowStageBindingRequest()
        if include_optional:
            return PatchedFlowStageBindingRequest(
                target = '',
                stage = '',
                evaluate_on_plan = True,
                re_evaluate_policies = True,
                order = -2147483648,
                policy_engine_mode = 'all',
                invalid_response_action = 'retry'
            )
        else:
            return PatchedFlowStageBindingRequest(
        )
        """

    def testPatchedFlowStageBindingRequest(self):
        """Test PatchedFlowStageBindingRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
