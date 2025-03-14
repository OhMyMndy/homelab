# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.api_overview_domains_actions_inbound import ApiOverviewDomainsActionsInbound

class TestApiOverviewDomainsActionsInbound(unittest.TestCase):
    """ApiOverviewDomainsActionsInbound unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiOverviewDomainsActionsInbound:
        """Test ApiOverviewDomainsActionsInbound
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiOverviewDomainsActionsInbound`
        """
        model = ApiOverviewDomainsActionsInbound()
        if include_optional:
            return ApiOverviewDomainsActionsInbound(
                full_domains = [
                    '["example.com"]'
                    ],
                wildcard_domains = [
                    '["example.com"]'
                    ]
            )
        else:
            return ApiOverviewDomainsActionsInbound(
        )
        """

    def testApiOverviewDomainsActionsInbound(self):
        """Test ApiOverviewDomainsActionsInbound"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
