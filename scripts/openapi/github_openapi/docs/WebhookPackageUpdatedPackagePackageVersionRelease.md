# WebhookPackageUpdatedPackagePackageVersionRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**User2**](User2.md) |  | 
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
from github_openapi.models.webhook_package_updated_package_package_version_release import WebhookPackageUpdatedPackagePackageVersionRelease

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPackageUpdatedPackagePackageVersionRelease from a JSON string
webhook_package_updated_package_package_version_release_instance = WebhookPackageUpdatedPackagePackageVersionRelease.from_json(json)
# print the JSON string representation of the object
print(WebhookPackageUpdatedPackagePackageVersionRelease.to_json())

# convert the object into a dict
webhook_package_updated_package_package_version_release_dict = webhook_package_updated_package_package_version_release_instance.to_dict()
# create an instance of WebhookPackageUpdatedPackagePackageVersionRelease from a dict
webhook_package_updated_package_package_version_release_from_dict = WebhookPackageUpdatedPackagePackageVersionRelease.from_dict(webhook_package_updated_package_package_version_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


