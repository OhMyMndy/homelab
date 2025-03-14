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

from authentik_openapi.models.model_request import ModelRequest

class TestModelRequest(unittest.TestCase):
    """ModelRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModelRequest:
        """Test ModelRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModelRequest`
        """
        model = ModelRequest()
        if include_optional:
            return ModelRequest(
                name = '0',
                property_mappings = [
                    ''
                    ],
                property_mappings_group = [
                    ''
                    ],
                delegated_subject = '0',
                credentials = authentik_openapi.models.credentials.credentials(),
                scopes = '0',
                exclude_users_service_account = True,
                filter_group = '',
                user_delete_action = 'do_nothing',
                group_delete_action = 'do_nothing',
                default_group_email_domain = '0',
                authentication_flow = '',
                authorization_flow = '',
                base_dn = '0',
                search_group = '',
                certificate = '',
                tls_server_name = '',
                uid_start_number = -2147483648,
                gid_start_number = -2147483648,
                search_mode = 'direct',
                bind_mode = 'direct',
                mfa_support = True,
                client_id = '0',
                client_secret = '',
                tenant_id = '0',
                client_type = 'confidential',
                access_code_validity = '0',
                access_token_validity = '0',
                refresh_token_validity = '0',
                include_claims_in_id_token = True,
                signing_key = '',
                redirect_uris = '',
                sub_mode = 'hashed_user_id',
                issuer_mode = 'global',
                jwks_sources = [
                    ''
                    ],
                internal_host = '',
                external_host = '0',
                internal_host_ssl_validation = True,
                skip_path_regex = '',
                basic_auth_enabled = True,
                basic_auth_password_attribute = '',
                basic_auth_user_attribute = '',
                mode = 'proxy',
                intercept_header_auth = True,
                cookie_domain = '',
                settings = authentik_openapi.models.settings.settings(),
                connection_expiry = '0',
                delete_token_on_disconnect = True,
                client_networks = '0',
                shared_secret = '0',
                acs_url = '0',
                audience = '',
                issuer = '0',
                assertion_valid_not_before = '0',
                assertion_valid_not_on_or_after = '0',
                session_valid_not_on_or_after = '0',
                name_id_mapping = '',
                digest_algorithm = 'http://www.w3.org/2000/09/xmldsig#sha1',
                signature_algorithm = 'http://www.w3.org/2000/09/xmldsig#rsa-sha1',
                signing_kp = '',
                verification_kp = '',
                sp_binding = 'redirect',
                default_relay_state = '',
                url = '0',
                token = '0'
            )
        else:
            return ModelRequest(
                name = '0',
                delegated_subject = '0',
                credentials = authentik_openapi.models.credentials.credentials(),
                default_group_email_domain = '0',
                authorization_flow = '',
                client_id = '0',
                client_secret = '',
                tenant_id = '0',
                external_host = '0',
                acs_url = '0',
                url = '0',
                token = '0',
        )
        """

    def testModelRequest(self):
        """Test ModelRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
