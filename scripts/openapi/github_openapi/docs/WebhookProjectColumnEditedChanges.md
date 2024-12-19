# WebhookProjectColumnEditedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**WebhookDiscussionCommentEditedChangesBody**](WebhookDiscussionCommentEditedChangesBody.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_project_column_edited_changes import WebhookProjectColumnEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectColumnEditedChanges from a JSON string
webhook_project_column_edited_changes_instance = WebhookProjectColumnEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectColumnEditedChanges.to_json())

# convert the object into a dict
webhook_project_column_edited_changes_dict = webhook_project_column_edited_changes_instance.to_dict()
# create an instance of WebhookProjectColumnEditedChanges from a dict
webhook_project_column_edited_changes_from_dict = WebhookProjectColumnEditedChanges.from_dict(webhook_project_column_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


