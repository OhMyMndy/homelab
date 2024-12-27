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

from authentik_openapi.models.ldap_source import LDAPSource

class TestLDAPSource(unittest.TestCase):
    """LDAPSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LDAPSource:
        """Test LDAPSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LDAPSource`
        """
        model = LDAPSource()
        if include_optional:
            return LDAPSource(
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
                user_matching_mode = 'identifier',
                managed = '',
                user_path_template = '',
                icon = '',
                server_uri = '',
                peer_certificate = '',
                client_certificate = '',
                bind_cn = '',
                start_tls = True,
                sni = True,
                base_dn = '',
                additional_user_dn = '',
                additional_group_dn = '',
                user_object_filter = '',
                group_object_filter = '',
                group_membership_field = '',
                object_uniqueness_field = '',
                password_login_update_internal_password = True,
                sync_users = True,
                sync_users_password = True,
                sync_groups = True,
                sync_parent_group = '',
                property_mappings = [
                    ''
                    ],
                property_mappings_group = [
                    ''
                    ],
                connectivity = {
                    'key' : {
                        'key' : ''
                        }
                    }
            )
        else:
            return LDAPSource(
                pk = '',
                name = '',
                slug = 'z',
                component = '',
                verbose_name = '',
                verbose_name_plural = '',
                meta_model_name = '',
                managed = '',
                icon = '',
                server_uri = '',
                base_dn = '',
                connectivity = {
                    'key' : {
                        'key' : ''
                        }
                    },
        )
        """

    def testLDAPSource(self):
        """Test LDAPSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()