# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.installation_account import InstallationAccount

class TestInstallationAccount(unittest.TestCase):
    """InstallationAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstallationAccount:
        """Test InstallationAccount
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstallationAccount`
        """
        model = InstallationAccount()
        if include_optional:
            return InstallationAccount(
                name = 'Octo Business',
                email = '',
                login = 'octocat',
                id = 42,
                node_id = 'MDEwOlJlcG9zaXRvcnkxMjk2MjY5',
                avatar_url = '',
                gravatar_id = '41d064eb2195891e12d0413f63227ea7',
                url = 'https://api.github.com/users/octocat',
                html_url = 'https://github.com/enterprises/octo-business',
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
                starred_at = '"2020-07-09T00:17:55Z"',
                user_view_type = 'public',
                description = '',
                website_url = '',
                slug = 'octo-business',
                created_at = '2019-01-26T19:01:12Z',
                updated_at = '2019-01-26T19:14:43Z'
            )
        else:
            return InstallationAccount(
                name = 'Octo Business',
                login = 'octocat',
                id = 42,
                node_id = 'MDEwOlJlcG9zaXRvcnkxMjk2MjY5',
                avatar_url = '',
                gravatar_id = '41d064eb2195891e12d0413f63227ea7',
                url = 'https://api.github.com/users/octocat',
                html_url = 'https://github.com/enterprises/octo-business',
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
                slug = 'octo-business',
                created_at = '2019-01-26T19:01:12Z',
                updated_at = '2019-01-26T19:14:43Z',
        )
        """

    def testInstallationAccount(self):
        """Test InstallationAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
