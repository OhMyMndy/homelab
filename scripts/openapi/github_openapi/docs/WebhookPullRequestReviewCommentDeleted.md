# WebhookPullRequestReviewCommentDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**comment** | [**WebhooksReviewComment**](WebhooksReviewComment.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**WebhookPullRequestReviewCommentDeletedPullRequest**](WebhookPullRequestReviewCommentDeletedPullRequest.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_comment_deleted import WebhookPullRequestReviewCommentDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewCommentDeleted from a JSON string
webhook_pull_request_review_comment_deleted_instance = WebhookPullRequestReviewCommentDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewCommentDeleted.to_json())

# convert the object into a dict
webhook_pull_request_review_comment_deleted_dict = webhook_pull_request_review_comment_deleted_instance.to_dict()
# create an instance of WebhookPullRequestReviewCommentDeleted from a dict
webhook_pull_request_review_comment_deleted_from_dict = WebhookPullRequestReviewCommentDeleted.from_dict(webhook_pull_request_review_comment_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


