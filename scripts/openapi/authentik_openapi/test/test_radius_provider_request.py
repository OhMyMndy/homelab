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

from authentik_openapi.models.radius_provider_request import RadiusProviderRequest

class TestRadiusProviderRequest(unittest.TestCase):
    """RadiusProviderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RadiusProviderRequest:
        """Test RadiusProviderRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RadiusProviderRequest`
        """
        model = RadiusProviderRequest()
        if include_optional:
            return RadiusProviderRequest(
                name = '0',
                authentication_flow = '',
                authorization_flow = '',
                property_mappings = [
                    ''
                    ],
                client_networks = '0',
                shared_secret = '0',
                mfa_support = True
            )
        else:
            return RadiusProviderRequest(
                name = '0',
                authorization_flow = '',
        )
        """

    def testRadiusProviderRequest(self):
        """Test RadiusProviderRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
