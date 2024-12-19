# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.issue7 import Issue7

class TestIssue7(unittest.TestCase):
    """Issue7 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Issue7:
        """Test Issue7
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Issue7`
        """
        model = Issue7()
        if include_optional:
            return Issue7(
                active_lock_reason = 'resolved',
                assignee = github_openapi.models.user.User(
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
                assignees = [
                    github_openapi.models.user.User(
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
                        user_view_type = '', )
                    ],
                author_association = 'COLLABORATOR',
                body = '',
                closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                comments = 56,
                comments_url = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                draft = True,
                events_url = '',
                html_url = '',
                id = 56,
                labels = [
                    github_openapi.models.label.Label(
                        color = '', 
                        default = True, 
                        description = '', 
                        id = 56, 
                        name = '', 
                        node_id = '', 
                        url = '', )
                    ],
                labels_url = '',
                locked = True,
                milestone = github_openapi.models.milestone.Milestone(
                    closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    closed_issues = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    creator = github_openapi.models.user.User(
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
                    description = '', 
                    due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    html_url = '', 
                    id = 56, 
                    labels_url = '', 
                    node_id = '', 
                    number = 56, 
                    open_issues = 56, 
                    state = 'open', 
                    title = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    url = '', ),
                node_id = '',
                number = 56,
                performed_via_github_app = github_openapi.models.app.App(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    description = '', 
                    events = [
                        'branch_protection_rule'
                        ], 
                    external_url = '', 
                    html_url = '', 
                    id = 56, 
                    name = '', 
                    node_id = '', 
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
                    permissions = github_openapi.models.app_permissions.App_permissions(
                        actions = 'read', 
                        administration = 'read', 
                        checks = 'read', 
                        content_references = 'read', 
                        contents = 'read', 
                        deployments = 'read', 
                        discussions = 'read', 
                        emails = 'read', 
                        environments = 'read', 
                        issues = 'read', 
                        keys = 'read', 
                        members = 'read', 
                        metadata = 'read', 
                        organization_administration = 'read', 
                        organization_hooks = 'read', 
                        organization_packages = 'read', 
                        organization_plan = 'read', 
                        organization_projects = 'read', 
                        organization_secrets = 'read', 
                        organization_self_hosted_runners = 'read', 
                        organization_user_blocking = 'read', 
                        packages = 'read', 
                        pages = 'read', 
                        pull_requests = 'read', 
                        repository_hooks = 'read', 
                        repository_projects = 'read', 
                        secret_scanning_alerts = 'read', 
                        secrets = 'read', 
                        security_events = 'read', 
                        security_scanning_alert = 'read', 
                        single_file = 'read', 
                        statuses = 'read', 
                        team_discussions = 'read', 
                        vulnerability_alerts = 'read', 
                        workflows = 'read', ), 
                    slug = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                pull_request = github_openapi.models.webhooks_issue_pull_request.webhooks_issue_pull_request(
                    diff_url = '', 
                    html_url = '', 
                    merged_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    patch_url = '', 
                    url = '', ),
                reactions = github_openapi.models.reactions.Reactions(
                    +1 = 56, 
                    _1 = 56, 
                    confused = 56, 
                    eyes = 56, 
                    heart = 56, 
                    hooray = 56, 
                    laugh = 56, 
                    rocket = 56, 
                    total_count = 56, 
                    url = '', ),
                repository_url = '',
                sub_issues_summary = github_openapi.models.sub_issues_summary.Sub-issues Summary(
                    total = 56, 
                    completed = 56, 
                    percent_completed = 56, ),
                state = 'open',
                state_reason = '',
                timeline_url = '',
                title = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '',
                user = github_openapi.models.user.User(
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
                    user_view_type = '', )
            )
        else:
            return Issue7(
                active_lock_reason = 'resolved',
                assignees = [
                    github_openapi.models.user.User(
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
                        user_view_type = '', )
                    ],
                author_association = 'COLLABORATOR',
                body = '',
                closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                comments = 56,
                comments_url = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                events_url = '',
                html_url = '',
                id = 56,
                labels_url = '',
                milestone = github_openapi.models.milestone.Milestone(
                    closed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    closed_issues = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    creator = github_openapi.models.user.User(
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
                    description = '', 
                    due_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    html_url = '', 
                    id = 56, 
                    labels_url = '', 
                    node_id = '', 
                    number = 56, 
                    open_issues = 56, 
                    state = 'open', 
                    title = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    url = '', ),
                node_id = '',
                number = 56,
                reactions = github_openapi.models.reactions.Reactions(
                    +1 = 56, 
                    _1 = 56, 
                    confused = 56, 
                    eyes = 56, 
                    heart = 56, 
                    hooray = 56, 
                    laugh = 56, 
                    rocket = 56, 
                    total_count = 56, 
                    url = '', ),
                repository_url = '',
                title = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '',
                user = github_openapi.models.user.User(
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
        )
        """

    def testIssue7(self):
        """Test Issue7"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
