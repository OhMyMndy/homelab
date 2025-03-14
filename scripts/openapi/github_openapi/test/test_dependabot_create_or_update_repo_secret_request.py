# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.dependabot_create_or_update_repo_secret_request import DependabotCreateOrUpdateRepoSecretRequest

class TestDependabotCreateOrUpdateRepoSecretRequest(unittest.TestCase):
    """DependabotCreateOrUpdateRepoSecretRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DependabotCreateOrUpdateRepoSecretRequest:
        """Test DependabotCreateOrUpdateRepoSecretRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DependabotCreateOrUpdateRepoSecretRequest`
        """
        model = DependabotCreateOrUpdateRepoSecretRequest()
        if include_optional:
            return DependabotCreateOrUpdateRepoSecretRequest(
                encrypted_value = 'zA9LCSLv1C1ylmgd0/Y2TA5TkIRHRRA401iz1CiIykN3HUO6XMsJPGh8AsaLONiNuo2ZPKNpkAmJHONf1Elbsh0SQR//',
                key_id = ''
            )
        else:
            return DependabotCreateOrUpdateRepoSecretRequest(
        )
        """

    def testDependabotCreateOrUpdateRepoSecretRequest(self):
        """Test DependabotCreateOrUpdateRepoSecretRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
