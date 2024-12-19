# WebhookPackageUpdatedPackagePackageVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**User2**](User2.md) |  | 
**body** | **str** |  | 
**body_html** | **str** |  | 
**created_at** | **str** |  | 
**description** | **str** |  | 
**docker_metadata** | [**List[WebhookPackagePublishedPackagePackageVersionDockerMetadataInner]**](WebhookPackagePublishedPackagePackageVersionDockerMetadataInner.md) |  | [optional] 
**draft** | **bool** |  | [optional] 
**html_url** | **str** |  | 
**id** | **int** |  | 
**installation_command** | **str** |  | 
**manifest** | **str** |  | [optional] 
**metadata** | **List[Dict[str, object]]** |  | 
**name** | **str** |  | 
**package_files** | [**List[WebhookPackageUpdatedPackagePackageVersionPackageFilesInner]**](WebhookPackageUpdatedPackagePackageVersionPackageFilesInner.md) |  | 
**package_url** | **str** |  | [optional] 
**prerelease** | **bool** |  | [optional] 
**release** | [**WebhookPackageUpdatedPackagePackageVersionRelease**](WebhookPackageUpdatedPackagePackageVersionRelease.md) |  | [optional] 
**rubygems_metadata** | [**List[WebhookRubygemsMetadata]**](WebhookRubygemsMetadata.md) |  | [optional] 
**source_url** | **str** |  | [optional] 
**summary** | **str** |  | 
**tag_name** | **str** |  | [optional] 
**target_commitish** | **str** |  | 
**target_oid** | **str** |  | 
**updated_at** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_package_updated_package_package_version import WebhookPackageUpdatedPackagePackageVersion

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPackageUpdatedPackagePackageVersion from a JSON string
webhook_package_updated_package_package_version_instance = WebhookPackageUpdatedPackagePackageVersion.from_json(json)
# print the JSON string representation of the object
print(WebhookPackageUpdatedPackagePackageVersion.to_json())

# convert the object into a dict
webhook_package_updated_package_package_version_dict = webhook_package_updated_package_package_version_instance.to_dict()
# create an instance of WebhookPackageUpdatedPackagePackageVersion from a dict
webhook_package_updated_package_package_version_from_dict = WebhookPackageUpdatedPackagePackageVersion.from_dict(webhook_package_updated_package_package_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


