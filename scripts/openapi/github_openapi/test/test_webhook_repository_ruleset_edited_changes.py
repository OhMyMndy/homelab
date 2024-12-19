# coding: utf-8

"""
    GitHub v3 REST API

    GitHub's v3 REST API.

    The version of the OpenAPI document: 1.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from github_openapi.models.webhook_repository_ruleset_edited_changes import WebhookRepositoryRulesetEditedChanges

class TestWebhookRepositoryRulesetEditedChanges(unittest.TestCase):
    """WebhookRepositoryRulesetEditedChanges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookRepositoryRulesetEditedChanges:
        """Test WebhookRepositoryRulesetEditedChanges
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookRepositoryRulesetEditedChanges`
        """
        model = WebhookRepositoryRulesetEditedChanges()
        if include_optional:
            return WebhookRepositoryRulesetEditedChanges(
                name = github_openapi.models.webhook_organization_renamed_changes_login.webhook_organization_renamed_changes_login(
                    from = '', ),
                enforcement = github_openapi.models.webhook_organization_renamed_changes_login.webhook_organization_renamed_changes_login(
                    from = '', ),
                conditions = github_openapi.models.webhook_repository_ruleset_edited_changes_conditions.webhook_repository_ruleset_edited_changes_conditions(
                    added = [
                        github_openapi.models.repository_ruleset_conditions_for_ref_names.Repository ruleset conditions for ref names(
                            ref_name = github_openapi.models.repository_ruleset_conditions_ref_name.repository_ruleset_conditions_ref_name(
                                include = [
                                    ''
                                    ], 
                                exclude = [
                                    ''
                                    ], ), )
                        ], 
                    deleted = [
                        github_openapi.models.repository_ruleset_conditions_for_ref_names.Repository ruleset conditions for ref names()
                        ], 
                    updated = [
                        github_openapi.models.webhook_repository_ruleset_edited_changes_conditions_updated_inner.webhook_repository_ruleset_edited_changes_conditions_updated_inner(
                            condition = , 
                            changes = github_openapi.models.webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes.webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes(
                                condition_type = github_openapi.models.webhook_organization_renamed_changes_login.webhook_organization_renamed_changes_login(
                                    from = '', ), 
                                target = github_openapi.models.webhook_organization_renamed_changes_login.webhook_organization_renamed_changes_login(
                                    from = '', ), ), )
                        ], ),
                rules = github_openapi.models.webhook_repository_ruleset_edited_changes_rules.webhook_repository_ruleset_edited_changes_rules(
                    added = [
                        github_openapi.models.repository_rule.Repository Rule()
                        ], 
                    deleted = [
                        github_openapi.models.repository_rule.Repository Rule()
                        ], 
                    updated = [
                        github_openapi.models.webhook_repository_ruleset_edited_changes_rules_updated_inner.webhook_repository_ruleset_edited_changes_rules_updated_inner(
                            rule = github_openapi.models.repository_rule.Repository Rule(), 
                            changes = github_openapi.models.webhook_repository_ruleset_edited_changes_rules_updated_inner_changes.webhook_repository_ruleset_edited_changes_rules_updated_inner_changes(
                                configuration = github_openapi.models.webhook_organization_renamed_changes_login.webhook_organization_renamed_changes_login(
                                    from = '', ), 
                                rule_type = github_openapi.models.webhook_organization_renamed_changes_login.webhook_organization_renamed_changes_login(
                                    from = '', ), 
                                pattern = , ), )
                        ], )
            )
        else:
            return WebhookRepositoryRulesetEditedChanges(
        )
        """

    def testWebhookRepositoryRulesetEditedChanges(self):
        """Test WebhookRepositoryRulesetEditedChanges"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()