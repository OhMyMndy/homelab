# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.dependabot_alert_with_repository import DependabotAlertWithRepository

class TestDependabotAlertWithRepository(unittest.TestCase):
    """DependabotAlertWithRepository unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DependabotAlertWithRepository:
        """Test DependabotAlertWithRepository
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DependabotAlertWithRepository`
        """
        model = DependabotAlertWithRepository()
        if include_optional:
            return DependabotAlertWithRepository(
                number = 56,
                state = 'auto_dismissed',
                dependency = github_openapi.models.dependabot_alert_with_repository_dependency.dependabot_alert_with_repository_dependency(
                    package = github_openapi.models.dependabot_alert_package.dependabot-alert-package(
                        ecosystem = '', 
                        name = '', ), 
                    manifest_path = '', 
                    scope = 'development', ),
                security_advisory = github_openapi.models.dependabot_alert_security_advisory.dependabot-alert-security-advisory(
                    ghsa_id = '', 
                    cve_id = '', 
                    summary = '', 
                    description = '', 
                    vulnerabilities = [
                        github_openapi.models.dependabot_alert_security_vulnerability.dependabot-alert-security-vulnerability(
                            package = github_openapi.models.dependabot_alert_package.dependabot-alert-package(
                                ecosystem = '', 
                                name = '', ), 
                            severity = 'low', 
                            vulnerable_version_range = '', 
                            first_patched_version = github_openapi.models.dependabot_alert_security_vulnerability_first_patched_version.dependabot_alert_security_vulnerability_first_patched_version(
                                identifier = '', ), )
                        ], 
                    severity = 'low', 
                    cvss = github_openapi.models.dependabot_alert_security_advisory_cvss.dependabot_alert_security_advisory_cvss(
                        score = 0, 
                        vector_string = '', ), 
                    cvss_severities = github_openapi.models.cvss_severities.cvss-severities(
                        cvss_v3 = github_openapi.models.cvss_severities_cvss_v3.cvss_severities_cvss_v3(
                            vector_string = '', 
                            score = 0, ), 
                        cvss_v4 = github_openapi.models.cvss_severities_cvss_v4.cvss_severities_cvss_v4(
                            vector_string = '', 
                            score = 0, ), ), 
                    cwes = [
                        github_openapi.models.dependabot_alert_security_advisory_cwes_inner.dependabot_alert_security_advisory_cwes_inner(
                            cwe_id = '', 
                            name = '', )
                        ], 
                    identifiers = [
                        github_openapi.models.dependabot_alert_security_advisory_identifiers_inner.dependabot_alert_security_advisory_identifiers_inner(
                            type = 'CVE', 
                            value = '', )
                        ], 
                    references = [
                        github_openapi.models.dependabot_alert_security_advisory_references_inner.dependabot_alert_security_advisory_references_inner(
                            url = '', )
                        ], 
                    published_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    withdrawn_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                security_vulnerability = github_openapi.models.dependabot_alert_security_vulnerability.dependabot-alert-security-vulnerability(
                    package = github_openapi.models.dependabot_alert_package.dependabot-alert-package(
                        ecosystem = '', 
                        name = '', ), 
                    severity = 'low', 
                    vulnerable_version_range = '', 
                    first_patched_version = github_openapi.models.dependabot_alert_security_vulnerability_first_patched_version.dependabot_alert_security_vulnerability_first_patched_version(
                        identifier = '', ), ),
                url = '',
                html_url = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dismissed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
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
                dismissed_reason = 'fix_started',
                dismissed_comment = '',
                fixed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                auto_dismissed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
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
            return DependabotAlertWithRepository(
                number = 56,
                state = 'auto_dismissed',
                dependency = github_openapi.models.dependabot_alert_with_repository_dependency.dependabot_alert_with_repository_dependency(
                    package = github_openapi.models.dependabot_alert_package.dependabot-alert-package(
                        ecosystem = '', 
                        name = '', ), 
                    manifest_path = '', 
                    scope = 'development', ),
                security_advisory = github_openapi.models.dependabot_alert_security_advisory.dependabot-alert-security-advisory(
                    ghsa_id = '', 
                    cve_id = '', 
                    summary = '', 
                    description = '', 
                    vulnerabilities = [
                        github_openapi.models.dependabot_alert_security_vulnerability.dependabot-alert-security-vulnerability(
                            package = github_openapi.models.dependabot_alert_package.dependabot-alert-package(
                                ecosystem = '', 
                                name = '', ), 
                            severity = 'low', 
                            vulnerable_version_range = '', 
                            first_patched_version = github_openapi.models.dependabot_alert_security_vulnerability_first_patched_version.dependabot_alert_security_vulnerability_first_patched_version(
                                identifier = '', ), )
                        ], 
                    severity = 'low', 
                    cvss = github_openapi.models.dependabot_alert_security_advisory_cvss.dependabot_alert_security_advisory_cvss(
                        score = 0, 
                        vector_string = '', ), 
                    cvss_severities = github_openapi.models.cvss_severities.cvss-severities(
                        cvss_v3 = github_openapi.models.cvss_severities_cvss_v3.cvss_severities_cvss_v3(
                            vector_string = '', 
                            score = 0, ), 
                        cvss_v4 = github_openapi.models.cvss_severities_cvss_v4.cvss_severities_cvss_v4(
                            vector_string = '', 
                            score = 0, ), ), 
                    cwes = [
                        github_openapi.models.dependabot_alert_security_advisory_cwes_inner.dependabot_alert_security_advisory_cwes_inner(
                            cwe_id = '', 
                            name = '', )
                        ], 
                    identifiers = [
                        github_openapi.models.dependabot_alert_security_advisory_identifiers_inner.dependabot_alert_security_advisory_identifiers_inner(
                            type = 'CVE', 
                            value = '', )
                        ], 
                    references = [
                        github_openapi.models.dependabot_alert_security_advisory_references_inner.dependabot_alert_security_advisory_references_inner(
                            url = '', )
                        ], 
                    published_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    withdrawn_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                security_vulnerability = github_openapi.models.dependabot_alert_security_vulnerability.dependabot-alert-security-vulnerability(
                    package = github_openapi.models.dependabot_alert_package.dependabot-alert-package(
                        ecosystem = '', 
                        name = '', ), 
                    severity = 'low', 
                    vulnerable_version_range = '', 
                    first_patched_version = github_openapi.models.dependabot_alert_security_vulnerability_first_patched_version.dependabot_alert_security_vulnerability_first_patched_version(
                        identifier = '', ), ),
                url = '',
                html_url = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dismissed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
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
                dismissed_reason = 'fix_started',
                dismissed_comment = '',
                fixed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
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

    def testDependabotAlertWithRepository(self):
        """Test DependabotAlertWithRepository"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()