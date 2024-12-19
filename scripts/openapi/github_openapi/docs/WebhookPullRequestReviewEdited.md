# WebhookPullRequestReviewEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookPullRequestReviewEditedChanges**](WebhookPullRequestReviewEditedChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**SimplePullRequest1**](SimplePullRequest1.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**review** | [**WebhooksReview**](WebhooksReview.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_edited import WebhookPullRequestReviewEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewEdited from a JSON string
webhook_pull_request_review_edited_instance = WebhookPullRequestReviewEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewEdited.to_json())

# convert the object into a dict
webhook_pull_request_review_edited_dict = webhook_pull_request_review_edited_instance.to_dict()
# create an instance of WebhookPullRequestReviewEdited from a dict
webhook_pull_request_review_edited_from_dict = WebhookPullRequestReviewEdited.from_dict(webhook_pull_request_review_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


