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

from authentik_openapi.models.authenticator_sms_stage import AuthenticatorSMSStage

class TestAuthenticatorSMSStage(unittest.TestCase):
    """AuthenticatorSMSStage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthenticatorSMSStage:
        """Test AuthenticatorSMSStage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthenticatorSMSStage`
        """
        model = AuthenticatorSMSStage()
        if include_optional:
            return AuthenticatorSMSStage(
                pk = '',
                name = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                flow_set = [
                    authentik_openapi.models.flow_set.FlowSet(
                        pk = '', 
                        policybindingmodel_ptr_id = '', 
                        name = '', 
                        slug = 'z', 
                        title = '', 
                        designation = null, 
                        background = '', 
                        policy_engine_mode = 'all', 
                        compatibility_mode = True, 
                        export_url = '', 
                        layout = 'stacked', 
                        denied_action = null, )
                    ],
                configure_flow = '',
                friendly_name = '',
                provider = 'twilio',
                from_number = '',
                account_sid = '',
                auth = '',
                auth_password = '',
                auth_type = 'basic',
                verify_only = True,
                mapping = ''
            )
        else:
            return AuthenticatorSMSStage(
                pk = '',
                name = '',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                provider = 'twilio',
                from_number = '',
                account_sid = '',
                auth = '',
        )
        """

    def testAuthenticatorSMSStage(self):
        """Test AuthenticatorSMSStage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
