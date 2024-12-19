# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.api_overview_domains import ApiOverviewDomains

class TestApiOverviewDomains(unittest.TestCase):
    """ApiOverviewDomains unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiOverviewDomains:
        """Test ApiOverviewDomains
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiOverviewDomains`
        """
        model = ApiOverviewDomains()
        if include_optional:
            return ApiOverviewDomains(
                website = [
                    '["example.com"]'
                    ],
                codespaces = [
                    '["example.com"]'
                    ],
                copilot = [
                    '["example.com"]'
                    ],
                packages = [
                    '["example.com"]'
                    ],
                actions = [
                    '["example.com"]'
                    ],
                actions_inbound = github_openapi.models.api_overview_domains_actions_inbound.api_overview_domains_actions_inbound(
                    full_domains = [
                        '["example.com"]'
                        ], 
                    wildcard_domains = [
                        '["example.com"]'
                        ], ),
                artifact_attestations = github_openapi.models.api_overview_domains_artifact_attestations.api_overview_domains_artifact_attestations(
                    trust_domain = '["example"]', 
                    services = [
                        '["example.com"]'
                        ], )
            )
        else:
            return ApiOverviewDomains(
        )
        """

    def testApiOverviewDomains(self):
        """Test ApiOverviewDomains"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
