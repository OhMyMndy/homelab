# WebhookRegistryPackageUpdatedRegistryPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**description** | **object** |  | 
**ecosystem** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**namespace** | **str** |  | 
**owner** | [**WebhookRegistryPackagePublishedRegistryPackageOwner**](WebhookRegistryPackagePublishedRegistryPackageOwner.md) |  | 
**package_type** | **str** |  | 
**package_version** | [**WebhookRegistryPackageUpdatedRegistryPackagePackageVersion**](WebhookRegistryPackageUpdatedRegistryPackagePackageVersion.md) |  | 
**registry** | **object** |  | 
**updated_at** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_registry_package_updated_registry_package import WebhookRegistryPackageUpdatedRegistryPackage

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegistryPackageUpdatedRegistryPackage from a JSON string
webhook_registry_package_updated_registry_package_instance = WebhookRegistryPackageUpdatedRegistryPackage.from_json(json)
# print the JSON string representation of the object
print(WebhookRegistryPackageUpdatedRegistryPackage.to_json())

# convert the object into a dict
webhook_registry_package_updated_registry_package_dict = webhook_registry_package_updated_registry_package_instance.to_dict()
# create an instance of WebhookRegistryPackageUpdatedRegistryPackage from a dict
webhook_registry_package_updated_registry_package_from_dict = WebhookRegistryPackageUpdatedRegistryPackage.from_dict(webhook_registry_package_updated_registry_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


