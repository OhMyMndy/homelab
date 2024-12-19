# WebhookPullRequestEditedChanges

The changes to the comment if the action was `edited`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | [**WebhookPullRequestEditedChangesBase**](WebhookPullRequestEditedChangesBase.md) |  | [optional] 
**body** | [**WebhookProjectEditedChangesBody**](WebhookProjectEditedChangesBody.md) |  | [optional] 
**title** | [**WebhookMilestoneEditedChangesTitle**](WebhookMilestoneEditedChangesTitle.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_pull_request_edited_changes import WebhookPullRequestEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestEditedChanges from a JSON string
webhook_pull_request_edited_changes_instance = WebhookPullRequestEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestEditedChanges.to_json())

# convert the object into a dict
webhook_pull_request_edited_changes_dict = webhook_pull_request_edited_changes_instance.to_dict()
# create an instance of WebhookPullRequestEditedChanges from a dict
webhook_pull_request_edited_changes_from_dict = WebhookPullRequestEditedChanges.from_dict(webhook_pull_request_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


