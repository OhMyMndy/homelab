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

from authentik_openapi.models.application import Application

class TestApplication(unittest.TestCase):
    """Application unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Application:
        """Test Application
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Application`
        """
        model = Application()
        if include_optional:
            return Application(
                pk = '',
                name = '',
                slug = 'z',
                provider = 56,
                provider_obj = authentik_openapi.models.provider.Provider(
                    pk = 56, 
                    name = '', 
                    authentication_flow = '', 
                    authorization_flow = '', 
                    property_mappings = [
                        ''
                        ], 
                    component = '', 
                    assigned_application_slug = '', 
                    assigned_application_name = '', 
                    assigned_backchannel_application_slug = '', 
                    assigned_backchannel_application_name = '', 
                    verbose_name = '', 
                    verbose_name_plural = '', 
                    meta_model_name = '', ),
                backchannel_providers = [
                    56
                    ],
                backchannel_providers_obj = [
                    authentik_openapi.models.provider.Provider(
                        pk = 56, 
                        name = '', 
                        authentication_flow = '', 
                        authorization_flow = '', 
                        property_mappings = [
                            ''
                            ], 
                        component = '', 
                        assigned_application_slug = '', 
                        assigned_application_name = '', 
                        assigned_backchannel_application_slug = '', 
                        assigned_backchannel_application_name = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', )
                    ],
                launch_url = '',
                open_in_new_tab = True,
                meta_launch_url = '',
                meta_icon = '',
                meta_description = '',
                meta_publisher = '',
                policy_engine_mode = 'all',
                group = ''
            )
        else:
            return Application(
                pk = '',
                name = '',
                slug = 'z',
                provider_obj = authentik_openapi.models.provider.Provider(
                    pk = 56, 
                    name = '', 
                    authentication_flow = '', 
                    authorization_flow = '', 
                    property_mappings = [
                        ''
                        ], 
                    component = '', 
                    assigned_application_slug = '', 
                    assigned_application_name = '', 
                    assigned_backchannel_application_slug = '', 
                    assigned_backchannel_application_name = '', 
                    verbose_name = '', 
                    verbose_name_plural = '', 
                    meta_model_name = '', ),
                backchannel_providers_obj = [
                    authentik_openapi.models.provider.Provider(
                        pk = 56, 
                        name = '', 
                        authentication_flow = '', 
                        authorization_flow = '', 
                        property_mappings = [
                            ''
                            ], 
                        component = '', 
                        assigned_application_slug = '', 
                        assigned_application_name = '', 
                        assigned_backchannel_application_slug = '', 
                        assigned_backchannel_application_name = '', 
                        verbose_name = '', 
                        verbose_name_plural = '', 
                        meta_model_name = '', )
                    ],
                launch_url = '',
                meta_icon = '',
        )
        """

    def testApplication(self):
        """Test Application"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
