# WebhookInstallationRepositoriesAddedRepositoriesRemovedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | [optional] 
**id** | **int** | Unique identifier of the repository | [optional] 
**name** | **str** | The name of the repository. | [optional] 
**node_id** | **str** |  | [optional] 
**private** | **bool** | Whether the repository is private or public. | [optional] 

## Example

```python
from github_openapi.models.webhook_installation_repositories_added_repositories_removed_inner import WebhookInstallationRepositoriesAddedRepositoriesRemovedInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInstallationRepositoriesAddedRepositoriesRemovedInner from a JSON string
webhook_installation_repositories_added_repositories_removed_inner_instance = WebhookInstallationRepositoriesAddedRepositoriesRemovedInner.from_json(json)
# print the JSON string representation of the object
print(WebhookInstallationRepositoriesAddedRepositoriesRemovedInner.to_json())

# convert the object into a dict
webhook_installation_repositories_added_repositories_removed_inner_dict = webhook_installation_repositories_added_repositories_removed_inner_instance.to_dict()
# create an instance of WebhookInstallationRepositoriesAddedRepositoriesRemovedInner from a dict
webhook_installation_repositories_added_repositories_removed_inner_from_dict = WebhookInstallationRepositoriesAddedRepositoriesRemovedInner.from_dict(webhook_installation_repositories_added_repositories_removed_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


