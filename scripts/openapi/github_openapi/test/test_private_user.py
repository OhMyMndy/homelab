# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.private_user import PrivateUser

class TestPrivateUser(unittest.TestCase):
    """PrivateUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrivateUser:
        """Test PrivateUser
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrivateUser`
        """
        model = PrivateUser()
        if include_optional:
            return PrivateUser(
                login = 'octocat',
                id = 1,
                user_view_type = '',
                node_id = 'MDQ6VXNlcjE=',
                avatar_url = 'https://github.com/images/error/octocat_happy.gif',
                gravatar_id = '41d064eb2195891e12d0413f63227ea7',
                url = 'https://api.github.com/users/octocat',
                html_url = 'https://github.com/octocat',
                followers_url = 'https://api.github.com/users/octocat/followers',
                following_url = 'https://api.github.com/users/octocat/following{/other_user}',
                gists_url = 'https://api.github.com/users/octocat/gists{/gist_id}',
                starred_url = 'https://api.github.com/users/octocat/starred{/owner}{/repo}',
                subscriptions_url = 'https://api.github.com/users/octocat/subscriptions',
                organizations_url = 'https://api.github.com/users/octocat/orgs',
                repos_url = 'https://api.github.com/users/octocat/repos',
                events_url = 'https://api.github.com/users/octocat/events{/privacy}',
                received_events_url = 'https://api.github.com/users/octocat/received_events',
                type = 'User',
                site_admin = True,
                name = 'monalisa octocat',
                company = 'GitHub',
                blog = 'https://github.com/blog',
                location = 'San Francisco',
                email = 'octocat@github.com',
                notification_email = 'octocat@github.com',
                hireable = True,
                bio = 'There once was...',
                twitter_username = 'monalisa',
                public_repos = 2,
                public_gists = 1,
                followers = 20,
                following = 0,
                created_at = '2008-01-14T04:33:35Z',
                updated_at = '2008-01-14T04:33:35Z',
                private_gists = 81,
                total_private_repos = 100,
                owned_private_repos = 100,
                disk_usage = 10000,
                collaborators = 8,
                two_factor_authentication = True,
                plan = github_openapi.models.public_user_plan.public_user_plan(
                    collaborators = 56, 
                    name = '', 
                    space = 56, 
                    private_repos = 56, ),
                business_plus = True,
                ldap_dn = ''
            )
        else:
            return PrivateUser(
                login = 'octocat',
                id = 1,
                node_id = 'MDQ6VXNlcjE=',
                avatar_url = 'https://github.com/images/error/octocat_happy.gif',
                gravatar_id = '41d064eb2195891e12d0413f63227ea7',
                url = 'https://api.github.com/users/octocat',
                html_url = 'https://github.com/octocat',
                followers_url = 'https://api.github.com/users/octocat/followers',
                following_url = 'https://api.github.com/users/octocat/following{/other_user}',
                gists_url = 'https://api.github.com/users/octocat/gists{/gist_id}',
                starred_url = 'https://api.github.com/users/octocat/starred{/owner}{/repo}',
                subscriptions_url = 'https://api.github.com/users/octocat/subscriptions',
                organizations_url = 'https://api.github.com/users/octocat/orgs',
                repos_url = 'https://api.github.com/users/octocat/repos',
                events_url = 'https://api.github.com/users/octocat/events{/privacy}',
                received_events_url = 'https://api.github.com/users/octocat/received_events',
                type = 'User',
                site_admin = True,
                name = 'monalisa octocat',
                company = 'GitHub',
                blog = 'https://github.com/blog',
                location = 'San Francisco',
                email = 'octocat@github.com',
                hireable = True,
                bio = 'There once was...',
                public_repos = 2,
                public_gists = 1,
                followers = 20,
                following = 0,
                created_at = '2008-01-14T04:33:35Z',
                updated_at = '2008-01-14T04:33:35Z',
                private_gists = 81,
                total_private_repos = 100,
                owned_private_repos = 100,
                disk_usage = 10000,
                collaborators = 8,
                two_factor_authentication = True,
        )
        """

    def testPrivateUser(self):
        """Test PrivateUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
