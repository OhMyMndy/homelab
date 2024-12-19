# WebhookRepositoryRulesetCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**repository_ruleset** | [**RepositoryRuleset**](RepositoryRuleset.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_repository_ruleset_created import WebhookRepositoryRulesetCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryRulesetCreated from a JSON string
webhook_repository_ruleset_created_instance = WebhookRepositoryRulesetCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryRulesetCreated.to_json())

# convert the object into a dict
webhook_repository_ruleset_created_dict = webhook_repository_ruleset_created_instance.to_dict()
# create an instance of WebhookRepositoryRulesetCreated from a dict
webhook_repository_ruleset_created_from_dict = WebhookRepositoryRulesetCreated.from_dict(webhook_repository_ruleset_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


