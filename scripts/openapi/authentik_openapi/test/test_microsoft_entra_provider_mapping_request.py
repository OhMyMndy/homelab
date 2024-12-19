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

from authentik_openapi.models.microsoft_entra_provider_mapping_request import MicrosoftEntraProviderMappingRequest

class TestMicrosoftEntraProviderMappingRequest(unittest.TestCase):
    """MicrosoftEntraProviderMappingRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MicrosoftEntraProviderMappingRequest:
        """Test MicrosoftEntraProviderMappingRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MicrosoftEntraProviderMappingRequest`
        """
        model = MicrosoftEntraProviderMappingRequest()
        if include_optional:
            return MicrosoftEntraProviderMappingRequest(
                managed = '0',
                name = '0',
                expression = '0'
            )
        else:
            return MicrosoftEntraProviderMappingRequest(
                name = '0',
                expression = '0',
        )
        """

    def testMicrosoftEntraProviderMappingRequest(self):
        """Test MicrosoftEntraProviderMappingRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
