# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_repository_ruleset_edited_changes_rules_updated_inner_changes import WebhookRepositoryRulesetEditedChangesRulesUpdatedInnerChanges

class TestWebhookRepositoryRulesetEditedChangesRulesUpdatedInnerChanges(unittest.TestCase):
    """WebhookRepositoryRulesetEditedChangesRulesUpdatedInnerChanges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookRepositoryRulesetEditedChangesRulesUpdatedInnerChanges:
        """Test WebhookRepositoryRulesetEditedChangesRulesUpdatedInnerChanges
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookRepositoryRulesetEditedChangesRulesUpdatedInnerChanges`
        """
        model = WebhookRepositoryRulesetEditedChangesRulesUpdatedInnerChanges()
        if include_optional:
            return WebhookRepositoryRulesetEditedChangesRulesUpdatedInnerChanges(
                configuration = github_openapi.models.webhook_organization_renamed_changes_login.webhook_organization_renamed_changes_login(
                    from = '', ),
                rule_type = github_openapi.models.webhook_organization_renamed_changes_login.webhook_organization_renamed_changes_login(
                    from = '', ),
                pattern = github_openapi.models.webhook_organization_renamed_changes_login.webhook_organization_renamed_changes_login(
                    from = '', )
            )
        else:
            return WebhookRepositoryRulesetEditedChangesRulesUpdatedInnerChanges(
        )
        """

    def testWebhookRepositoryRulesetEditedChangesRulesUpdatedInnerChanges(self):
        """Test WebhookRepositoryRulesetEditedChangesRulesUpdatedInnerChanges"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
