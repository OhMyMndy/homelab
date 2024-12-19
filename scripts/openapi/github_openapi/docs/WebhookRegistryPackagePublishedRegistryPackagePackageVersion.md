# WebhookRegistryPackagePublishedRegistryPackagePackageVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**WebhookRegistryPackagePublishedRegistryPackageOwner**](WebhookRegistryPackagePublishedRegistryPackageOwner.md) |  | [optional] 
**body** | [**WebhookPackagePublishedPackagePackageVersionBody**](WebhookPackagePublishedPackagePackageVersionBody.md) |  | [optional] 
**body_html** | **str** |  | [optional] 
**container_metadata** | [**WebhookRegistryPackagePublishedRegistryPackagePackageVersionContainerMetadata**](WebhookRegistryPackagePublishedRegistryPackagePackageVersionContainerMetadata.md) |  | [optional] 
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
**npm_metadata** | [**WebhookRegistryPackagePublishedRegistryPackagePackageVersionNpmMetadata**](WebhookRegistryPackagePublishedRegistryPackagePackageVersionNpmMetadata.md) |  | [optional] 
**nuget_metadata** | [**List[WebhookRegistryPackagePublishedRegistryPackagePackageVersionNugetMetadataInner]**](WebhookRegistryPackagePublishedRegistryPackagePackageVersionNugetMetadataInner.md) |  | [optional] 
**package_files** | [**List[WebhookRegistryPackagePublishedRegistryPackagePackageVersionPackageFilesInner]**](WebhookRegistryPackagePublishedRegistryPackagePackageVersionPackageFilesInner.md) |  | 
**package_url** | **str** |  | 
**prerelease** | **bool** |  | [optional] 
**release** | [**WebhookRegistryPackagePublishedRegistryPackagePackageVersionRelease**](WebhookRegistryPackagePublishedRegistryPackagePackageVersionRelease.md) |  | [optional] 
**rubygems_metadata** | [**List[WebhookRubygemsMetadata]**](WebhookRubygemsMetadata.md) |  | [optional] 
**summary** | **str** |  | 
**tag_name** | **str** |  | [optional] 
**target_commitish** | **str** |  | [optional] 
**target_oid** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**version** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_registry_package_published_registry_package_package_version import WebhookRegistryPackagePublishedRegistryPackagePackageVersion

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegistryPackagePublishedRegistryPackagePackageVersion from a JSON string
webhook_registry_package_published_registry_package_package_version_instance = WebhookRegistryPackagePublishedRegistryPackagePackageVersion.from_json(json)
# print the JSON string representation of the object
print(WebhookRegistryPackagePublishedRegistryPackagePackageVersion.to_json())

# convert the object into a dict
webhook_registry_package_published_registry_package_package_version_dict = webhook_registry_package_published_registry_package_package_version_instance.to_dict()
# create an instance of WebhookRegistryPackagePublishedRegistryPackagePackageVersion from a dict
webhook_registry_package_published_registry_package_package_version_from_dict = WebhookRegistryPackagePublishedRegistryPackagePackageVersion.from_dict(webhook_registry_package_published_registry_package_package_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


