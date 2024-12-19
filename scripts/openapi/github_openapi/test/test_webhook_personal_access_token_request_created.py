# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_personal_access_token_request_created import WebhookPersonalAccessTokenRequestCreated

class TestWebhookPersonalAccessTokenRequestCreated(unittest.TestCase):
    """WebhookPersonalAccessTokenRequestCreated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookPersonalAccessTokenRequestCreated:
        """Test WebhookPersonalAccessTokenRequestCreated
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookPersonalAccessTokenRequestCreated`
        """
        model = WebhookPersonalAccessTokenRequestCreated()
        if include_optional:
            return WebhookPersonalAccessTokenRequestCreated(
                action = 'created',
                personal_access_token_request = github_openapi.models.personal_access_token_request.Personal Access Token Request(
                    id = 56, 
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
                    permissions_added = github_openapi.models.personal_access_token_request_permissions_added.personal_access_token_request_permissions_added(
                        organization = {
                            'key' : ''
                            }, 
                        repository = {
                            'key' : ''
                            }, 
                        other = {
                            'key' : ''
                            }, ), 
                    permissions_upgraded = github_openapi.models.personal_access_token_request_permissions_upgraded.personal_access_token_request_permissions_upgraded(), 
                    permissions_result = github_openapi.models.personal_access_token_request_permissions_result.personal_access_token_request_permissions_result(), 
                    repository_selection = 'none', 
                    repository_count = 56, 
                    repositories = [
                        github_openapi.models.webhooks_repositories_inner.webhooks_repositories_inner(
                            full_name = '', 
                            id = 56, 
                            name = '', 
                            node_id = '', 
                            private = True, )
                        ], 
                    created_at = '', 
                    token_id = 56, 
                    token_name = '', 
                    token_expired = True, 
                    token_expires_at = '', 
                    token_last_used_at = '', ),
                enterprise = github_openapi.models.enterprise.Enterprise(
                    description = '', 
                    html_url = 'https://github.com/enterprises/octo-business', 
                    website_url = '', 
                    id = 42, 
                    node_id = 'MDEwOlJlcG9zaXRvcnkxMjk2MjY5', 
                    name = 'Octo Business', 
                    slug = 'octo-business', 
                    created_at = '2019-01-26T19:01:12Z', 
                    updated_at = '2019-01-26T19:14:43Z', 
                    avatar_url = '', ),
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
                installation = github_openapi.models.simple_installation.Simple Installation(
                    id = 1, 
                    node_id = 'MDQ6VXNlcjU4MzIzMQ==', )
            )
        else:
            return WebhookPersonalAccessTokenRequestCreated(
                action = 'created',
                personal_access_token_request = github_openapi.models.personal_access_token_request.Personal Access Token Request(
                    id = 56, 
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
                    permissions_added = github_openapi.models.personal_access_token_request_permissions_added.personal_access_token_request_permissions_added(
                        organization = {
                            'key' : ''
                            }, 
                        repository = {
                            'key' : ''
                            }, 
                        other = {
                            'key' : ''
                            }, ), 
                    permissions_upgraded = github_openapi.models.personal_access_token_request_permissions_upgraded.personal_access_token_request_permissions_upgraded(), 
                    permissions_result = github_openapi.models.personal_access_token_request_permissions_result.personal_access_token_request_permissions_result(), 
                    repository_selection = 'none', 
                    repository_count = 56, 
                    repositories = [
                        github_openapi.models.webhooks_repositories_inner.webhooks_repositories_inner(
                            full_name = '', 
                            id = 56, 
                            name = '', 
                            node_id = '', 
                            private = True, )
                        ], 
                    created_at = '', 
                    token_id = 56, 
                    token_name = '', 
                    token_expired = True, 
                    token_expires_at = '', 
                    token_last_used_at = '', ),
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

    def testWebhookPersonalAccessTokenRequestCreated(self):
        """Test WebhookPersonalAccessTokenRequestCreated"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
