# WebhookRegistryPackagePublishedRegistryPackagePackageVersionNpmMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**npm_user** | **str** |  | [optional] 
**author** | [**Deployment1Payload**](Deployment1Payload.md) |  | [optional] 
**bugs** | [**Deployment1Payload**](Deployment1Payload.md) |  | [optional] 
**dependencies** | **object** |  | [optional] 
**dev_dependencies** | **object** |  | [optional] 
**peer_dependencies** | **object** |  | [optional] 
**optional_dependencies** | **object** |  | [optional] 
**description** | **str** |  | [optional] 
**dist** | [**Deployment1Payload**](Deployment1Payload.md) |  | [optional] 
**git_head** | **str** |  | [optional] 
**homepage** | **str** |  | [optional] 
**license** | **str** |  | [optional] 
**main** | **str** |  | [optional] 
**repository** | [**Deployment1Payload**](Deployment1Payload.md) |  | [optional] 
**scripts** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**node_version** | **str** |  | [optional] 
**npm_version** | **str** |  | [optional] 
**has_shrinkwrap** | **bool** |  | [optional] 
**maintainers** | **List[str]** |  | [optional] 
**contributors** | **List[str]** |  | [optional] 
**engines** | **object** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**files** | **List[str]** |  | [optional] 
**bin** | **object** |  | [optional] 
**man** | **object** |  | [optional] 
**directories** | [**Deployment1Payload**](Deployment1Payload.md) |  | [optional] 
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
from github_openapi.models.webhook_registry_package_published_registry_package_package_version_npm_metadata import WebhookRegistryPackagePublishedRegistryPackagePackageVersionNpmMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRegistryPackagePublishedRegistryPackagePackageVersionNpmMetadata from a JSON string
webhook_registry_package_published_registry_package_package_version_npm_metadata_instance = WebhookRegistryPackagePublishedRegistryPackagePackageVersionNpmMetadata.from_json(json)
# print the JSON string representation of the object
print(WebhookRegistryPackagePublishedRegistryPackagePackageVersionNpmMetadata.to_json())

# convert the object into a dict
webhook_registry_package_published_registry_package_package_version_npm_metadata_dict = webhook_registry_package_published_registry_package_package_version_npm_metadata_instance.to_dict()
# create an instance of WebhookRegistryPackagePublishedRegistryPackagePackageVersionNpmMetadata from a dict
webhook_registry_package_published_registry_package_package_version_npm_metadata_from_dict = WebhookRegistryPackagePublishedRegistryPackagePackageVersionNpmMetadata.from_dict(webhook_registry_package_published_registry_package_package_version_npm_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


