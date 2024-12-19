# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.rate_limit_overview import RateLimitOverview

class TestRateLimitOverview(unittest.TestCase):
    """RateLimitOverview unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RateLimitOverview:
        """Test RateLimitOverview
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RateLimitOverview`
        """
        model = RateLimitOverview()
        if include_optional:
            return RateLimitOverview(
                resources = github_openapi.models.rate_limit_overview_resources.rate_limit_overview_resources(
                    core = github_openapi.models.rate_limit.Rate Limit(
                        limit = 56, 
                        remaining = 56, 
                        reset = 56, 
                        used = 56, ), 
                    graphql = github_openapi.models.rate_limit.Rate Limit(
                        limit = 56, 
                        remaining = 56, 
                        reset = 56, 
                        used = 56, ), 
                    search = , 
                    code_search = , 
                    source_import = , 
                    integration_manifest = , 
                    code_scanning_upload = , 
                    actions_runner_registration = , 
                    scim = , 
                    dependency_snapshots = , 
                    code_scanning_autofix = , ),
                rate = github_openapi.models.rate_limit.Rate Limit(
                    limit = 56, 
                    remaining = 56, 
                    reset = 56, 
                    used = 56, )
            )
        else:
            return RateLimitOverview(
                resources = github_openapi.models.rate_limit_overview_resources.rate_limit_overview_resources(
                    core = github_openapi.models.rate_limit.Rate Limit(
                        limit = 56, 
                        remaining = 56, 
                        reset = 56, 
                        used = 56, ), 
                    graphql = github_openapi.models.rate_limit.Rate Limit(
                        limit = 56, 
                        remaining = 56, 
                        reset = 56, 
                        used = 56, ), 
                    search = , 
                    code_search = , 
                    source_import = , 
                    integration_manifest = , 
                    code_scanning_upload = , 
                    actions_runner_registration = , 
                    scim = , 
                    dependency_snapshots = , 
                    code_scanning_autofix = , ),
                rate = github_openapi.models.rate_limit.Rate Limit(
                    limit = 56, 
                    remaining = 56, 
                    reset = 56, 
                    used = 56, ),
        )
        """

    def testRateLimitOverview(self):
        """Test RateLimitOverview"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()