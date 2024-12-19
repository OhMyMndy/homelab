# WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_type** | [**WebhookOrganizationRenamedChangesLogin**](WebhookOrganizationRenamedChangesLogin.md) |  | [optional] 
**target** | [**WebhookOrganizationRenamedChangesLogin**](WebhookOrganizationRenamedChangesLogin.md) |  | [optional] 
**include** | [**WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChangesInclude**](WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChangesInclude.md) |  | [optional] 
**exclude** | [**WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChangesInclude**](WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChangesInclude.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes import WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges from a JSON string
webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes_instance = WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges.to_json())

# convert the object into a dict
webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes_dict = webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes_instance.to_dict()
# create an instance of WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges from a dict
webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes_from_dict = WebhookRepositoryRulesetEditedChangesConditionsUpdatedInnerChanges.from_dict(webhook_repository_ruleset_edited_changes_conditions_updated_inner_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


