# WebhookRegistryPackageUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**registry_package** | [**WebhookRegistryPackageUpdatedRegistryPackage**](WebhookRegistryPackageUpdatedRegistryPackage.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_registry_package_updated import WebhookRegistryPackageUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegistryPackageUpdated from a JSON string
webhook_registry_package_updated_instance = WebhookRegistryPackageUpdated.from_json(json)
# print the JSON string representation of the object
print(WebhookRegistryPackageUpdated.to_json())

# convert the object into a dict
webhook_registry_package_updated_dict = webhook_registry_package_updated_instance.to_dict()
# create an instance of WebhookRegistryPackageUpdated from a dict
webhook_registry_package_updated_from_dict = WebhookRegistryPackageUpdated.from_dict(webhook_registry_package_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


