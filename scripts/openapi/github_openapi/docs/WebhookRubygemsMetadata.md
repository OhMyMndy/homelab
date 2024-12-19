# WebhookRubygemsMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**readme** | **str** |  | [optional] 
**homepage** | **str** |  | [optional] 
**version_info** | [**WebhookRubygemsMetadataVersionInfo**](WebhookRubygemsMetadataVersionInfo.md) |  | [optional] 
**platform** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**repo** | **str** |  | [optional] 
**dependencies** | **List[Dict[str, str]]** |  | [optional] 
**commit_oid** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_rubygems_metadata import WebhookRubygemsMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRubygemsMetadata from a JSON string
webhook_rubygems_metadata_instance = WebhookRubygemsMetadata.from_json(json)
# print the JSON string representation of the object
print(WebhookRubygemsMetadata.to_json())

# convert the object into a dict
webhook_rubygems_metadata_dict = webhook_rubygems_metadata_instance.to_dict()
# create an instance of WebhookRubygemsMetadata from a dict
webhook_rubygems_metadata_from_dict = WebhookRubygemsMetadata.from_dict(webhook_rubygems_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


