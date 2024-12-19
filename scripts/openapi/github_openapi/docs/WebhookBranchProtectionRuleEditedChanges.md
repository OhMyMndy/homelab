# WebhookBranchProtectionRuleEditedChanges

If the action was `edited`, the changes to the rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_enforced** | [**WebhookBranchProtectionRuleEditedChangesAdminEnforced**](WebhookBranchProtectionRuleEditedChangesAdminEnforced.md) |  | [optional] 
**authorized_actor_names** | [**WebhookBranchProtectionRuleEditedChangesAuthorizedActorNames**](WebhookBranchProtectionRuleEditedChangesAuthorizedActorNames.md) |  | [optional] 
**authorized_actors_only** | [**WebhookBranchProtectionRuleEditedChangesAdminEnforced**](WebhookBranchProtectionRuleEditedChangesAdminEnforced.md) |  | [optional] 
**authorized_dismissal_actors_only** | [**WebhookBranchProtectionRuleEditedChangesAdminEnforced**](WebhookBranchProtectionRuleEditedChangesAdminEnforced.md) |  | [optional] 
**linear_history_requirement_enforcement_level** | [**WebhookBranchProtectionRuleEditedChangesLinearHistoryRequirementEnforcementLevel**](WebhookBranchProtectionRuleEditedChangesLinearHistoryRequirementEnforcementLevel.md) |  | [optional] 
**lock_branch_enforcement_level** | [**WebhookBranchProtectionRuleEditedChangesLinearHistoryRequirementEnforcementLevel**](WebhookBranchProtectionRuleEditedChangesLinearHistoryRequirementEnforcementLevel.md) |  | [optional] 
**lock_allows_fork_sync** | [**WebhookBranchProtectionRuleEditedChangesAdminEnforced**](WebhookBranchProtectionRuleEditedChangesAdminEnforced.md) |  | [optional] 
**pull_request_reviews_enforcement_level** | [**WebhookBranchProtectionRuleEditedChangesLinearHistoryRequirementEnforcementLevel**](WebhookBranchProtectionRuleEditedChangesLinearHistoryRequirementEnforcementLevel.md) |  | [optional] 
**require_last_push_approval** | [**WebhookBranchProtectionRuleEditedChangesAdminEnforced**](WebhookBranchProtectionRuleEditedChangesAdminEnforced.md) |  | [optional] 
**required_status_checks** | [**WebhookBranchProtectionRuleEditedChangesAuthorizedActorNames**](WebhookBranchProtectionRuleEditedChangesAuthorizedActorNames.md) |  | [optional] 
**required_status_checks_enforcement_level** | [**WebhookBranchProtectionRuleEditedChangesLinearHistoryRequirementEnforcementLevel**](WebhookBranchProtectionRuleEditedChangesLinearHistoryRequirementEnforcementLevel.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_branch_protection_rule_edited_changes import WebhookBranchProtectionRuleEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookBranchProtectionRuleEditedChanges from a JSON string
webhook_branch_protection_rule_edited_changes_instance = WebhookBranchProtectionRuleEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookBranchProtectionRuleEditedChanges.to_json())

# convert the object into a dict
webhook_branch_protection_rule_edited_changes_dict = webhook_branch_protection_rule_edited_changes_instance.to_dict()
# create an instance of WebhookBranchProtectionRuleEditedChanges from a dict
webhook_branch_protection_rule_edited_changes_from_dict = WebhookBranchProtectionRuleEditedChanges.from_dict(webhook_branch_protection_rule_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


