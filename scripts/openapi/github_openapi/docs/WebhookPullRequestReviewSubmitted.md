# WebhookPullRequestReviewSubmitted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**SimplePullRequest2**](SimplePullRequest2.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**review** | [**WebhooksReview**](WebhooksReview.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_submitted import WebhookPullRequestReviewSubmitted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewSubmitted from a JSON string
webhook_pull_request_review_submitted_instance = WebhookPullRequestReviewSubmitted.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewSubmitted.to_json())

# convert the object into a dict
webhook_pull_request_review_submitted_dict = webhook_pull_request_review_submitted_instance.to_dict()
# create an instance of WebhookPullRequestReviewSubmitted from a dict
webhook_pull_request_review_submitted_from_dict = WebhookPullRequestReviewSubmitted.from_dict(webhook_pull_request_review_submitted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


