# WebhookInstallationRepositoriesRemoved


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**Installation**](Installation.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repositories_added** | [**List[WebhooksRepositoriesInner]**](WebhooksRepositoriesInner.md) | An array of repository objects, which were added to the installation. | 
**repositories_removed** | [**List[WebhooksRepositoriesInner]**](WebhooksRepositoriesInner.md) | An array of repository objects, which were removed from the installation. | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**repository_selection** | [**WebhooksRepositorySelection**](WebhooksRepositorySelection.md) |  | 
**requester** | [**WebhooksUser**](WebhooksUser.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_installation_repositories_removed import WebhookInstallationRepositoriesRemoved

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInstallationRepositoriesRemoved from a JSON string
webhook_installation_repositories_removed_instance = WebhookInstallationRepositoriesRemoved.from_json(json)
# print the JSON string representation of the object
print(WebhookInstallationRepositoriesRemoved.to_json())

# convert the object into a dict
webhook_installation_repositories_removed_dict = webhook_installation_repositories_removed_instance.to_dict()
# create an instance of WebhookInstallationRepositoriesRemoved from a dict
webhook_installation_repositories_removed_from_dict = WebhookInstallationRepositoriesRemoved.from_dict(webhook_installation_repositories_removed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


