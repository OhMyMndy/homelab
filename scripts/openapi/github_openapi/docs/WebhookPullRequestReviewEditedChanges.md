# WebhookPullRequestReviewEditedChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**WebhookProjectEditedChangesBody**](WebhookProjectEditedChangesBody.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_pull_request_review_edited_changes import WebhookPullRequestReviewEditedChanges

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewEditedChanges from a JSON string
webhook_pull_request_review_edited_changes_instance = WebhookPullRequestReviewEditedChanges.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewEditedChanges.to_json())

# convert the object into a dict
webhook_pull_request_review_edited_changes_dict = webhook_pull_request_review_edited_changes_instance.to_dict()
# create an instance of WebhookPullRequestReviewEditedChanges from a dict
webhook_pull_request_review_edited_changes_from_dict = WebhookPullRequestReviewEditedChanges.from_dict(webhook_pull_request_review_edited_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


