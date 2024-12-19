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

from authentik_openapi.models.patched_microsoft_entra_provider_request import PatchedMicrosoftEntraProviderRequest

class TestPatchedMicrosoftEntraProviderRequest(unittest.TestCase):
    """PatchedMicrosoftEntraProviderRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedMicrosoftEntraProviderRequest:
        """Test PatchedMicrosoftEntraProviderRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedMicrosoftEntraProviderRequest`
        """
        model = PatchedMicrosoftEntraProviderRequest()
        if include_optional:
            return PatchedMicrosoftEntraProviderRequest(
                name = '0',
                property_mappings = [
                    ''
                    ],
                property_mappings_group = [
                    ''
                    ],
                client_id = '0',
                client_secret = '0',
                tenant_id = '0',
                exclude_users_service_account = True,
                filter_group = '',
                user_delete_action = 'do_nothing',
                group_delete_action = 'do_nothing'
            )
        else:
            return PatchedMicrosoftEntraProviderRequest(
        )
        """

    def testPatchedMicrosoftEntraProviderRequest(self):
        """Test PatchedMicrosoftEntraProviderRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
