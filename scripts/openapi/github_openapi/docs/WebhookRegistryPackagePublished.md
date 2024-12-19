# WebhookRegistryPackagePublished


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**registry_package** | [**WebhookRegistryPackagePublishedRegistryPackage**](WebhookRegistryPackagePublishedRegistryPackage.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_registry_package_published import WebhookRegistryPackagePublished

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegistryPackagePublished from a JSON string
webhook_registry_package_published_instance = WebhookRegistryPackagePublished.from_json(json)
# print the JSON string representation of the object
print(WebhookRegistryPackagePublished.to_json())

# convert the object into a dict
webhook_registry_package_published_dict = webhook_registry_package_published_instance.to_dict()
# create an instance of WebhookRegistryPackagePublished from a dict
webhook_registry_package_published_from_dict = WebhookRegistryPackagePublished.from_dict(webhook_registry_package_published_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


