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

from authentik_openapi.models.user_saml_source_connection import UserSAMLSourceConnection

class TestUserSAMLSourceConnection(unittest.TestCase):
    """UserSAMLSourceConnection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSAMLSourceConnection:
        """Test UserSAMLSourceConnection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSAMLSourceConnection`
        """
        model = UserSAMLSourceConnection()
        if include_optional:
            return UserSAMLSourceConnection(
                pk = 56,
                user = 56,
                source = authentik_openapi.models.source.Source(
                    pk = '', 
                    name = '', 
                    slug = 'z', 
                    enabled = True, 
                    authentication_flow = '', 
                    enrollment_flow = '', 
                    component = '', 
                    verbose_name = '', 
                    verbose_name_plural = '', 
                    meta_model_name = '', 
                    policy_engine_mode = 'all', 
                    user_matching_mode = null, 
                    managed = '', 
                    user_path_template = '', 
                    icon = '', ),
                identifier = ''
            )
        else:
            return UserSAMLSourceConnection(
                pk = 56,
                user = 56,
                source = authentik_openapi.models.source.Source(
                    pk = '', 
                    name = '', 
                    slug = 'z', 
                    enabled = True, 
                    authentication_flow = '', 
                    enrollment_flow = '', 
                    component = '', 
                    verbose_name = '', 
                    verbose_name_plural = '', 
                    meta_model_name = '', 
                    policy_engine_mode = 'all', 
                    user_matching_mode = null, 
                    managed = '', 
                    user_path_template = '', 
                    icon = '', ),
                identifier = '',
        )
        """

    def testUserSAMLSourceConnection(self):
        """Test UserSAMLSourceConnection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
