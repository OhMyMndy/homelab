# WebhookRegistryPackageUpdatedRegistryPackagePackageVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**WebhookRegistryPackagePublishedRegistryPackageOwner**](WebhookRegistryPackagePublishedRegistryPackageOwner.md) |  | 
**body** | **str** |  | 
**body_html** | **str** |  | 
**created_at** | **str** |  | 
**description** | **str** |  | 
**docker_metadata** | [**List[WebhookRegistryPackageUpdatedRegistryPackagePackageVersionDockerMetadataInner]**](WebhookRegistryPackageUpdatedRegistryPackagePackageVersionDockerMetadataInner.md) |  | [optional] 
**draft** | **bool** |  | [optional] 
**html_url** | **str** |  | 
**id** | **int** |  | 
**installation_command** | **str** |  | 
**manifest** | **str** |  | [optional] 
**metadata** | **List[Dict[str, object]]** |  | 
**name** | **str** |  | 
**package_files** | [**List[WebhookRegistryPackageUpdatedRegistryPackagePackageVersionPackageFilesInner]**](WebhookRegistryPackageUpdatedRegistryPackagePackageVersionPackageFilesInner.md) |  | 
**package_url** | **str** |  | 
**prerelease** | **bool** |  | [optional] 
**release** | [**WebhookRegistryPackageUpdatedRegistryPackagePackageVersionRelease**](WebhookRegistryPackageUpdatedRegistryPackagePackageVersionRelease.md) |  | [optional] 
**rubygems_metadata** | [**List[WebhookRubygemsMetadata]**](WebhookRubygemsMetadata.md) |  | [optional] 
**summary** | **str** |  | 
**tag_name** | **str** |  | [optional] 
**target_commitish** | **str** |  | 
**target_oid** | **str** |  | 
**updated_at** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_registry_package_updated_registry_package_package_version import WebhookRegistryPackageUpdatedRegistryPackagePackageVersion

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegistryPackageUpdatedRegistryPackagePackageVersion from a JSON string
webhook_registry_package_updated_registry_package_package_version_instance = WebhookRegistryPackageUpdatedRegistryPackagePackageVersion.from_json(json)
# print the JSON string representation of the object
print(WebhookRegistryPackageUpdatedRegistryPackagePackageVersion.to_json())

# convert the object into a dict
webhook_registry_package_updated_registry_package_package_version_dict = webhook_registry_package_updated_registry_package_package_version_instance.to_dict()
# create an instance of WebhookRegistryPackageUpdatedRegistryPackagePackageVersion from a dict
webhook_registry_package_updated_registry_package_package_version_from_dict = WebhookRegistryPackageUpdatedRegistryPackagePackageVersion.from_dict(webhook_registry_package_updated_registry_package_package_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


