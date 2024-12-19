# WebhookRepositoryRulesetEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**repository_ruleset** | [**RepositoryRuleset**](RepositoryRuleset.md) |  | 
**changes** | [**WebhookRepositoryRulesetEditedChanges**](WebhookRepositoryRulesetEditedChanges.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_repository_ruleset_edited import WebhookRepositoryRulesetEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryRulesetEdited from a JSON string
webhook_repository_ruleset_edited_instance = WebhookRepositoryRulesetEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryRulesetEdited.to_json())

# convert the object into a dict
webhook_repository_ruleset_edited_dict = webhook_repository_ruleset_edited_instance.to_dict()
# create an instance of WebhookRepositoryRulesetEdited from a dict
webhook_repository_ruleset_edited_from_dict = WebhookRepositoryRulesetEdited.from_dict(webhook_repository_ruleset_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


