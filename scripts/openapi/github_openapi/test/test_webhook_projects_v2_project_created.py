# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_projects_v2_project_created import WebhookProjectsV2ProjectCreated

class TestWebhookProjectsV2ProjectCreated(unittest.TestCase):
    """WebhookProjectsV2ProjectCreated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookProjectsV2ProjectCreated:
        """Test WebhookProjectsV2ProjectCreated
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookProjectsV2ProjectCreated`
        """
        model = WebhookProjectsV2ProjectCreated()
        if include_optional:
            return WebhookProjectsV2ProjectCreated(
                action = 'created',
                installation = github_openapi.models.simple_installation.Simple Installation(
                    id = 1, 
                    node_id = 'MDQ6VXNlcjU4MzIzMQ==', ),
                organization = github_openapi.models.organization_simple.Organization Simple(
                    login = 'github', 
                    id = 1, 
                    node_id = 'MDEyOk9yZ2FuaXphdGlvbjE=', 
                    url = 'https://api.github.com/orgs/github', 
                    repos_url = 'https://api.github.com/orgs/github/repos', 
                    events_url = 'https://api.github.com/orgs/github/events', 
                    hooks_url = 'https://api.github.com/orgs/github/hooks', 
                    issues_url = 'https://api.github.com/orgs/github/issues', 
                    members_url = 'https://api.github.com/orgs/github/members{/member}', 
                    public_members_url = 'https://api.github.com/orgs/github/public_members{/member}', 
                    avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                    description = 'A great organization', ),
                projects_v2 = github_openapi.models.projects_v2_project.Projects v2 Project(
                    id = 1.337, 
                    node_id = '', 
                    owner = github_openapi.models.simple_user.Simple User(
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
                        user_view_type = 'public', ), 
                    creator = github_openapi.models.simple_user.Simple User(
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
                        user_view_type = 'public', ), 
                    title = '', 
                    description = '', 
                    public = True, 
                    closed_at = '2022-04-28T12:00Z', 
                    created_at = '2022-04-28T12:00Z', 
                    updated_at = '2022-04-28T12:00Z', 
                    number = 56, 
                    short_description = '', 
                    deleted_at = '2022-04-28T12:00Z', 
                    deleted_by = github_openapi.models.simple_user.Simple User(
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
                        user_view_type = 'public', ), ),
                sender = github_openapi.models.simple_user.Simple User(
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
                    user_view_type = 'public', )
            )
        else:
            return WebhookProjectsV2ProjectCreated(
                action = 'created',
                organization = github_openapi.models.organization_simple.Organization Simple(
                    login = 'github', 
                    id = 1, 
                    node_id = 'MDEyOk9yZ2FuaXphdGlvbjE=', 
                    url = 'https://api.github.com/orgs/github', 
                    repos_url = 'https://api.github.com/orgs/github/repos', 
                    events_url = 'https://api.github.com/orgs/github/events', 
                    hooks_url = 'https://api.github.com/orgs/github/hooks', 
                    issues_url = 'https://api.github.com/orgs/github/issues', 
                    members_url = 'https://api.github.com/orgs/github/members{/member}', 
                    public_members_url = 'https://api.github.com/orgs/github/public_members{/member}', 
                    avatar_url = 'https://github.com/images/error/octocat_happy.gif', 
                    description = 'A great organization', ),
                projects_v2 = github_openapi.models.projects_v2_project.Projects v2 Project(
                    id = 1.337, 
                    node_id = '', 
                    owner = github_openapi.models.simple_user.Simple User(
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
                        user_view_type = 'public', ), 
                    creator = github_openapi.models.simple_user.Simple User(
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
                        user_view_type = 'public', ), 
                    title = '', 
                    description = '', 
                    public = True, 
                    closed_at = '2022-04-28T12:00Z', 
                    created_at = '2022-04-28T12:00Z', 
                    updated_at = '2022-04-28T12:00Z', 
                    number = 56, 
                    short_description = '', 
                    deleted_at = '2022-04-28T12:00Z', 
                    deleted_by = github_openapi.models.simple_user.Simple User(
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
                        user_view_type = 'public', ), ),
                sender = github_openapi.models.simple_user.Simple User(
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
                    user_view_type = 'public', ),
        )
        """

    def testWebhookProjectsV2ProjectCreated(self):
        """Test WebhookProjectsV2ProjectCreated"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
