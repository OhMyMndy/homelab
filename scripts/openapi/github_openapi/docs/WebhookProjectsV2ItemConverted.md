# WebhookProjectsV2ItemConverted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookProjectsV2ItemConvertedChanges**](WebhookProjectsV2ItemConvertedChanges.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**projects_v2_item** | [**ProjectsV2Item**](ProjectsV2Item.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_projects_v2_item_converted import WebhookProjectsV2ItemConverted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2ItemConverted from a JSON string
webhook_projects_v2_item_converted_instance = WebhookProjectsV2ItemConverted.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2ItemConverted.to_json())

# convert the object into a dict
webhook_projects_v2_item_converted_dict = webhook_projects_v2_item_converted_instance.to_dict()
# create an instance of WebhookProjectsV2ItemConverted from a dict
webhook_projects_v2_item_converted_from_dict = WebhookProjectsV2ItemConverted.from_dict(webhook_projects_v2_item_converted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


