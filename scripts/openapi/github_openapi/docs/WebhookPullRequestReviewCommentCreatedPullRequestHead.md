# WebhookPullRequestReviewCommentCreatedPullRequestHead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository7**](Repository7.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_comment_created_pull_request_head import WebhookPullRequestReviewCommentCreatedPullRequestHead

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewCommentCreatedPullRequestHead from a JSON string
webhook_pull_request_review_comment_created_pull_request_head_instance = WebhookPullRequestReviewCommentCreatedPullRequestHead.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewCommentCreatedPullRequestHead.to_json())

# convert the object into a dict
webhook_pull_request_review_comment_created_pull_request_head_dict = webhook_pull_request_review_comment_created_pull_request_head_instance.to_dict()
# create an instance of WebhookPullRequestReviewCommentCreatedPullRequestHead from a dict
webhook_pull_request_review_comment_created_pull_request_head_from_dict = WebhookPullRequestReviewCommentCreatedPullRequestHead.from_dict(webhook_pull_request_review_comment_created_pull_request_head_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


