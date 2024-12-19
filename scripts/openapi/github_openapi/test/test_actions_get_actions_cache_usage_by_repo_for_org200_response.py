# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.actions_get_actions_cache_usage_by_repo_for_org200_response import ActionsGetActionsCacheUsageByRepoForOrg200Response

class TestActionsGetActionsCacheUsageByRepoForOrg200Response(unittest.TestCase):
    """ActionsGetActionsCacheUsageByRepoForOrg200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActionsGetActionsCacheUsageByRepoForOrg200Response:
        """Test ActionsGetActionsCacheUsageByRepoForOrg200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActionsGetActionsCacheUsageByRepoForOrg200Response`
        """
        model = ActionsGetActionsCacheUsageByRepoForOrg200Response()
        if include_optional:
            return ActionsGetActionsCacheUsageByRepoForOrg200Response(
                total_count = 56,
                repository_cache_usages = [
                    github_openapi.models.actions_cache_usage_by_repository.Actions Cache Usage by repository(
                        full_name = 'octo-org/Hello-World', 
                        active_caches_size_in_bytes = 2322142, 
                        active_caches_count = 3, )
                    ]
            )
        else:
            return ActionsGetActionsCacheUsageByRepoForOrg200Response(
                total_count = 56,
                repository_cache_usages = [
                    github_openapi.models.actions_cache_usage_by_repository.Actions Cache Usage by repository(
                        full_name = 'octo-org/Hello-World', 
                        active_caches_size_in_bytes = 2322142, 
                        active_caches_count = 3, )
                    ],
        )
        """

    def testActionsGetActionsCacheUsageByRepoForOrg200Response(self):
        """Test ActionsGetActionsCacheUsageByRepoForOrg200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
