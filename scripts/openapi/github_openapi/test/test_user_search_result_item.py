# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.user_search_result_item import UserSearchResultItem

class TestUserSearchResultItem(unittest.TestCase):
    """UserSearchResultItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserSearchResultItem:
        """Test UserSearchResultItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSearchResultItem`
        """
        model = UserSearchResultItem()
        if include_optional:
            return UserSearchResultItem(
                login = '',
                id = 56,
                node_id = '',
                avatar_url = '',
                gravatar_id = '',
                url = '',
                html_url = '',
                followers_url = '',
                subscriptions_url = '',
                organizations_url = '',
                repos_url = '',
                received_events_url = '',
                type = '',
                score = 1.337,
                following_url = '',
                gists_url = '',
                starred_url = '',
                events_url = '',
                public_repos = 56,
                public_gists = 56,
                followers = 56,
                following = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                bio = '',
                email = '',
                location = '',
                site_admin = True,
                hireable = True,
                text_matches = [
                    github_openapi.models.search_result_text_matches_inner.search_result_text_matches_inner(
                        object_url = '', 
                        object_type = '', 
                        property = '', 
                        fragment = '', 
                        matches = [
                            github_openapi.models.search_result_text_matches_inner_matches_inner.search_result_text_matches_inner_matches_inner(
                                text = '', 
                                indices = [
                                    56
                                    ], )
                            ], )
                    ],
                blog = '',
                company = '',
                suspended_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                user_view_type = ''
            )
        else:
            return UserSearchResultItem(
                login = '',
                id = 56,
                node_id = '',
                avatar_url = '',
                gravatar_id = '',
                url = '',
                html_url = '',
                followers_url = '',
                subscriptions_url = '',
                organizations_url = '',
                repos_url = '',
                received_events_url = '',
                type = '',
                score = 1.337,
                following_url = '',
                gists_url = '',
                starred_url = '',
                events_url = '',
                site_admin = True,
        )
        """

    def testUserSearchResultItem(self):
        """Test UserSearchResultItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
