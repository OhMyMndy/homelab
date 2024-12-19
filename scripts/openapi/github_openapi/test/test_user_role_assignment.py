# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.user_role_assignment import UserRoleAssignment

class TestUserRoleAssignment(unittest.TestCase):
    """UserRoleAssignment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserRoleAssignment:
        """Test UserRoleAssignment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserRoleAssignment`
        """
        model = UserRoleAssignment()
        if include_optional:
            return UserRoleAssignment(
                assignment = 'direct',
                inherited_from = [
                    github_openapi.models.team_simple.Team Simple(
                        id = 1, 
                        node_id = 'MDQ6VGVhbTE=', 
                        url = 'https://api.github.com/organizations/1/team/1', 
                        members_url = 'https://api.github.com/organizations/1/team/1/members{/member}', 
                        name = 'Justice League', 
                        description = 'A great team.', 
                        permission = 'admin', 
                        privacy = 'closed', 
                        notification_setting = 'notifications_enabled', 
                        html_url = 'https://github.com/orgs/rails/teams/core', 
                        repositories_url = 'https://api.github.com/organizations/1/team/1/repos', 
                        slug = 'justice-league', 
                        ldap_dn = 'uid=example,ou=users,dc=github,dc=com', )
                    ],
                name = '',
                email = '',
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
                starred_at = '"2020-07-09T00:17:55Z"',
                user_view_type = 'public'
            )
        else:
            return UserRoleAssignment(
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
        )
        """

    def testUserRoleAssignment(self):
        """Test UserRoleAssignment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()