# WebhookPackagePublishedPackagePackageVersionContainerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **object** |  | [optional] 
**manifest** | **object** |  | [optional] 
**tag** | [**WebhookPackagePublishedPackagePackageVersionContainerMetadataTag**](WebhookPackagePublishedPackagePackageVersionContainerMetadataTag.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_package_published_package_package_version_container_metadata import WebhookPackagePublishedPackagePackageVersionContainerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPackagePublishedPackagePackageVersionContainerMetadata from a JSON string
webhook_package_published_package_package_version_container_metadata_instance = WebhookPackagePublishedPackagePackageVersionContainerMetadata.from_json(json)
# print the JSON string representation of the object
print(WebhookPackagePublishedPackagePackageVersionContainerMetadata.to_json())

# convert the object into a dict
webhook_package_published_package_package_version_container_metadata_dict = webhook_package_published_package_package_version_container_metadata_instance.to_dict()
# create an instance of WebhookPackagePublishedPackagePackageVersionContainerMetadata from a dict
webhook_package_published_package_package_version_container_metadata_from_dict = WebhookPackagePublishedPackagePackageVersionContainerMetadata.from_dict(webhook_package_published_package_package_version_container_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


