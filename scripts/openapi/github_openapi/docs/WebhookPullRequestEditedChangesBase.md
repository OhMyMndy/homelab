# WebhookPullRequestEditedChangesBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | [**WebhookDiscussionCommentEditedChangesBody**](WebhookDiscussionCommentEditedChangesBody.md) |  | 
**sha** | [**WebhookDiscussionCommentEditedChangesBody**](WebhookDiscussionCommentEditedChangesBody.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_edited_changes_base import WebhookPullRequestEditedChangesBase

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestEditedChangesBase from a JSON string
webhook_pull_request_edited_changes_base_instance = WebhookPullRequestEditedChangesBase.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestEditedChangesBase.to_json())

# convert the object into a dict
webhook_pull_request_edited_changes_base_dict = webhook_pull_request_edited_changes_base_instance.to_dict()
# create an instance of WebhookPullRequestEditedChangesBase from a dict
webhook_pull_request_edited_changes_base_from_dict = WebhookPullRequestEditedChangesBase.from_dict(webhook_pull_request_edited_changes_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


