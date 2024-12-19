# WebhookProjectsV2StatusUpdateEditedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**WebhookMemberEditedChangesPermission**](WebhookMemberEditedChangesPermission.md) |  | [optional] 
**status** | [**WebhookProjectsV2StatusUpdateEditedChangesStatus**](WebhookProjectsV2StatusUpdateEditedChangesStatus.md) |  | [optional] 
**start_date** | [**WebhookProjectsV2StatusUpdateEditedChangesStartDate**](WebhookProjectsV2StatusUpdateEditedChangesStartDate.md) |  | [optional] 
**target_date** | [**WebhookProjectsV2StatusUpdateEditedChangesStartDate**](WebhookProjectsV2StatusUpdateEditedChangesStartDate.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_projects_v2_status_update_edited_changes import WebhookProjectsV2StatusUpdateEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2StatusUpdateEditedChanges from a JSON string
webhook_projects_v2_status_update_edited_changes_instance = WebhookProjectsV2StatusUpdateEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2StatusUpdateEditedChanges.to_json())

# convert the object into a dict
webhook_projects_v2_status_update_edited_changes_dict = webhook_projects_v2_status_update_edited_changes_instance.to_dict()
# create an instance of WebhookProjectsV2StatusUpdateEditedChanges from a dict
webhook_projects_v2_status_update_edited_changes_from_dict = WebhookProjectsV2StatusUpdateEditedChanges.from_dict(webhook_projects_v2_status_update_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


