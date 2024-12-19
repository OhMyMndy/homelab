# WebhookRegistryPackagePublishedRegistryPackageRegistry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_registry_package_published_registry_package_registry import WebhookRegistryPackagePublishedRegistryPackageRegistry

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegistryPackagePublishedRegistryPackageRegistry from a JSON string
webhook_registry_package_published_registry_package_registry_instance = WebhookRegistryPackagePublishedRegistryPackageRegistry.from_json(json)
# print the JSON string representation of the object
print(WebhookRegistryPackagePublishedRegistryPackageRegistry.to_json())

# convert the object into a dict
webhook_registry_package_published_registry_package_registry_dict = webhook_registry_package_published_registry_package_registry_instance.to_dict()
# create an instance of WebhookRegistryPackagePublishedRegistryPackageRegistry from a dict
webhook_registry_package_published_registry_package_registry_from_dict = WebhookRegistryPackagePublishedRegistryPackageRegistry.from_dict(webhook_registry_package_published_registry_package_registry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


