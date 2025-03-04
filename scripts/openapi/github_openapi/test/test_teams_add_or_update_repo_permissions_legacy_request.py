# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.teams_add_or_update_repo_permissions_legacy_request import TeamsAddOrUpdateRepoPermissionsLegacyRequest

class TestTeamsAddOrUpdateRepoPermissionsLegacyRequest(unittest.TestCase):
    """TeamsAddOrUpdateRepoPermissionsLegacyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamsAddOrUpdateRepoPermissionsLegacyRequest:
        """Test TeamsAddOrUpdateRepoPermissionsLegacyRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamsAddOrUpdateRepoPermissionsLegacyRequest`
        """
        model = TeamsAddOrUpdateRepoPermissionsLegacyRequest()
        if include_optional:
            return TeamsAddOrUpdateRepoPermissionsLegacyRequest(
                permission = 'pull'
            )
        else:
            return TeamsAddOrUpdateRepoPermissionsLegacyRequest(
        )
        """

    def testTeamsAddOrUpdateRepoPermissionsLegacyRequest(self):
        """Test TeamsAddOrUpdateRepoPermissionsLegacyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
