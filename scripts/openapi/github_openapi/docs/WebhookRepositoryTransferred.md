# WebhookRepositoryTransferred


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookRepositoryTransferredChanges**](WebhookRepositoryTransferredChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_repository_transferred import WebhookRepositoryTransferred

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryTransferred from a JSON string
webhook_repository_transferred_instance = WebhookRepositoryTransferred.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryTransferred.to_json())

# convert the object into a dict
webhook_repository_transferred_dict = webhook_repository_transferred_instance.to_dict()
# create an instance of WebhookRepositoryTransferred from a dict
webhook_repository_transferred_from_dict = WebhookRepositoryTransferred.from_dict(webhook_repository_transferred_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


