# WebhookRepositoryRulesetEditedChangesRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | [**List[RepositoryRule]**](RepositoryRule.md) |  | [optional] 
**deleted** | [**List[RepositoryRule]**](RepositoryRule.md) |  | [optional] 
**updated** | [**List[WebhookRepositoryRulesetEditedChangesRulesUpdatedInner]**](WebhookRepositoryRulesetEditedChangesRulesUpdatedInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_repository_ruleset_edited_changes_rules import WebhookRepositoryRulesetEditedChangesRules

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryRulesetEditedChangesRules from a JSON string
webhook_repository_ruleset_edited_changes_rules_instance = WebhookRepositoryRulesetEditedChangesRules.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryRulesetEditedChangesRules.to_json())

# convert the object into a dict
webhook_repository_ruleset_edited_changes_rules_dict = webhook_repository_ruleset_edited_changes_rules_instance.to_dict()
# create an instance of WebhookRepositoryRulesetEditedChangesRules from a dict
webhook_repository_ruleset_edited_changes_rules_from_dict = WebhookRepositoryRulesetEditedChangesRules.from_dict(webhook_repository_ruleset_edited_changes_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


