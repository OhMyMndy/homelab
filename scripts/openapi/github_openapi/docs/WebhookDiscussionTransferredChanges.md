# WebhookDiscussionTransferredChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_discussion** | [**Discussion**](Discussion.md) |  | 
**new_repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 

## Example

```python
from github_openapi.models.webhook_discussion_transferred_changes import WebhookDiscussionTransferredChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionTransferredChanges from a JSON string
webhook_discussion_transferred_changes_instance = WebhookDiscussionTransferredChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionTransferredChanges.to_json())

# convert the object into a dict
webhook_discussion_transferred_changes_dict = webhook_discussion_transferred_changes_instance.to_dict()
# create an instance of WebhookDiscussionTransferredChanges from a dict
webhook_discussion_transferred_changes_from_dict = WebhookDiscussionTransferredChanges.from_dict(webhook_discussion_transferred_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


