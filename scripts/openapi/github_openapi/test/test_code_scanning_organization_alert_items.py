# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.code_scanning_organization_alert_items import CodeScanningOrganizationAlertItems

class TestCodeScanningOrganizationAlertItems(unittest.TestCase):
    """CodeScanningOrganizationAlertItems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CodeScanningOrganizationAlertItems:
        """Test CodeScanningOrganizationAlertItems
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CodeScanningOrganizationAlertItems`
        """
        model = CodeScanningOrganizationAlertItems()
        if include_optional:
            return CodeScanningOrganizationAlertItems(
                number = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '',
                html_url = '',
                instances_url = '',
                state = 'open',
                fixed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dismissed_by = github_openapi.models.simple_user.Simple User(
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
                dismissed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dismissed_reason = 'false positive',
                dismissed_comment = '',
                rule = github_openapi.models.code_scanning_alert_rule_summary.code-scanning-alert-rule-summary(
                    id = '', 
                    name = '', 
                    severity = 'none', 
                    security_severity_level = 'low', 
                    description = '', 
                    full_description = '', 
                    tags = [
                        ''
                        ], 
                    help = '', 
                    help_uri = '', ),
                tool = github_openapi.models.code_scanning_analysis_tool.code-scanning-analysis-tool(
                    name = '', 
                    version = '', 
                    guid = '', ),
                most_recent_instance = github_openapi.models.code_scanning_alert_instance.code-scanning-alert-instance(
                    ref = '', 
                    analysis_key = '', 
                    environment = '', 
                    category = '', 
                    state = 'open', 
                    commit_sha = '', 
                    message = github_openapi.models.code_scanning_alert_instance_message.code_scanning_alert_instance_message(
                        text = '', ), 
                    location = github_openapi.models.code_scanning_alert_location.code-scanning-alert-location(
                        path = '', 
                        start_line = 56, 
                        end_line = 56, 
                        start_column = 56, 
                        end_column = 56, ), 
                    html_url = '', 
                    classifications = [
                        'source'
                        ], ),
                repository = github_openapi.models.simple_repository.Simple Repository(
                    id = 1296269, 
                    node_id = 'MDEwOlJlcG9zaXRvcnkxMjk2MjY5', 
                    name = 'Hello-World', 
                    full_name = 'octocat/Hello-World', 
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
                    private = True, 
                    html_url = 'https://github.com/octocat/Hello-World', 
                    description = 'This your first repo!', 
                    fork = True, 
                    url = 'https://api.github.com/repos/octocat/Hello-World', 
                    archive_url = 'https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}', 
                    assignees_url = 'https://api.github.com/repos/octocat/Hello-World/assignees{/user}', 
                    blobs_url = 'https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}', 
                    branches_url = 'https://api.github.com/repos/octocat/Hello-World/branches{/branch}', 
                    collaborators_url = 'https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}', 
                    comments_url = 'https://api.github.com/repos/octocat/Hello-World/comments{/number}', 
                    commits_url = 'https://api.github.com/repos/octocat/Hello-World/commits{/sha}', 
                    compare_url = 'https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}', 
                    contents_url = 'https://api.github.com/repos/octocat/Hello-World/contents/{+path}', 
                    contributors_url = 'https://api.github.com/repos/octocat/Hello-World/contributors', 
                    deployments_url = 'https://api.github.com/repos/octocat/Hello-World/deployments', 
                    downloads_url = 'https://api.github.com/repos/octocat/Hello-World/downloads', 
                    events_url = 'https://api.github.com/repos/octocat/Hello-World/events', 
                    forks_url = 'https://api.github.com/repos/octocat/Hello-World/forks', 
                    git_commits_url = 'https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}', 
                    git_refs_url = 'https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}', 
                    git_tags_url = 'https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}', 
                    issue_comment_url = 'https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}', 
                    issue_events_url = 'https://api.github.com/repos/octocat/Hello-World/issues/events{/number}', 
                    issues_url = 'https://api.github.com/repos/octocat/Hello-World/issues{/number}', 
                    keys_url = 'https://api.github.com/repos/octocat/Hello-World/keys{/key_id}', 
                    labels_url = 'https://api.github.com/repos/octocat/Hello-World/labels{/name}', 
                    languages_url = 'https://api.github.com/repos/octocat/Hello-World/languages', 
                    merges_url = 'https://api.github.com/repos/octocat/Hello-World/merges', 
                    milestones_url = 'https://api.github.com/repos/octocat/Hello-World/milestones{/number}', 
                    notifications_url = 'https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}', 
                    pulls_url = 'https://api.github.com/repos/octocat/Hello-World/pulls{/number}', 
                    releases_url = 'https://api.github.com/repos/octocat/Hello-World/releases{/id}', 
                    stargazers_url = 'https://api.github.com/repos/octocat/Hello-World/stargazers', 
                    statuses_url = 'https://api.github.com/repos/octocat/Hello-World/statuses/{sha}', 
                    subscribers_url = 'https://api.github.com/repos/octocat/Hello-World/subscribers', 
                    subscription_url = 'https://api.github.com/repos/octocat/Hello-World/subscription', 
                    tags_url = 'https://api.github.com/repos/octocat/Hello-World/tags', 
                    teams_url = 'https://api.github.com/repos/octocat/Hello-World/teams', 
                    trees_url = 'https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}', 
                    hooks_url = 'https://api.github.com/repos/octocat/Hello-World/hooks', )
            )
        else:
            return CodeScanningOrganizationAlertItems(
                number = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '',
                html_url = '',
                instances_url = '',
                state = 'open',
                dismissed_by = github_openapi.models.simple_user.Simple User(
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
                dismissed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dismissed_reason = 'false positive',
                rule = github_openapi.models.code_scanning_alert_rule_summary.code-scanning-alert-rule-summary(
                    id = '', 
                    name = '', 
                    severity = 'none', 
                    security_severity_level = 'low', 
                    description = '', 
                    full_description = '', 
                    tags = [
                        ''
                        ], 
                    help = '', 
                    help_uri = '', ),
                tool = github_openapi.models.code_scanning_analysis_tool.code-scanning-analysis-tool(
                    name = '', 
                    version = '', 
                    guid = '', ),
                most_recent_instance = github_openapi.models.code_scanning_alert_instance.code-scanning-alert-instance(
                    ref = '', 
                    analysis_key = '', 
                    environment = '', 
                    category = '', 
                    state = 'open', 
                    commit_sha = '', 
                    message = github_openapi.models.code_scanning_alert_instance_message.code_scanning_alert_instance_message(
                        text = '', ), 
                    location = github_openapi.models.code_scanning_alert_location.code-scanning-alert-location(
                        path = '', 
                        start_line = 56, 
                        end_line = 56, 
                        start_column = 56, 
                        end_column = 56, ), 
                    html_url = '', 
                    classifications = [
                        'source'
                        ], ),
                repository = github_openapi.models.simple_repository.Simple Repository(
                    id = 1296269, 
                    node_id = 'MDEwOlJlcG9zaXRvcnkxMjk2MjY5', 
                    name = 'Hello-World', 
                    full_name = 'octocat/Hello-World', 
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
                    private = True, 
                    html_url = 'https://github.com/octocat/Hello-World', 
                    description = 'This your first repo!', 
                    fork = True, 
                    url = 'https://api.github.com/repos/octocat/Hello-World', 
                    archive_url = 'https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}', 
                    assignees_url = 'https://api.github.com/repos/octocat/Hello-World/assignees{/user}', 
                    blobs_url = 'https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}', 
                    branches_url = 'https://api.github.com/repos/octocat/Hello-World/branches{/branch}', 
                    collaborators_url = 'https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}', 
                    comments_url = 'https://api.github.com/repos/octocat/Hello-World/comments{/number}', 
                    commits_url = 'https://api.github.com/repos/octocat/Hello-World/commits{/sha}', 
                    compare_url = 'https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}', 
                    contents_url = 'https://api.github.com/repos/octocat/Hello-World/contents/{+path}', 
                    contributors_url = 'https://api.github.com/repos/octocat/Hello-World/contributors', 
                    deployments_url = 'https://api.github.com/repos/octocat/Hello-World/deployments', 
                    downloads_url = 'https://api.github.com/repos/octocat/Hello-World/downloads', 
                    events_url = 'https://api.github.com/repos/octocat/Hello-World/events', 
                    forks_url = 'https://api.github.com/repos/octocat/Hello-World/forks', 
                    git_commits_url = 'https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}', 
                    git_refs_url = 'https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}', 
                    git_tags_url = 'https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}', 
                    issue_comment_url = 'https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}', 
                    issue_events_url = 'https://api.github.com/repos/octocat/Hello-World/issues/events{/number}', 
                    issues_url = 'https://api.github.com/repos/octocat/Hello-World/issues{/number}', 
                    keys_url = 'https://api.github.com/repos/octocat/Hello-World/keys{/key_id}', 
                    labels_url = 'https://api.github.com/repos/octocat/Hello-World/labels{/name}', 
                    languages_url = 'https://api.github.com/repos/octocat/Hello-World/languages', 
                    merges_url = 'https://api.github.com/repos/octocat/Hello-World/merges', 
                    milestones_url = 'https://api.github.com/repos/octocat/Hello-World/milestones{/number}', 
                    notifications_url = 'https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}', 
                    pulls_url = 'https://api.github.com/repos/octocat/Hello-World/pulls{/number}', 
                    releases_url = 'https://api.github.com/repos/octocat/Hello-World/releases{/id}', 
                    stargazers_url = 'https://api.github.com/repos/octocat/Hello-World/stargazers', 
                    statuses_url = 'https://api.github.com/repos/octocat/Hello-World/statuses/{sha}', 
                    subscribers_url = 'https://api.github.com/repos/octocat/Hello-World/subscribers', 
                    subscription_url = 'https://api.github.com/repos/octocat/Hello-World/subscription', 
                    tags_url = 'https://api.github.com/repos/octocat/Hello-World/tags', 
                    teams_url = 'https://api.github.com/repos/octocat/Hello-World/teams', 
                    trees_url = 'https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}', 
                    hooks_url = 'https://api.github.com/repos/octocat/Hello-World/hooks', ),
        )
        """

    def testCodeScanningOrganizationAlertItems(self):
        """Test CodeScanningOrganizationAlertItems"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
