# WebhookProjectsV2ItemEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookProjectsV2ItemEditedChanges**](WebhookProjectsV2ItemEditedChanges.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**projects_v2_item** | [**ProjectsV2Item**](ProjectsV2Item.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_projects_v2_item_edited import WebhookProjectsV2ItemEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2ItemEdited from a JSON string
webhook_projects_v2_item_edited_instance = WebhookProjectsV2ItemEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2ItemEdited.to_json())

# convert the object into a dict
webhook_projects_v2_item_edited_dict = webhook_projects_v2_item_edited_instance.to_dict()
# create an instance of WebhookProjectsV2ItemEdited from a dict
webhook_projects_v2_item_edited_from_dict = WebhookProjectsV2ItemEdited.from_dict(webhook_projects_v2_item_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


