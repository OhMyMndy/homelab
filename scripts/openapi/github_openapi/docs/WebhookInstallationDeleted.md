# WebhookInstallationDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**Installation**](Installation.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repositories** | [**List[WebhooksRepositoriesInner]**](WebhooksRepositoriesInner.md) | An array of repository objects that the installation can access. | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**requester** | **object** |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_installation_deleted import WebhookInstallationDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInstallationDeleted from a JSON string
webhook_installation_deleted_instance = WebhookInstallationDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookInstallationDeleted.to_json())

# convert the object into a dict
webhook_installation_deleted_dict = webhook_installation_deleted_instance.to_dict()
# create an instance of WebhookInstallationDeleted from a dict
webhook_installation_deleted_from_dict = WebhookInstallationDeleted.from_dict(webhook_installation_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


