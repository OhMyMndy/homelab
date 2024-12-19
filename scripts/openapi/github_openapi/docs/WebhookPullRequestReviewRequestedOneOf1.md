# WebhookPullRequestReviewRequestedOneOf1


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
**requested_team** | [**Team**](Team.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_requested_one_of1 import WebhookPullRequestReviewRequestedOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewRequestedOneOf1 from a JSON string
webhook_pull_request_review_requested_one_of1_instance = WebhookPullRequestReviewRequestedOneOf1.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewRequestedOneOf1.to_json())

# convert the object into a dict
webhook_pull_request_review_requested_one_of1_dict = webhook_pull_request_review_requested_one_of1_instance.to_dict()
# create an instance of WebhookPullRequestReviewRequestedOneOf1 from a dict
webhook_pull_request_review_requested_one_of1_from_dict = WebhookPullRequestReviewRequestedOneOf1.from_dict(webhook_pull_request_review_requested_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


