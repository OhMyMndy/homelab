# WebhookPackagePublishedPackageRegistry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about_url** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**url** | **str** |  | 
**vendor** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_package_published_package_registry import WebhookPackagePublishedPackageRegistry

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPackagePublishedPackageRegistry from a JSON string
webhook_package_published_package_registry_instance = WebhookPackagePublishedPackageRegistry.from_json(json)
# print the JSON string representation of the object
print(WebhookPackagePublishedPackageRegistry.to_json())

# convert the object into a dict
webhook_package_published_package_registry_dict = webhook_package_published_package_registry_instance.to_dict()
# create an instance of WebhookPackagePublishedPackageRegistry from a dict
webhook_package_published_package_registry_from_dict = WebhookPackagePublishedPackageRegistry.from_dict(webhook_package_published_package_registry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


