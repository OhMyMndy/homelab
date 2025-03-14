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

from authentik_openapi.models.authenticator_totp_challenge import AuthenticatorTOTPChallenge

class TestAuthenticatorTOTPChallenge(unittest.TestCase):
    """AuthenticatorTOTPChallenge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthenticatorTOTPChallenge:
        """Test AuthenticatorTOTPChallenge
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthenticatorTOTPChallenge`
        """
        model = AuthenticatorTOTPChallenge()
        if include_optional:
            return AuthenticatorTOTPChallenge(
                type = 'native',
                flow_info = authentik_openapi.models.contextual_flow_info.ContextualFlowInfo(
                    title = '', 
                    background = '', 
                    cancel_url = '', 
                    layout = 'stacked', ),
                component = 'ak-stage-authenticator-totp',
                response_errors = {
                    'key' : [
                        authentik_openapi.models.error_detail.ErrorDetail(
                            string = '', 
                            code = '', )
                        ]
                    },
                pending_user = '',
                pending_user_avatar = '',
                config_url = ''
            )
        else:
            return AuthenticatorTOTPChallenge(
                type = 'native',
                pending_user = '',
                pending_user_avatar = '',
                config_url = '',
        )
        """

    def testAuthenticatorTOTPChallenge(self):
        """Test AuthenticatorTOTPChallenge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
