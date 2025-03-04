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

from authentik_openapi.models.o_auth_device_code_finish_challenge_response_request import OAuthDeviceCodeFinishChallengeResponseRequest

class TestOAuthDeviceCodeFinishChallengeResponseRequest(unittest.TestCase):
    """OAuthDeviceCodeFinishChallengeResponseRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OAuthDeviceCodeFinishChallengeResponseRequest:
        """Test OAuthDeviceCodeFinishChallengeResponseRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuthDeviceCodeFinishChallengeResponseRequest`
        """
        model = OAuthDeviceCodeFinishChallengeResponseRequest()
        if include_optional:
            return OAuthDeviceCodeFinishChallengeResponseRequest(
                component = 'ak-provider-oauth2-device-code-finish'
            )
        else:
            return OAuthDeviceCodeFinishChallengeResponseRequest(
        )
        """

    def testOAuthDeviceCodeFinishChallengeResponseRequest(self):
        """Test OAuthDeviceCodeFinishChallengeResponseRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
