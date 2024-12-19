# WebhookRepositoryUnarchived


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_repository_unarchived import WebhookRepositoryUnarchived

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryUnarchived from a JSON string
webhook_repository_unarchived_instance = WebhookRepositoryUnarchived.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryUnarchived.to_json())

# convert the object into a dict
webhook_repository_unarchived_dict = webhook_repository_unarchived_instance.to_dict()
# create an instance of WebhookRepositoryUnarchived from a dict
webhook_repository_unarchived_from_dict = WebhookRepositoryUnarchived.from_dict(webhook_repository_unarchived_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

