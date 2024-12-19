# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_team_deleted import WebhookTeamDeleted

class TestWebhookTeamDeleted(unittest.TestCase):
    """WebhookTeamDeleted unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookTeamDeleted:
        """Test WebhookTeamDeleted
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookTeamDeleted`
        """
        model = WebhookTeamDeleted()
        if include_optional:
            return WebhookTeamDeleted(
                action = 'deleted',
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
                repository = github_openapi.models.repository.Repository(
                    allow_auto_merge = True, 
                    allow_forking = True, 
                    allow_merge_commit = True, 
                    allow_rebase_merge = True, 
                    allow_squash_merge = True, 
                    allow_update_branch = True, 
                    archive_url = '', 
                    archived = True, 
                    assignees_url = '', 
                    blobs_url = '', 
                    branches_url = '', 
                    clone_url = '', 
                    collaborators_url = '', 
                    comments_url = '', 
                    commits_url = '', 
                    compare_url = '', 
                    contents_url = '', 
                    contributors_url = '', 
                    created_at = null, 
                    custom_properties = { }, 
                    default_branch = '', 
                    delete_branch_on_merge = True, 
                    deployments_url = '', 
                    description = '', 
                    disabled = True, 
                    downloads_url = '', 
                    events_url = '', 
                    fork = True, 
                    forks = 56, 
                    forks_count = 56, 
                    forks_url = '', 
                    full_name = '', 
                    git_commits_url = '', 
                    git_refs_url = '', 
                    git_tags_url = '', 
                    git_url = '', 
                    has_downloads = True, 
                    has_issues = True, 
                    has_pages = True, 
                    has_projects = True, 
                    has_wiki = True, 
                    homepage = '', 
                    hooks_url = '', 
                    html_url = '', 
                    id = 56, 
                    is_template = True, 
                    issue_comment_url = '', 
                    issue_events_url = '', 
                    issues_url = '', 
                    keys_url = '', 
                    labels_url = '', 
                    language = '', 
                    languages_url = '', 
                    license = github_openapi.models.license.License(
                        key = '', 
                        name = '', 
                        node_id = '', 
                        spdx_id = '', 
                        url = '', ), 
                    master_branch = '', 
                    merges_url = '', 
                    milestones_url = '', 
                    mirror_url = '', 
                    name = '', 
                    node_id = '', 
                    notifications_url = '', 
                    open_issues = 56, 
                    open_issues_count = 56, 
                    organization = '', 
                    owner = github_openapi.models.user.User(
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
                        user_view_type = '', ), 
                    permissions = github_openapi.models.repository_permissions.Repository_permissions(
                        admin = True, 
                        maintain = True, 
                        pull = True, 
                        push = True, 
                        triage = True, ), 
                    private = True, 
                    public = True, 
                    pulls_url = '', 
                    pushed_at = null, 
                    releases_url = '', 
                    role_name = '', 
                    size = 56, 
                    ssh_url = '', 
                    stargazers = 56, 
                    stargazers_count = 56, 
                    stargazers_url = '', 
                    statuses_url = '', 
                    subscribers_url = '', 
                    subscription_url = '', 
                    svn_url = '', 
                    tags_url = '', 
                    teams_url = '', 
                    topics = [
                        ''
                        ], 
                    trees_url = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    url = '', 
                    visibility = 'public', 
                    watchers = 56, 
                    watchers_count = 56, ),
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
                team = github_openapi.models.team.Team(
                    deleted = True, 
                    description = '', 
                    html_url = '', 
                    id = 56, 
                    members_url = '', 
                    name = '', 
                    node_id = '', 
                    parent = github_openapi.models.webhooks_team_parent.webhooks_team_parent(
                        description = '', 
                        html_url = '', 
                        id = 56, 
                        members_url = '', 
                        name = '', 
                        node_id = '', 
                        permission = '', 
                        privacy = 'open', 
                        notification_setting = 'notifications_enabled', 
                        repositories_url = '', 
                        slug = '', 
                        url = '', ), 
                    permission = '', 
                    privacy = 'open', 
                    notification_setting = 'notifications_enabled', 
                    repositories_url = '', 
                    slug = '', 
                    url = '', )
            )
        else:
            return WebhookTeamDeleted(
                action = 'deleted',
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
                team = github_openapi.models.team.Team(
                    deleted = True, 
                    description = '', 
                    html_url = '', 
                    id = 56, 
                    members_url = '', 
                    name = '', 
                    node_id = '', 
                    parent = github_openapi.models.webhooks_team_parent.webhooks_team_parent(
                        description = '', 
                        html_url = '', 
                        id = 56, 
                        members_url = '', 
                        name = '', 
                        node_id = '', 
                        permission = '', 
                        privacy = 'open', 
                        notification_setting = 'notifications_enabled', 
                        repositories_url = '', 
                        slug = '', 
                        url = '', ), 
                    permission = '', 
                    privacy = 'open', 
                    notification_setting = 'notifications_enabled', 
                    repositories_url = '', 
                    slug = '', 
                    url = '', ),
        )
        """

    def testWebhookTeamDeleted(self):
        """Test WebhookTeamDeleted"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
