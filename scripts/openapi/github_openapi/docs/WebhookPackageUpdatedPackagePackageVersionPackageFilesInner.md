# WebhookPackageUpdatedPackagePackageVersionPackageFilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | 
**created_at** | **str** |  | 
**download_url** | **str** |  | 
**id** | **int** |  | 
**md5** | **str** |  | 
**name** | **str** |  | 
**sha1** | **str** |  | 
**sha256** | **str** |  | 
**size** | **int** |  | 
**state** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_package_updated_package_package_version_package_files_inner import WebhookPackageUpdatedPackagePackageVersionPackageFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPackageUpdatedPackagePackageVersionPackageFilesInner from a JSON string
webhook_package_updated_package_package_version_package_files_inner_instance = WebhookPackageUpdatedPackagePackageVersionPackageFilesInner.from_json(json)
# print the JSON string representation of the object
print(WebhookPackageUpdatedPackagePackageVersionPackageFilesInner.to_json())

# convert the object into a dict
webhook_package_updated_package_package_version_package_files_inner_dict = webhook_package_updated_package_package_version_package_files_inner_instance.to_dict()
# create an instance of WebhookPackageUpdatedPackagePackageVersionPackageFilesInner from a dict
webhook_package_updated_package_package_version_package_files_inner_from_dict = WebhookPackageUpdatedPackagePackageVersionPackageFilesInner.from_dict(webhook_package_updated_package_package_version_package_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


