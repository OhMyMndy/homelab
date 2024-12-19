# WebhookPackagePublishedPackagePackageVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**User2**](User2.md) |  | [optional] 
**body** | [**WebhookPackagePublishedPackagePackageVersionBody**](WebhookPackagePublishedPackagePackageVersionBody.md) |  | [optional] 
**body_html** | **str** |  | [optional] 
**container_metadata** | [**WebhookPackagePublishedPackagePackageVersionContainerMetadata**](WebhookPackagePublishedPackagePackageVersionContainerMetadata.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | 
**docker_metadata** | [**List[WebhookPackagePublishedPackagePackageVersionDockerMetadataInner]**](WebhookPackagePublishedPackagePackageVersionDockerMetadataInner.md) |  | [optional] 
**draft** | **bool** |  | [optional] 
**html_url** | **str** |  | 
**id** | **int** |  | 
**installation_command** | **str** |  | 
**manifest** | **str** |  | [optional] 
**metadata** | **List[Dict[str, object]]** |  | 
**name** | **str** |  | 
**npm_metadata** | [**WebhookPackagePublishedPackagePackageVersionNpmMetadata**](WebhookPackagePublishedPackagePackageVersionNpmMetadata.md) |  | [optional] 
**nuget_metadata** | [**List[WebhookPackagePublishedPackagePackageVersionNugetMetadataInner]**](WebhookPackagePublishedPackagePackageVersionNugetMetadataInner.md) |  | [optional] 
**package_files** | [**List[WebhookPackagePublishedPackagePackageVersionPackageFilesInner]**](WebhookPackagePublishedPackagePackageVersionPackageFilesInner.md) |  | 
**package_url** | **str** |  | [optional] 
**prerelease** | **bool** |  | [optional] 
**release** | [**WebhookPackagePublishedPackagePackageVersionRelease**](WebhookPackagePublishedPackagePackageVersionRelease.md) |  | [optional] 
**rubygems_metadata** | [**List[WebhookRubygemsMetadata]**](WebhookRubygemsMetadata.md) |  | [optional] 
**source_url** | **str** |  | [optional] 
**summary** | **str** |  | 
**tag_name** | **str** |  | [optional] 
**target_commitish** | **str** |  | [optional] 
**target_oid** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**version** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_package_published_package_package_version import WebhookPackagePublishedPackagePackageVersion

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPackagePublishedPackagePackageVersion from a JSON string
webhook_package_published_package_package_version_instance = WebhookPackagePublishedPackagePackageVersion.from_json(json)
# print the JSON string representation of the object
print(WebhookPackagePublishedPackagePackageVersion.to_json())

# convert the object into a dict
webhook_package_published_package_package_version_dict = webhook_package_published_package_package_version_instance.to_dict()
# create an instance of WebhookPackagePublishedPackagePackageVersion from a dict
webhook_package_published_package_package_version_from_dict = WebhookPackagePublishedPackagePackageVersion.from_dict(webhook_package_published_package_package_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


