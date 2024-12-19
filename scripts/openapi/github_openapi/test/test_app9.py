# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.app9 import App9

class TestApp9(unittest.TestCase):
    """App9 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> App9:
        """Test App9
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `App9`
        """
        model = App9()
        if include_optional:
            return App9(
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
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return App9(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = '',
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
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApp9(self):
        """Test App9"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
