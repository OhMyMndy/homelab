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

from authentik_openapi.models.patched_saml_provider_request import PatchedSAMLProviderRequest

class TestPatchedSAMLProviderRequest(unittest.TestCase):
    """PatchedSAMLProviderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedSAMLProviderRequest:
        """Test PatchedSAMLProviderRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedSAMLProviderRequest`
        """
        model = PatchedSAMLProviderRequest()
        if include_optional:
            return PatchedSAMLProviderRequest(
                name = '0',
                authentication_flow = '',
                authorization_flow = '',
                property_mappings = [
                    ''
                    ],
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
                default_relay_state = ''
            )
        else:
            return PatchedSAMLProviderRequest(
        )
        """

    def testPatchedSAMLProviderRequest(self):
        """Test PatchedSAMLProviderRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
