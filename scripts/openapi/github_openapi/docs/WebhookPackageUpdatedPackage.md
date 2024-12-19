# WebhookPackageUpdatedPackage

Information about the package.

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
**owner** | [**User2**](User2.md) |  | 
**package_type** | **str** |  | 
**package_version** | [**WebhookPackageUpdatedPackagePackageVersion**](WebhookPackageUpdatedPackagePackageVersion.md) |  | 
**registry** | [**WebhookPackagePublishedPackageRegistry**](WebhookPackagePublishedPackageRegistry.md) |  | 
**updated_at** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_package_updated_package import WebhookPackageUpdatedPackage

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPackageUpdatedPackage from a JSON string
webhook_package_updated_package_instance = WebhookPackageUpdatedPackage.from_json(json)
# print the JSON string representation of the object
print(WebhookPackageUpdatedPackage.to_json())

# convert the object into a dict
webhook_package_updated_package_dict = webhook_package_updated_package_instance.to_dict()
# create an instance of WebhookPackageUpdatedPackage from a dict
webhook_package_updated_package_from_dict = WebhookPackageUpdatedPackage.from_dict(webhook_package_updated_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


