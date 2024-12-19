# WebhookPullRequestReviewCommentDeletedPullRequestHead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository4**](Repository4.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_comment_deleted_pull_request_head import WebhookPullRequestReviewCommentDeletedPullRequestHead

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewCommentDeletedPullRequestHead from a JSON string
webhook_pull_request_review_comment_deleted_pull_request_head_instance = WebhookPullRequestReviewCommentDeletedPullRequestHead.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewCommentDeletedPullRequestHead.to_json())

# convert the object into a dict
webhook_pull_request_review_comment_deleted_pull_request_head_dict = webhook_pull_request_review_comment_deleted_pull_request_head_instance.to_dict()
# create an instance of WebhookPullRequestReviewCommentDeletedPullRequestHead from a dict
webhook_pull_request_review_comment_deleted_pull_request_head_from_dict = WebhookPullRequestReviewCommentDeletedPullRequestHead.from_dict(webhook_pull_request_review_comment_deleted_pull_request_head_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


