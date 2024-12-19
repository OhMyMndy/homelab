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

from authentik_openapi.models.source_type import SourceType

class TestSourceType(unittest.TestCase):
    """SourceType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SourceType:
        """Test SourceType
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SourceType`
        """
        model = SourceType()
        if include_optional:
            return SourceType(
                name = '',
                verbose_name = '',
                urls_customizable = True,
                request_token_url = '',
                authorization_url = '',
                access_token_url = '',
                profile_url = '',
                oidc_well_known_url = '',
                oidc_jwks_url = ''
            )
        else:
            return SourceType(
                name = '',
                verbose_name = '',
                urls_customizable = True,
                request_token_url = '',
                authorization_url = '',
                access_token_url = '',
                profile_url = '',
                oidc_well_known_url = '',
                oidc_jwks_url = '',
        )
        """

    def testSourceType(self):
        """Test SourceType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
