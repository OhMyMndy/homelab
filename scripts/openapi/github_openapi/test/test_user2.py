# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.user2 import User2

class TestUser2(unittest.TestCase):
    """User2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> User2:
        """Test User2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `User2`
        """
        model = User2()
        if include_optional:
            return User2(
                avatar_url = '',
                deleted = True,
                email = '',
                events_url = '',
                followers_url = '',
                following_url = '',
                gists_url = '',
                gravatar_id = '',
                html_url = '',
                id = 56,
                login = '',
                name = '',
                node_id = '',
                organizations_url = '',
                received_events_url = '',
                repos_url = '',
                site_admin = True,
                starred_url = '',
                subscriptions_url = '',
                type = 'Bot',
                url = '',
                user_view_type = ''
            )
        else:
            return User2(
                id = 56,
                login = '',
        )
        """

    def testUser2(self):
        """Test User2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()