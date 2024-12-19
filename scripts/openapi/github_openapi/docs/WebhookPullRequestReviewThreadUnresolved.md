# WebhookPullRequestReviewThreadUnresolved


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**SimplePullRequest4**](SimplePullRequest4.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**thread** | [**WebhookPullRequestReviewThreadUnresolvedThread**](WebhookPullRequestReviewThreadUnresolvedThread.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_thread_unresolved import WebhookPullRequestReviewThreadUnresolved

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewThreadUnresolved from a JSON string
webhook_pull_request_review_thread_unresolved_instance = WebhookPullRequestReviewThreadUnresolved.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewThreadUnresolved.to_json())

# convert the object into a dict
webhook_pull_request_review_thread_unresolved_dict = webhook_pull_request_review_thread_unresolved_instance.to_dict()
# create an instance of WebhookPullRequestReviewThreadUnresolved from a dict
webhook_pull_request_review_thread_unresolved_from_dict = WebhookPullRequestReviewThreadUnresolved.from_dict(webhook_pull_request_review_thread_unresolved_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


