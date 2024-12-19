# WebhookRepositoryRulesetEditedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**WebhookOrganizationRenamedChangesLogin**](WebhookOrganizationRenamedChangesLogin.md) |  | [optional] 
**enforcement** | [**WebhookOrganizationRenamedChangesLogin**](WebhookOrganizationRenamedChangesLogin.md) |  | [optional] 
**conditions** | [**WebhookRepositoryRulesetEditedChangesConditions**](WebhookRepositoryRulesetEditedChangesConditions.md) |  | [optional] 
**rules** | [**WebhookRepositoryRulesetEditedChangesRules**](WebhookRepositoryRulesetEditedChangesRules.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_repository_ruleset_edited_changes import WebhookRepositoryRulesetEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryRulesetEditedChanges from a JSON string
webhook_repository_ruleset_edited_changes_instance = WebhookRepositoryRulesetEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryRulesetEditedChanges.to_json())

# convert the object into a dict
webhook_repository_ruleset_edited_changes_dict = webhook_repository_ruleset_edited_changes_instance.to_dict()
# create an instance of WebhookRepositoryRulesetEditedChanges from a dict
webhook_repository_ruleset_edited_changes_from_dict = WebhookRepositoryRulesetEditedChanges.from_dict(webhook_repository_ruleset_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


