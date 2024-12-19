# WebhookRegistryPackagePublishedRegistryPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**description** | **str** |  | 
**ecosystem** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**namespace** | **str** |  | 
**owner** | [**WebhookRegistryPackagePublishedRegistryPackageOwner**](WebhookRegistryPackagePublishedRegistryPackageOwner.md) |  | 
**package_type** | **str** |  | 
**package_version** | [**WebhookRegistryPackagePublishedRegistryPackagePackageVersion**](WebhookRegistryPackagePublishedRegistryPackagePackageVersion.md) |  | 
**registry** | [**WebhookRegistryPackagePublishedRegistryPackageRegistry**](WebhookRegistryPackagePublishedRegistryPackageRegistry.md) |  | 
**updated_at** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_registry_package_published_registry_package import WebhookRegistryPackagePublishedRegistryPackage

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegistryPackagePublishedRegistryPackage from a JSON string
webhook_registry_package_published_registry_package_instance = WebhookRegistryPackagePublishedRegistryPackage.from_json(json)
# print the JSON string representation of the object
print(WebhookRegistryPackagePublishedRegistryPackage.to_json())

# convert the object into a dict
webhook_registry_package_published_registry_package_dict = webhook_registry_package_published_registry_package_instance.to_dict()
# create an instance of WebhookRegistryPackagePublishedRegistryPackage from a dict
webhook_registry_package_published_registry_package_from_dict = WebhookRegistryPackagePublishedRegistryPackage.from_dict(webhook_registry_package_published_registry_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


