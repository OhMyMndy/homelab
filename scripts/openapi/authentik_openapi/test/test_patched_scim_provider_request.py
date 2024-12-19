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

from authentik_openapi.models.patched_scim_provider_request import PatchedSCIMProviderRequest

class TestPatchedSCIMProviderRequest(unittest.TestCase):
    """PatchedSCIMProviderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedSCIMProviderRequest:
        """Test PatchedSCIMProviderRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedSCIMProviderRequest`
        """
        model = PatchedSCIMProviderRequest()
        if include_optional:
            return PatchedSCIMProviderRequest(
                name = '0',
                property_mappings = [
                    ''
                    ],
                property_mappings_group = [
                    ''
                    ],
                url = '0',
                token = '0',
                exclude_users_service_account = True,
                filter_group = ''
            )
        else:
            return PatchedSCIMProviderRequest(
        )
        """

    def testPatchedSCIMProviderRequest(self):
        """Test PatchedSCIMProviderRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
