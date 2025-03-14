# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_projects_v2_item_edited_changes_one_of1 import WebhookProjectsV2ItemEditedChangesOneOf1

class TestWebhookProjectsV2ItemEditedChangesOneOf1(unittest.TestCase):
    """WebhookProjectsV2ItemEditedChangesOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookProjectsV2ItemEditedChangesOneOf1:
        """Test WebhookProjectsV2ItemEditedChangesOneOf1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookProjectsV2ItemEditedChangesOneOf1`
        """
        model = WebhookProjectsV2ItemEditedChangesOneOf1()
        if include_optional:
            return WebhookProjectsV2ItemEditedChangesOneOf1(
                body = github_openapi.models.webhook_member_edited_changes_permission.webhook_member_edited_changes_permission(
                    from = '', 
                    to = '', )
            )
        else:
            return WebhookProjectsV2ItemEditedChangesOneOf1(
                body = github_openapi.models.webhook_member_edited_changes_permission.webhook_member_edited_changes_permission(
                    from = '', 
                    to = '', ),
        )
        """

    def testWebhookProjectsV2ItemEditedChangesOneOf1(self):
        """Test WebhookProjectsV2ItemEditedChangesOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
