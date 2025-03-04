# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.apps_create_installation_access_token_request import AppsCreateInstallationAccessTokenRequest

class TestAppsCreateInstallationAccessTokenRequest(unittest.TestCase):
    """AppsCreateInstallationAccessTokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppsCreateInstallationAccessTokenRequest:
        """Test AppsCreateInstallationAccessTokenRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppsCreateInstallationAccessTokenRequest`
        """
        model = AppsCreateInstallationAccessTokenRequest()
        if include_optional:
            return AppsCreateInstallationAccessTokenRequest(
                repositories = [
                    'rails'
                    ],
                repository_ids = [1],
                permissions = {"contents":"read","issues":"read","deployments":"write","single_file":"read"}
            )
        else:
            return AppsCreateInstallationAccessTokenRequest(
        )
        """

    def testAppsCreateInstallationAccessTokenRequest(self):
        """Test AppsCreateInstallationAccessTokenRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
