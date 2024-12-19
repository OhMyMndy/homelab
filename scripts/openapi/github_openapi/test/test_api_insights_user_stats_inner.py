# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.api_insights_user_stats_inner import ApiInsightsUserStatsInner

class TestApiInsightsUserStatsInner(unittest.TestCase):
    """ApiInsightsUserStatsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiInsightsUserStatsInner:
        """Test ApiInsightsUserStatsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiInsightsUserStatsInner`
        """
        model = ApiInsightsUserStatsInner()
        if include_optional:
            return ApiInsightsUserStatsInner(
                actor_type = '',
                actor_name = '',
                actor_id = 56,
                integration_id = 56,
                oauth_application_id = 56,
                total_request_count = 56,
                rate_limited_request_count = 56,
                last_rate_limited_timestamp = '',
                last_request_timestamp = ''
            )
        else:
            return ApiInsightsUserStatsInner(
        )
        """

    def testApiInsightsUserStatsInner(self):
        """Test ApiInsightsUserStatsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()