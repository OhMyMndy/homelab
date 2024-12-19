# WebhookDiscussionCommentEditedChangesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_discussion_comment_edited_changes_body import WebhookDiscussionCommentEditedChangesBody

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionCommentEditedChangesBody from a JSON string
webhook_discussion_comment_edited_changes_body_instance = WebhookDiscussionCommentEditedChangesBody.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionCommentEditedChangesBody.to_json())

# convert the object into a dict
webhook_discussion_comment_edited_changes_body_dict = webhook_discussion_comment_edited_changes_body_instance.to_dict()
# create an instance of WebhookDiscussionCommentEditedChangesBody from a dict
webhook_discussion_comment_edited_changes_body_from_dict = WebhookDiscussionCommentEditedChangesBody.from_dict(webhook_discussion_comment_edited_changes_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


