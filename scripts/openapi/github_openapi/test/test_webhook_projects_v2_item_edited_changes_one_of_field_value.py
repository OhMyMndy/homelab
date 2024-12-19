# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_projects_v2_item_edited_changes_one_of_field_value import WebhookProjectsV2ItemEditedChangesOneOfFieldValue

class TestWebhookProjectsV2ItemEditedChangesOneOfFieldValue(unittest.TestCase):
    """WebhookProjectsV2ItemEditedChangesOneOfFieldValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookProjectsV2ItemEditedChangesOneOfFieldValue:
        """Test WebhookProjectsV2ItemEditedChangesOneOfFieldValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookProjectsV2ItemEditedChangesOneOfFieldValue`
        """
        model = WebhookProjectsV2ItemEditedChangesOneOfFieldValue()
        if include_optional:
            return WebhookProjectsV2ItemEditedChangesOneOfFieldValue(
                field_node_id = '',
                field_type = '',
                field_name = '',
                project_number = 56,
                var_from = None,
                to = None
            )
        else:
            return WebhookProjectsV2ItemEditedChangesOneOfFieldValue(
        )
        """

    def testWebhookProjectsV2ItemEditedChangesOneOfFieldValue(self):
        """Test WebhookProjectsV2ItemEditedChangesOneOfFieldValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
