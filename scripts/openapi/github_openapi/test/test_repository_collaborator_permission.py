# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.repository_collaborator_permission import RepositoryCollaboratorPermission

class TestRepositoryCollaboratorPermission(unittest.TestCase):
    """RepositoryCollaboratorPermission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepositoryCollaboratorPermission:
        """Test RepositoryCollaboratorPermission
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepositoryCollaboratorPermission`
        """
        model = RepositoryCollaboratorPermission()
        if include_optional:
            return RepositoryCollaboratorPermission(
                permission = '',
                role_name = 'admin',
                user = github_openapi.models.collaborator.Collaborator(
                    login = 'octocat', 
                    id = 1, 
                    email = '', 
                    name = '', 
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
                    permissions = github_openapi.models.collaborator_permissions.collaborator_permissions(
                        pull = True, 
                        triage = True, 
                        push = True, 
                        maintain = True, 
                        admin = True, ), 
                    role_name = 'admin', 
                    user_view_type = 'public', )
            )
        else:
            return RepositoryCollaboratorPermission(
                permission = '',
                role_name = 'admin',
                user = github_openapi.models.collaborator.Collaborator(
                    login = 'octocat', 
                    id = 1, 
                    email = '', 
                    name = '', 
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
                    permissions = github_openapi.models.collaborator_permissions.collaborator_permissions(
                        pull = True, 
                        triage = True, 
                        push = True, 
                        maintain = True, 
                        admin = True, ), 
                    role_name = 'admin', 
                    user_view_type = 'public', ),
        )
        """

    def testRepositoryCollaboratorPermission(self):
        """Test RepositoryCollaboratorPermission"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
