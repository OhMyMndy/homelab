# WebhookProjectsV2StatusUpdateEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookProjectsV2StatusUpdateEditedChanges**](WebhookProjectsV2StatusUpdateEditedChanges.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**projects_v2_status_update** | [**ProjectsV2StatusUpdate**](ProjectsV2StatusUpdate.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_projects_v2_status_update_edited import WebhookProjectsV2StatusUpdateEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2StatusUpdateEdited from a JSON string
webhook_projects_v2_status_update_edited_instance = WebhookProjectsV2StatusUpdateEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2StatusUpdateEdited.to_json())

# convert the object into a dict
webhook_projects_v2_status_update_edited_dict = webhook_projects_v2_status_update_edited_instance.to_dict()
# create an instance of WebhookProjectsV2StatusUpdateEdited from a dict
webhook_projects_v2_status_update_edited_from_dict = WebhookProjectsV2StatusUpdateEdited.from_dict(webhook_projects_v2_status_update_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


