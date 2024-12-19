# WebhookProjectEditedChanges

The changes to the project if the action was `edited`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**WebhookProjectEditedChangesBody**](WebhookProjectEditedChangesBody.md) |  | [optional] 
**name** | [**WebhookProjectEditedChangesName**](WebhookProjectEditedChangesName.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_project_edited_changes import WebhookProjectEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectEditedChanges from a JSON string
webhook_project_edited_changes_instance = WebhookProjectEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectEditedChanges.to_json())

# convert the object into a dict
webhook_project_edited_changes_dict = webhook_project_edited_changes_instance.to_dict()
# create an instance of WebhookProjectEditedChanges from a dict
webhook_project_edited_changes_from_dict = WebhookProjectEditedChanges.from_dict(webhook_project_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


