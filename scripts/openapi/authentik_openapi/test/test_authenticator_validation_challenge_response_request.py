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

from authentik_openapi.models.authenticator_validation_challenge_response_request import AuthenticatorValidationChallengeResponseRequest

class TestAuthenticatorValidationChallengeResponseRequest(unittest.TestCase):
    """AuthenticatorValidationChallengeResponseRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthenticatorValidationChallengeResponseRequest:
        """Test AuthenticatorValidationChallengeResponseRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthenticatorValidationChallengeResponseRequest`
        """
        model = AuthenticatorValidationChallengeResponseRequest()
        if include_optional:
            return AuthenticatorValidationChallengeResponseRequest(
                component = 'ak-stage-authenticator-validate',
                selected_challenge = authentik_openapi.models.device_challenge_request.DeviceChallengeRequest(
                    device_class = '0', 
                    device_uid = '0', 
                    challenge = {
                        'key' : null
                        }, ),
                selected_stage = '0',
                code = '0',
                webauthn = {
                    'key' : null
                    },
                duo = 56
            )
        else:
            return AuthenticatorValidationChallengeResponseRequest(
        )
        """

    def testAuthenticatorValidationChallengeResponseRequest(self):
        """Test AuthenticatorValidationChallengeResponseRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()