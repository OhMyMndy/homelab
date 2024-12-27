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

from authentik_openapi.models.captcha_stage_request import CaptchaStageRequest

class TestCaptchaStageRequest(unittest.TestCase):
    """CaptchaStageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CaptchaStageRequest:
        """Test CaptchaStageRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CaptchaStageRequest`
        """
        model = CaptchaStageRequest()
        if include_optional:
            return CaptchaStageRequest(
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
                public_key = '0',
                private_key = '0',
                js_url = '0',
                api_url = '0',
                score_min_threshold = 1.337,
                score_max_threshold = 1.337,
                error_on_invalid_score = True
            )
        else:
            return CaptchaStageRequest(
                name = '0',
                public_key = '0',
                private_key = '0',
        )
        """

    def testCaptchaStageRequest(self):
        """Test CaptchaStageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()