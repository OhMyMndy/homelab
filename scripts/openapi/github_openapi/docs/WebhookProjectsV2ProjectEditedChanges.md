# WebhookProjectsV2ProjectEditedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**WebhookMemberEditedChangesPermission**](WebhookMemberEditedChangesPermission.md) |  | [optional] 
**public** | [**WebhookProjectsV2ProjectEditedChangesPublic**](WebhookProjectsV2ProjectEditedChangesPublic.md) |  | [optional] 
**short_description** | [**WebhookMemberEditedChangesPermission**](WebhookMemberEditedChangesPermission.md) |  | [optional] 
**title** | [**WebhookProjectsV2ProjectEditedChangesTitle**](WebhookProjectsV2ProjectEditedChangesTitle.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_projects_v2_project_edited_changes import WebhookProjectsV2ProjectEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2ProjectEditedChanges from a JSON string
webhook_projects_v2_project_edited_changes_instance = WebhookProjectsV2ProjectEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2ProjectEditedChanges.to_json())

# convert the object into a dict
webhook_projects_v2_project_edited_changes_dict = webhook_projects_v2_project_edited_changes_instance.to_dict()
# create an instance of WebhookProjectsV2ProjectEditedChanges from a dict
webhook_projects_v2_project_edited_changes_from_dict = WebhookProjectsV2ProjectEditedChanges.from_dict(webhook_projects_v2_project_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


