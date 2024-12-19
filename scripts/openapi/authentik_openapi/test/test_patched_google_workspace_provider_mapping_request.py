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

from authentik_openapi.models.patched_google_workspace_provider_mapping_request import PatchedGoogleWorkspaceProviderMappingRequest

class TestPatchedGoogleWorkspaceProviderMappingRequest(unittest.TestCase):
    """PatchedGoogleWorkspaceProviderMappingRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchedGoogleWorkspaceProviderMappingRequest:
        """Test PatchedGoogleWorkspaceProviderMappingRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchedGoogleWorkspaceProviderMappingRequest`
        """
        model = PatchedGoogleWorkspaceProviderMappingRequest()
        if include_optional:
            return PatchedGoogleWorkspaceProviderMappingRequest(
                managed = '0',
                name = '0',
                expression = '0'
            )
        else:
            return PatchedGoogleWorkspaceProviderMappingRequest(
        )
        """

    def testPatchedGoogleWorkspaceProviderMappingRequest(self):
        """Test PatchedGoogleWorkspaceProviderMappingRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
