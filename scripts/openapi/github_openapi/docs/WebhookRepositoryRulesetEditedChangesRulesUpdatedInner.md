# WebhookRepositoryRulesetEditedChangesRulesUpdatedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | [**RepositoryRule**](RepositoryRule.md) |  | [optional] 
**changes** | [**WebhookRepositoryRulesetEditedChangesRulesUpdatedInnerChanges**](WebhookRepositoryRulesetEditedChangesRulesUpdatedInnerChanges.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_repository_ruleset_edited_changes_rules_updated_inner import WebhookRepositoryRulesetEditedChangesRulesUpdatedInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryRulesetEditedChangesRulesUpdatedInner from a JSON string
webhook_repository_ruleset_edited_changes_rules_updated_inner_instance = WebhookRepositoryRulesetEditedChangesRulesUpdatedInner.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryRulesetEditedChangesRulesUpdatedInner.to_json())

# convert the object into a dict
webhook_repository_ruleset_edited_changes_rules_updated_inner_dict = webhook_repository_ruleset_edited_changes_rules_updated_inner_instance.to_dict()
# create an instance of WebhookRepositoryRulesetEditedChangesRulesUpdatedInner from a dict
webhook_repository_ruleset_edited_changes_rules_updated_inner_from_dict = WebhookRepositoryRulesetEditedChangesRulesUpdatedInner.from_dict(webhook_repository_ruleset_edited_changes_rules_updated_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


