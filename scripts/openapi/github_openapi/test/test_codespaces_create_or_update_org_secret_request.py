# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.codespaces_create_or_update_org_secret_request import CodespacesCreateOrUpdateOrgSecretRequest

class TestCodespacesCreateOrUpdateOrgSecretRequest(unittest.TestCase):
    """CodespacesCreateOrUpdateOrgSecretRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CodespacesCreateOrUpdateOrgSecretRequest:
        """Test CodespacesCreateOrUpdateOrgSecretRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodespacesCreateOrUpdateOrgSecretRequest`
        """
        model = CodespacesCreateOrUpdateOrgSecretRequest()
        if include_optional:
            return CodespacesCreateOrUpdateOrgSecretRequest(
                encrypted_value = 'zA9LCSLv1C1ylmgd0/Y2TA5TkIRHRRA401iz1CiIykN3HUO6XMsJPGh8AsaLONiNuo2ZPKNpkAmJHONf1Elbsh0SQR//',
                key_id = '',
                visibility = 'all',
                selected_repository_ids = [
                    56
                    ]
            )
        else:
            return CodespacesCreateOrUpdateOrgSecretRequest(
                visibility = 'all',
        )
        """

    def testCodespacesCreateOrUpdateOrgSecretRequest(self):
        """Test CodespacesCreateOrUpdateOrgSecretRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
