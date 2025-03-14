# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.root import Root

class TestRoot(unittest.TestCase):
    """Root unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Root:
        """Test Root
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Root`
        """
        model = Root()
        if include_optional:
            return Root(
                current_user_url = '',
                current_user_authorizations_html_url = '',
                authorizations_url = '',
                code_search_url = '',
                commit_search_url = '',
                emails_url = '',
                emojis_url = '',
                events_url = '',
                feeds_url = '',
                followers_url = '',
                following_url = '',
                gists_url = '',
                hub_url = '',
                issue_search_url = '',
                issues_url = '',
                keys_url = '',
                label_search_url = '',
                notifications_url = '',
                organization_url = '',
                organization_repositories_url = '',
                organization_teams_url = '',
                public_gists_url = '',
                rate_limit_url = '',
                repository_url = '',
                repository_search_url = '',
                current_user_repositories_url = '',
                starred_url = '',
                starred_gists_url = '',
                topic_search_url = '',
                user_url = '',
                user_organizations_url = '',
                user_repositories_url = '',
                user_search_url = ''
            )
        else:
            return Root(
                current_user_url = '',
                current_user_authorizations_html_url = '',
                authorizations_url = '',
                code_search_url = '',
                commit_search_url = '',
                emails_url = '',
                emojis_url = '',
                events_url = '',
                feeds_url = '',
                followers_url = '',
                following_url = '',
                gists_url = '',
                issue_search_url = '',
                issues_url = '',
                keys_url = '',
                label_search_url = '',
                notifications_url = '',
                organization_url = '',
                organization_repositories_url = '',
                organization_teams_url = '',
                public_gists_url = '',
                rate_limit_url = '',
                repository_url = '',
                repository_search_url = '',
                current_user_repositories_url = '',
                starred_url = '',
                starred_gists_url = '',
                user_url = '',
                user_organizations_url = '',
                user_repositories_url = '',
                user_search_url = '',
        )
        """

    def testRoot(self):
        """Test Root"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
