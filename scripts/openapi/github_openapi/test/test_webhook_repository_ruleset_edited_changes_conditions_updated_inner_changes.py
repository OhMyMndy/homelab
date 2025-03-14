# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes import WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges

class TestWebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges(unittest.TestCase):
    """WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges:
        """Test WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges`
        """
        model = WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges()
        if include_optional:
            return WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges(
                condition_type = github_openapi.models.webhook_organization_renamed_changes_login.webhook_organization_renamed_changes_login(
                    from = '', ),
                target = github_openapi.models.webhook_organization_renamed_changes_login.webhook_organization_renamed_changes_login(
                    from = '', ),
                include = github_openapi.models.webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes_include.webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes_include(
                    from = [
                        ''
                        ], ),
                exclude = github_openapi.models.webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes_include.webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes_include(
                    from = [
                        ''
                        ], )
            )
        else:
            return WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges(
        )
        """

    def testWebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges(self):
        """Test WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
