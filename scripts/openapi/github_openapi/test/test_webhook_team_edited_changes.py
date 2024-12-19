# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_team_edited_changes import WebhookTeamEditedChanges

class TestWebhookTeamEditedChanges(unittest.TestCase):
    """WebhookTeamEditedChanges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookTeamEditedChanges:
        """Test WebhookTeamEditedChanges
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookTeamEditedChanges`
        """
        model = WebhookTeamEditedChanges()
        if include_optional:
            return WebhookTeamEditedChanges(
                description = github_openapi.models.webhook_label_edited_changes_description.webhook_label_edited_changes_description(
                    from = '', ),
                name = github_openapi.models.webhook_label_edited_changes_name.webhook_label_edited_changes_name(
                    from = '', ),
                privacy = github_openapi.models.webhook_team_edited_changes_privacy.webhook_team_edited_changes_privacy(
                    from = '', ),
                notification_setting = github_openapi.models.webhook_team_edited_changes_notification_setting.webhook_team_edited_changes_notification_setting(
                    from = '', ),
                repository = github_openapi.models.webhook_team_edited_changes_repository.webhook_team_edited_changes_repository(
                    permissions = github_openapi.models.webhook_team_edited_changes_repository_permissions.webhook_team_edited_changes_repository_permissions(
                        from = github_openapi.models.webhook_team_edited_changes_repository_permissions_from.webhook_team_edited_changes_repository_permissions_from(
                            admin = True, 
                            pull = True, 
                            push = True, ), ), )
            )
        else:
            return WebhookTeamEditedChanges(
        )
        """

    def testWebhookTeamEditedChanges(self):
        """Test WebhookTeamEditedChanges"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()