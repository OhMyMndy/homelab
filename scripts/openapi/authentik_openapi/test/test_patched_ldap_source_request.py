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

from authentik_openapi.models.patched_ldap_source_request import PatchedLDAPSourceRequest

class TestPatchedLDAPSourceRequest(unittest.TestCase):
    """PatchedLDAPSourceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedLDAPSourceRequest:
        """Test PatchedLDAPSourceRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedLDAPSourceRequest`
        """
        model = PatchedLDAPSourceRequest()
        if include_optional:
            return PatchedLDAPSourceRequest(
                name = '0',
                slug = 'z0',
                enabled = True,
                authentication_flow = '',
                enrollment_flow = '',
                policy_engine_mode = 'all',
                user_matching_mode = 'identifier',
                user_path_template = '0',
                server_uri = '0',
                peer_certificate = '',
                client_certificate = '',
                bind_cn = '',
                bind_password = '',
                start_tls = True,
                sni = True,
                base_dn = '0',
                additional_user_dn = '',
                additional_group_dn = '',
                user_object_filter = '0',
                group_object_filter = '0',
                group_membership_field = '0',
                object_uniqueness_field = '0',
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
                    ]
            )
        else:
            return PatchedLDAPSourceRequest(
        )
        """

    def testPatchedLDAPSourceRequest(self):
        """Test PatchedLDAPSourceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
