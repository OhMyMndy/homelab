# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_projects_v2_item_edited_changes import WebhookProjectsV2ItemEditedChanges

class TestWebhookProjectsV2ItemEditedChanges(unittest.TestCase):
    """WebhookProjectsV2ItemEditedChanges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookProjectsV2ItemEditedChanges:
        """Test WebhookProjectsV2ItemEditedChanges
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookProjectsV2ItemEditedChanges`
        """
        model = WebhookProjectsV2ItemEditedChanges()
        if include_optional:
            return WebhookProjectsV2ItemEditedChanges(
                field_value = github_openapi.models.webhook_projects_v2_item_edited_changes_one_of_field_value.webhook_projects_v2_item_edited_changes_oneOf_field_value(
                    field_node_id = '', 
                    field_type = '', 
                    field_name = '', 
                    project_number = 56, 
                    from = null, 
                    to = null, ),
                body = github_openapi.models.webhook_member_edited_changes_permission.webhook_member_edited_changes_permission(
                    from = '', 
                    to = '', )
            )
        else:
            return WebhookProjectsV2ItemEditedChanges(
                field_value = github_openapi.models.webhook_projects_v2_item_edited_changes_one_of_field_value.webhook_projects_v2_item_edited_changes_oneOf_field_value(
                    field_node_id = '', 
                    field_type = '', 
                    field_name = '', 
                    project_number = 56, 
                    from = null, 
                    to = null, ),
                body = github_openapi.models.webhook_member_edited_changes_permission.webhook_member_edited_changes_permission(
                    from = '', 
                    to = '', ),
        )
        """

    def testWebhookProjectsV2ItemEditedChanges(self):
        """Test WebhookProjectsV2ItemEditedChanges"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()