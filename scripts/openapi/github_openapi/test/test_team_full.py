# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.team_full import TeamFull

class TestTeamFull(unittest.TestCase):
    """TeamFull unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamFull:
        """Test TeamFull
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamFull`
        """
        model = TeamFull()
        if include_optional:
            return TeamFull(
                id = 42,
                node_id = 'MDQ6VGVhbTE=',
                url = 'https://api.github.com/organizations/1/team/1',
                html_url = 'https://github.com/orgs/rails/teams/core',
                name = 'Developers',
                slug = 'justice-league',
                description = 'A great team.',
                privacy = 'closed',
                notification_setting = 'notifications_enabled',
                permission = 'push',
                members_url = 'https://api.github.com/organizations/1/team/1/members{/member}',
                repositories_url = 'https://api.github.com/organizations/1/team/1/repos',
                parent = github_openapi.models.team_simple.Team Simple(
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
                    ldap_dn = 'uid=example,ou=users,dc=github,dc=com', ),
                members_count = 3,
                repos_count = 10,
                created_at = '2017-07-14T16:53:42Z',
                updated_at = '2017-08-17T12:37:15Z',
                organization = github_openapi.models.team_organization.Team Organization(
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
                    description = 'A great organization', 
                    name = 'github', 
                    company = 'GitHub', 
                    blog = 'https://github.com/blog', 
                    location = 'San Francisco', 
                    email = 'octocat@github.com', 
                    twitter_username = 'github', 
                    is_verified = True, 
                    has_organization_projects = True, 
                    has_repository_projects = True, 
                    public_repos = 2, 
                    public_gists = 1, 
                    followers = 20, 
                    following = 0, 
                    html_url = 'https://github.com/octocat', 
                    created_at = '2008-01-14T04:33:35Z', 
                    type = 'Organization', 
                    total_private_repos = 100, 
                    owned_private_repos = 100, 
                    private_gists = 81, 
                    disk_usage = 10000, 
                    collaborators = 8, 
                    billing_email = 'org@example.com', 
                    plan = github_openapi.models.organization_full_plan.organization_full_plan(
                        name = '', 
                        space = 56, 
                        private_repos = 56, 
                        filled_seats = 56, 
                        seats = 56, ), 
                    default_repository_permission = '', 
                    members_can_create_repositories = True, 
                    two_factor_requirement_enabled = True, 
                    members_allowed_repository_creation_type = 'all', 
                    members_can_create_public_repositories = True, 
                    members_can_create_private_repositories = True, 
                    members_can_create_internal_repositories = True, 
                    members_can_create_pages = True, 
                    members_can_create_public_pages = True, 
                    members_can_create_private_pages = True, 
                    members_can_fork_private_repositories = False, 
                    web_commit_signoff_required = False, 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                ldap_dn = 'uid=example,ou=users,dc=github,dc=com'
            )
        else:
            return TeamFull(
                id = 42,
                node_id = 'MDQ6VGVhbTE=',
                url = 'https://api.github.com/organizations/1/team/1',
                html_url = 'https://github.com/orgs/rails/teams/core',
                name = 'Developers',
                slug = 'justice-league',
                description = 'A great team.',
                permission = 'push',
                members_url = 'https://api.github.com/organizations/1/team/1/members{/member}',
                repositories_url = 'https://api.github.com/organizations/1/team/1/repos',
                members_count = 3,
                repos_count = 10,
                created_at = '2017-07-14T16:53:42Z',
                updated_at = '2017-08-17T12:37:15Z',
                organization = github_openapi.models.team_organization.Team Organization(
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
                    description = 'A great organization', 
                    name = 'github', 
                    company = 'GitHub', 
                    blog = 'https://github.com/blog', 
                    location = 'San Francisco', 
                    email = 'octocat@github.com', 
                    twitter_username = 'github', 
                    is_verified = True, 
                    has_organization_projects = True, 
                    has_repository_projects = True, 
                    public_repos = 2, 
                    public_gists = 1, 
                    followers = 20, 
                    following = 0, 
                    html_url = 'https://github.com/octocat', 
                    created_at = '2008-01-14T04:33:35Z', 
                    type = 'Organization', 
                    total_private_repos = 100, 
                    owned_private_repos = 100, 
                    private_gists = 81, 
                    disk_usage = 10000, 
                    collaborators = 8, 
                    billing_email = 'org@example.com', 
                    plan = github_openapi.models.organization_full_plan.organization_full_plan(
                        name = '', 
                        space = 56, 
                        private_repos = 56, 
                        filled_seats = 56, 
                        seats = 56, ), 
                    default_repository_permission = '', 
                    members_can_create_repositories = True, 
                    two_factor_requirement_enabled = True, 
                    members_allowed_repository_creation_type = 'all', 
                    members_can_create_public_repositories = True, 
                    members_can_create_private_repositories = True, 
                    members_can_create_internal_repositories = True, 
                    members_can_create_pages = True, 
                    members_can_create_public_pages = True, 
                    members_can_create_private_pages = True, 
                    members_can_fork_private_repositories = False, 
                    web_commit_signoff_required = False, 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testTeamFull(self):
        """Test TeamFull"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()