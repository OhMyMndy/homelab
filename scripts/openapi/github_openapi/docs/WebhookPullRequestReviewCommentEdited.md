# WebhookPullRequestReviewCommentEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhooksChanges**](WebhooksChanges.md) |  | 
**comment** | [**WebhooksReviewComment**](WebhooksReviewComment.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**WebhookPullRequestReviewCommentEditedPullRequest**](WebhookPullRequestReviewCommentEditedPullRequest.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_comment_edited import WebhookPullRequestReviewCommentEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewCommentEdited from a JSON string
webhook_pull_request_review_comment_edited_instance = WebhookPullRequestReviewCommentEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewCommentEdited.to_json())

# convert the object into a dict
webhook_pull_request_review_comment_edited_dict = webhook_pull_request_review_comment_edited_instance.to_dict()
# create an instance of WebhookPullRequestReviewCommentEdited from a dict
webhook_pull_request_review_comment_edited_from_dict = WebhookPullRequestReviewCommentEdited.from_dict(webhook_pull_request_review_comment_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


