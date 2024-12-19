# WebhookRepositoryRulesetEditedChangesConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added** | [**List[RepositoryRulesetConditions]**](RepositoryRulesetConditions.md) |  | [optional] 
**deleted** | [**List[RepositoryRulesetConditions]**](RepositoryRulesetConditions.md) |  | [optional] 
**updated** | [**List[WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner]**](WebhookRepositoryRulesetEditedChangesConditionsUpdatedInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_repository_ruleset_edited_changes_conditions import WebhookRepositoryRulesetEditedChangesConditions

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryRulesetEditedChangesConditions from a JSON string
webhook_repository_ruleset_edited_changes_conditions_instance = WebhookRepositoryRulesetEditedChangesConditions.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryRulesetEditedChangesConditions.to_json())

# convert the object into a dict
webhook_repository_ruleset_edited_changes_conditions_dict = webhook_repository_ruleset_edited_changes_conditions_instance.to_dict()
# create an instance of WebhookRepositoryRulesetEditedChangesConditions from a dict
webhook_repository_ruleset_edited_changes_conditions_from_dict = WebhookRepositoryRulesetEditedChangesConditions.from_dict(webhook_repository_ruleset_edited_changes_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


