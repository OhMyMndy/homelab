# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.app1_permissions import App1Permissions

class TestApp1Permissions(unittest.TestCase):
    """App1Permissions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> App1Permissions:
        """Test App1Permissions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `App1Permissions`
        """
        model = App1Permissions()
        if include_optional:
            return App1Permissions(
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
                workflows = 'read'
            )
        else:
            return App1Permissions(
        )
        """

    def testApp1Permissions(self):
        """Test App1Permissions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
