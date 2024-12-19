# WebhookPullRequestReviewThreadResolved


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**SimplePullRequest3**](SimplePullRequest3.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**thread** | [**WebhookPullRequestReviewThreadResolvedThread**](WebhookPullRequestReviewThreadResolvedThread.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_thread_resolved import WebhookPullRequestReviewThreadResolved

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewThreadResolved from a JSON string
webhook_pull_request_review_thread_resolved_instance = WebhookPullRequestReviewThreadResolved.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewThreadResolved.to_json())

# convert the object into a dict
webhook_pull_request_review_thread_resolved_dict = webhook_pull_request_review_thread_resolved_instance.to_dict()
# create an instance of WebhookPullRequestReviewThreadResolved from a dict
webhook_pull_request_review_thread_resolved_from_dict = WebhookPullRequestReviewThreadResolved.from_dict(webhook_pull_request_review_thread_resolved_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


