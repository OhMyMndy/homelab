# WebhookPackagePublishedPackage

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
**package_version** | [**WebhookPackagePublishedPackagePackageVersion**](WebhookPackagePublishedPackagePackageVersion.md) |  | 
**registry** | [**WebhookPackagePublishedPackageRegistry**](WebhookPackagePublishedPackageRegistry.md) |  | 
**updated_at** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_package_published_package import WebhookPackagePublishedPackage

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPackagePublishedPackage from a JSON string
webhook_package_published_package_instance = WebhookPackagePublishedPackage.from_json(json)
# print the JSON string representation of the object
print(WebhookPackagePublishedPackage.to_json())

# convert the object into a dict
webhook_package_published_package_dict = webhook_package_published_package_instance.to_dict()
# create an instance of WebhookPackagePublishedPackage from a dict
webhook_package_published_package_from_dict = WebhookPackagePublishedPackage.from_dict(webhook_package_published_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


