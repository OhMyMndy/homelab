# WebhookPullRequestReviewRequestRemoved


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** | The pull request number. | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest7**](PullRequest7.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**requested_reviewer** | [**User2**](User2.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**requested_team** | [**Team1**](Team1.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_request_removed import WebhookPullRequestReviewRequestRemoved

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewRequestRemoved from a JSON string
webhook_pull_request_review_request_removed_instance = WebhookPullRequestReviewRequestRemoved.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewRequestRemoved.to_json())

# convert the object into a dict
webhook_pull_request_review_request_removed_dict = webhook_pull_request_review_request_removed_instance.to_dict()
# create an instance of WebhookPullRequestReviewRequestRemoved from a dict
webhook_pull_request_review_request_removed_from_dict = WebhookPullRequestReviewRequestRemoved.from_dict(webhook_pull_request_review_request_removed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


