# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_milestone_edited_changes import WebhookMilestoneEditedChanges

class TestWebhookMilestoneEditedChanges(unittest.TestCase):
    """WebhookMilestoneEditedChanges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookMilestoneEditedChanges:
        """Test WebhookMilestoneEditedChanges
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookMilestoneEditedChanges`
        """
        model = WebhookMilestoneEditedChanges()
        if include_optional:
            return WebhookMilestoneEditedChanges(
                description = github_openapi.models.webhook_label_edited_changes_description.webhook_label_edited_changes_description(
                    from = '', ),
                due_on = github_openapi.models.webhook_milestone_edited_changes_due_on.webhook_milestone_edited_changes_due_on(
                    from = '', ),
                title = github_openapi.models.webhook_milestone_edited_changes_title.webhook_milestone_edited_changes_title(
                    from = '', )
            )
        else:
            return WebhookMilestoneEditedChanges(
        )
        """

    def testWebhookMilestoneEditedChanges(self):
        """Test WebhookMilestoneEditedChanges"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
