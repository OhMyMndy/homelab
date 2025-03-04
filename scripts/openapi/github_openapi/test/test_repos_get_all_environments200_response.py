# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repos_get_all_environments200_response import ReposGetAllEnvironments200Response

class TestReposGetAllEnvironments200Response(unittest.TestCase):
    """ReposGetAllEnvironments200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReposGetAllEnvironments200Response:
        """Test ReposGetAllEnvironments200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReposGetAllEnvironments200Response`
        """
        model = ReposGetAllEnvironments200Response()
        if include_optional:
            return ReposGetAllEnvironments200Response(
                total_count = 5,
                environments = [
                    github_openapi.models.environment.Environment(
                        id = 56780428, 
                        node_id = 'MDExOkVudmlyb25tZW50NTY3ODA0Mjg=', 
                        name = 'staging', 
                        url = 'https://api.github.com/repos/github/hello-world/environments/staging', 
                        html_url = 'https://github.com/github/hello-world/deployments/activity_log?environments_filter=staging', 
                        created_at = '2020-11-23T22:00:40Z', 
                        updated_at = '2020-11-23T22:00:40Z', 
                        protection_rules = [
                            null
                            ], 
                        deployment_branch_policy = github_openapi.models.deployment_branch_policy_settings.deployment-branch-policy-settings(
                            protected_branches = True, 
                            custom_branch_policies = True, ), )
                    ]
            )
        else:
            return ReposGetAllEnvironments200Response(
        )
        """

    def testReposGetAllEnvironments200Response(self):
        """Test ReposGetAllEnvironments200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
