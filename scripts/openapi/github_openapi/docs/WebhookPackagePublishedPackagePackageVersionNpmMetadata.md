# WebhookPackagePublishedPackagePackageVersionNpmMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**npm_user** | **str** |  | [optional] 
**author** | **object** |  | [optional] 
**bugs** | **object** |  | [optional] 
**dependencies** | **object** |  | [optional] 
**dev_dependencies** | **object** |  | [optional] 
**peer_dependencies** | **object** |  | [optional] 
**optional_dependencies** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**dist** | **object** |  | [optional] 
**git_head** | **str** |  | [optional] 
**homepage** | **str** |  | [optional] 
**license** | **str** |  | [optional] 
**main** | **str** |  | [optional] 
**repository** | **object** |  | [optional] 
**scripts** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**node_version** | **str** |  | [optional] 
**npm_version** | **str** |  | [optional] 
**has_shrinkwrap** | **bool** |  | [optional] 
**maintainers** | **List[object]** |  | [optional] 
**contributors** | **List[object]** |  | [optional] 
**engines** | **object** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**files** | **List[str]** |  | [optional] 
**bin** | **object** |  | [optional] 
**man** | **object** |  | [optional] 
**directories** | **object** |  | [optional] 
**os** | **List[str]** |  | [optional] 
**cpu** | **List[str]** |  | [optional] 
**readme** | **str** |  | [optional] 
**installation_command** | **str** |  | [optional] 
**release_id** | **int** |  | [optional] 
**commit_oid** | **str** |  | [optional] 
**published_via_actions** | **bool** |  | [optional] 
**deleted_by_id** | **int** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_package_published_package_package_version_npm_metadata import WebhookPackagePublishedPackagePackageVersionNpmMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPackagePublishedPackagePackageVersionNpmMetadata from a JSON string
webhook_package_published_package_package_version_npm_metadata_instance = WebhookPackagePublishedPackagePackageVersionNpmMetadata.from_json(json)
# print the JSON string representation of the object
print(WebhookPackagePublishedPackagePackageVersionNpmMetadata.to_json())

# convert the object into a dict
webhook_package_published_package_package_version_npm_metadata_dict = webhook_package_published_package_package_version_npm_metadata_instance.to_dict()
# create an instance of WebhookPackagePublishedPackagePackageVersionNpmMetadata from a dict
webhook_package_published_package_package_version_npm_metadata_from_dict = WebhookPackagePublishedPackagePackageVersionNpmMetadata.from_dict(webhook_package_published_package_package_version_npm_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


