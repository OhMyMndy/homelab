# WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | [**RepositoryRulesetConditions**](RepositoryRulesetConditions.md) |  | [optional] 
**changes** | [**WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges**](WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_repository_ruleset_edited_changes_conditions_updated_inner import WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner from a JSON string
webhook_repository_ruleset_edited_changes_conditions_updated_inner_instance = WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner.to_json())

# convert the object into a dict
webhook_repository_ruleset_edited_changes_conditions_updated_inner_dict = webhook_repository_ruleset_edited_changes_conditions_updated_inner_instance.to_dict()
# create an instance of WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner from a dict
webhook_repository_ruleset_edited_changes_conditions_updated_inner_from_dict = WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner.from_dict(webhook_repository_ruleset_edited_changes_conditions_updated_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


