# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_projects_v2_project_edited_changes import WebhookProjectsV2ProjectEditedChanges

class TestWebhookProjectsV2ProjectEditedChanges(unittest.TestCase):
    """WebhookProjectsV2ProjectEditedChanges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookProjectsV2ProjectEditedChanges:
        """Test WebhookProjectsV2ProjectEditedChanges
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookProjectsV2ProjectEditedChanges`
        """
        model = WebhookProjectsV2ProjectEditedChanges()
        if include_optional:
            return WebhookProjectsV2ProjectEditedChanges(
                description = github_openapi.models.webhook_member_edited_changes_permission.webhook_member_edited_changes_permission(
                    from = '', 
                    to = '', ),
                public = github_openapi.models.webhook_projects_v2_project_edited_changes_public.webhook_projects_v2_project_edited_changes_public(
                    from = True, 
                    to = True, ),
                short_description = github_openapi.models.webhook_member_edited_changes_permission.webhook_member_edited_changes_permission(
                    from = '', 
                    to = '', ),
                title = github_openapi.models.webhook_projects_v2_project_edited_changes_title.webhook_projects_v2_project_edited_changes_title(
                    from = '', 
                    to = '', )
            )
        else:
            return WebhookProjectsV2ProjectEditedChanges(
        )
        """

    def testWebhookProjectsV2ProjectEditedChanges(self):
        """Test WebhookProjectsV2ProjectEditedChanges"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
