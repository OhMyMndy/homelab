# WebhookRegistryPackageUpdatedRegistryPackagePackageVersionRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**WebhookRegistryPackagePublishedRegistryPackageOwner**](WebhookRegistryPackagePublishedRegistryPackageOwner.md) |  | 
**created_at** | **str** |  | 
**draft** | **bool** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**prerelease** | **bool** |  | 
**published_at** | **str** |  | 
**tag_name** | **str** |  | 
**target_commitish** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_registry_package_updated_registry_package_package_version_release import WebhookRegistryPackageUpdatedRegistryPackagePackageVersionRelease

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegistryPackageUpdatedRegistryPackagePackageVersionRelease from a JSON string
webhook_registry_package_updated_registry_package_package_version_release_instance = WebhookRegistryPackageUpdatedRegistryPackagePackageVersionRelease.from_json(json)
# print the JSON string representation of the object
print(WebhookRegistryPackageUpdatedRegistryPackagePackageVersionRelease.to_json())

# convert the object into a dict
webhook_registry_package_updated_registry_package_package_version_release_dict = webhook_registry_package_updated_registry_package_package_version_release_instance.to_dict()
# create an instance of WebhookRegistryPackageUpdatedRegistryPackagePackageVersionRelease from a dict
webhook_registry_package_updated_registry_package_package_version_release_from_dict = WebhookRegistryPackageUpdatedRegistryPackagePackageVersionRelease.from_dict(webhook_registry_package_updated_registry_package_package_version_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


