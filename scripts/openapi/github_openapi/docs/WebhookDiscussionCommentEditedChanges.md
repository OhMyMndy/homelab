# WebhookDiscussionCommentEditedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**WebhookDiscussionCommentEditedChangesBody**](WebhookDiscussionCommentEditedChangesBody.md) |  | 

## Example

```python
from github_openapi.models.webhook_discussion_comment_edited_changes import WebhookDiscussionCommentEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionCommentEditedChanges from a JSON string
webhook_discussion_comment_edited_changes_instance = WebhookDiscussionCommentEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionCommentEditedChanges.to_json())

# convert the object into a dict
webhook_discussion_comment_edited_changes_dict = webhook_discussion_comment_edited_changes_instance.to_dict()
# create an instance of WebhookDiscussionCommentEditedChanges from a dict
webhook_discussion_comment_edited_changes_from_dict = WebhookDiscussionCommentEditedChanges.from_dict(webhook_discussion_comment_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


