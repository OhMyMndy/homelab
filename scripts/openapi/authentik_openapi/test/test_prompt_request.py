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

from authentik_openapi.models.prompt_request import PromptRequest

class TestPromptRequest(unittest.TestCase):
    """PromptRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PromptRequest:
        """Test PromptRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PromptRequest`
        """
        model = PromptRequest()
        if include_optional:
            return PromptRequest(
                name = '0',
                field_key = '0',
                label = '0',
                type = 'text',
                required = True,
                placeholder = '',
                initial_value = '',
                order = -2147483648,
                promptstage_set = [
                    authentik_openapi.models.stage_request.StageRequest(
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
                            ], )
                    ],
                sub_text = '',
                placeholder_expression = True,
                initial_value_expression = True
            )
        else:
            return PromptRequest(
                name = '0',
                field_key = '0',
                label = '0',
                type = 'text',
        )
        """

    def testPromptRequest(self):
        """Test PromptRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
