# WebhookInstallationNewPermissionsAccepted


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
from github_openapi.models.webhook_installation_new_permissions_accepted import WebhookInstallationNewPermissionsAccepted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInstallationNewPermissionsAccepted from a JSON string
webhook_installation_new_permissions_accepted_instance = WebhookInstallationNewPermissionsAccepted.from_json(json)
# print the JSON string representation of the object
print(WebhookInstallationNewPermissionsAccepted.to_json())

# convert the object into a dict
webhook_installation_new_permissions_accepted_dict = webhook_installation_new_permissions_accepted_instance.to_dict()
# create an instance of WebhookInstallationNewPermissionsAccepted from a dict
webhook_installation_new_permissions_accepted_from_dict = WebhookInstallationNewPermissionsAccepted.from_dict(webhook_installation_new_permissions_accepted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


