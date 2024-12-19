# WebhookPullRequestReviewCommentCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**comment** | [**PullRequestReviewComment**](PullRequestReviewComment.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**WebhookPullRequestReviewCommentCreatedPullRequest**](WebhookPullRequestReviewCommentCreatedPullRequest.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_comment_created import WebhookPullRequestReviewCommentCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewCommentCreated from a JSON string
webhook_pull_request_review_comment_created_instance = WebhookPullRequestReviewCommentCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewCommentCreated.to_json())

# convert the object into a dict
webhook_pull_request_review_comment_created_dict = webhook_pull_request_review_comment_created_instance.to_dict()
# create an instance of WebhookPullRequestReviewCommentCreated from a dict
webhook_pull_request_review_comment_created_from_dict = WebhookPullRequestReviewCommentCreated.from_dict(webhook_pull_request_review_comment_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


