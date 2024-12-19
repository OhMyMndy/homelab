# WebhookPullRequestReviewRequested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** | The pull request number. | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest9**](PullRequest9.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**requested_reviewer** | [**User4**](User4.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**requested_team** | [**Team**](Team.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_requested import WebhookPullRequestReviewRequested

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewRequested from a JSON string
webhook_pull_request_review_requested_instance = WebhookPullRequestReviewRequested.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewRequested.to_json())

# convert the object into a dict
webhook_pull_request_review_requested_dict = webhook_pull_request_review_requested_instance.to_dict()
# create an instance of WebhookPullRequestReviewRequested from a dict
webhook_pull_request_review_requested_from_dict = WebhookPullRequestReviewRequested.from_dict(webhook_pull_request_review_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


