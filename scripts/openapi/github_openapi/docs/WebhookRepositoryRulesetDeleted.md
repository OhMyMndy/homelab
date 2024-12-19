# WebhookRepositoryRulesetDeleted


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
from github_openapi.models.webhook_repository_ruleset_deleted import WebhookRepositoryRulesetDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryRulesetDeleted from a JSON string
webhook_repository_ruleset_deleted_instance = WebhookRepositoryRulesetDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryRulesetDeleted.to_json())

# convert the object into a dict
webhook_repository_ruleset_deleted_dict = webhook_repository_ruleset_deleted_instance.to_dict()
# create an instance of WebhookRepositoryRulesetDeleted from a dict
webhook_repository_ruleset_deleted_from_dict = WebhookRepositoryRulesetDeleted.from_dict(webhook_repository_ruleset_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


