# WebhookPullRequestReviewDismissed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**SimplePullRequest**](SimplePullRequest.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**review** | [**WebhookPullRequestReviewDismissedReview**](WebhookPullRequestReviewDismissedReview.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_dismissed import WebhookPullRequestReviewDismissed

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewDismissed from a JSON string
webhook_pull_request_review_dismissed_instance = WebhookPullRequestReviewDismissed.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewDismissed.to_json())

# convert the object into a dict
webhook_pull_request_review_dismissed_dict = webhook_pull_request_review_dismissed_instance.to_dict()
# create an instance of WebhookPullRequestReviewDismissed from a dict
webhook_pull_request_review_dismissed_from_dict = WebhookPullRequestReviewDismissed.from_dict(webhook_pull_request_review_dismissed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


