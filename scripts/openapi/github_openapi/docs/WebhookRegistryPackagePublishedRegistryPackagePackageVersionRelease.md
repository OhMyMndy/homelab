# WebhookRegistryPackagePublishedRegistryPackagePackageVersionRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**WebhooksSponsorshipMaintainer**](WebhooksSponsorshipMaintainer.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**draft** | **bool** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**prerelease** | **bool** |  | [optional] 
**published_at** | **str** |  | [optional] 
**tag_name** | **str** |  | [optional] 
**target_commitish** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_registry_package_published_registry_package_package_version_release import WebhookRegistryPackagePublishedRegistryPackagePackageVersionRelease

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegistryPackagePublishedRegistryPackagePackageVersionRelease from a JSON string
webhook_registry_package_published_registry_package_package_version_release_instance = WebhookRegistryPackagePublishedRegistryPackagePackageVersionRelease.from_json(json)
# print the JSON string representation of the object
print(WebhookRegistryPackagePublishedRegistryPackagePackageVersionRelease.to_json())

# convert the object into a dict
webhook_registry_package_published_registry_package_package_version_release_dict = webhook_registry_package_published_registry_package_package_version_release_instance.to_dict()
# create an instance of WebhookRegistryPackagePublishedRegistryPackagePackageVersionRelease from a dict
webhook_registry_package_published_registry_package_package_version_release_from_dict = WebhookRegistryPackagePublishedRegistryPackagePackageVersionRelease.from_dict(webhook_registry_package_published_registry_package_package_version_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


