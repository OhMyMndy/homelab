# WebhookDiscussionEditedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**WebhookDiscussionCommentEditedChangesBody**](WebhookDiscussionCommentEditedChangesBody.md) |  | [optional] 
**title** | [**WebhookDiscussionCommentEditedChangesBody**](WebhookDiscussionCommentEditedChangesBody.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_discussion_edited_changes import WebhookDiscussionEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionEditedChanges from a JSON string
webhook_discussion_edited_changes_instance = WebhookDiscussionEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionEditedChanges.to_json())

# convert the object into a dict
webhook_discussion_edited_changes_dict = webhook_discussion_edited_changes_instance.to_dict()
# create an instance of WebhookDiscussionEditedChanges from a dict
webhook_discussion_edited_changes_from_dict = WebhookDiscussionEditedChanges.from_dict(webhook_discussion_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


