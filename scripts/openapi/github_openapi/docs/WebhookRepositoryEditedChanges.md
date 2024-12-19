# WebhookRepositoryEditedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_branch** | [**WebhookDiscussionCommentEditedChangesBody**](WebhookDiscussionCommentEditedChangesBody.md) |  | [optional] 
**description** | [**WebhookProjectCardEditedChangesNote**](WebhookProjectCardEditedChangesNote.md) |  | [optional] 
**homepage** | [**WebhookProjectCardEditedChangesNote**](WebhookProjectCardEditedChangesNote.md) |  | [optional] 
**topics** | [**WebhookRepositoryEditedChangesTopics**](WebhookRepositoryEditedChangesTopics.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_repository_edited_changes import WebhookRepositoryEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryEditedChanges from a JSON string
webhook_repository_edited_changes_instance = WebhookRepositoryEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryEditedChanges.to_json())

# convert the object into a dict
webhook_repository_edited_changes_dict = webhook_repository_edited_changes_instance.to_dict()
# create an instance of WebhookRepositoryEditedChanges from a dict
webhook_repository_edited_changes_from_dict = WebhookRepositoryEditedChanges.from_dict(webhook_repository_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


