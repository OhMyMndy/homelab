# WebhookPackagePublishedPackagePackageVersionNugetMetadataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ActionsGetWorkflowWorkflowIdParameter**](ActionsGetWorkflowWorkflowIdParameter.md) |  | [optional] 
**name** | **str** |  | [optional] 
**value** | [**WebhookPackagePublishedPackagePackageVersionNugetMetadataInnerValue**](WebhookPackagePublishedPackagePackageVersionNugetMetadataInnerValue.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_package_published_package_package_version_nuget_metadata_inner import WebhookPackagePublishedPackagePackageVersionNugetMetadataInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPackagePublishedPackagePackageVersionNugetMetadataInner from a JSON string
webhook_package_published_package_package_version_nuget_metadata_inner_instance = WebhookPackagePublishedPackagePackageVersionNugetMetadataInner.from_json(json)
# print the JSON string representation of the object
print(WebhookPackagePublishedPackagePackageVersionNugetMetadataInner.to_json())

# convert the object into a dict
webhook_package_published_package_package_version_nuget_metadata_inner_dict = webhook_package_published_package_package_version_nuget_metadata_inner_instance.to_dict()
# create an instance of WebhookPackagePublishedPackagePackageVersionNugetMetadataInner from a dict
webhook_package_published_package_package_version_nuget_metadata_inner_from_dict = WebhookPackagePublishedPackagePackageVersionNugetMetadataInner.from_dict(webhook_package_published_package_package_version_nuget_metadata_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


