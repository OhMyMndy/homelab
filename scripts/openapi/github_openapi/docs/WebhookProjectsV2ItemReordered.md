# WebhookProjectsV2ItemReordered


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookProjectsV2ItemReorderedChanges**](WebhookProjectsV2ItemReorderedChanges.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**projects_v2_item** | [**ProjectsV2Item**](ProjectsV2Item.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_projects_v2_item_reordered import WebhookProjectsV2ItemReordered

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2ItemReordered from a JSON string
webhook_projects_v2_item_reordered_instance = WebhookProjectsV2ItemReordered.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2ItemReordered.to_json())

# convert the object into a dict
webhook_projects_v2_item_reordered_dict = webhook_projects_v2_item_reordered_instance.to_dict()
# create an instance of WebhookProjectsV2ItemReordered from a dict
webhook_projects_v2_item_reordered_from_dict = WebhookProjectsV2ItemReordered.from_dict(webhook_projects_v2_item_reordered_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


