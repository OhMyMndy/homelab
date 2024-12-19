# WebhookPullRequestReadyForReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** | The pull request number. | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequestWebhook**](PullRequestWebhook.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_ready_for_review import WebhookPullRequestReadyForReview

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReadyForReview from a JSON string
webhook_pull_request_ready_for_review_instance = WebhookPullRequestReadyForReview.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReadyForReview.to_json())

# convert the object into a dict
webhook_pull_request_ready_for_review_dict = webhook_pull_request_ready_for_review_instance.to_dict()
# create an instance of WebhookPullRequestReadyForReview from a dict
webhook_pull_request_ready_for_review_from_dict = WebhookPullRequestReadyForReview.from_dict(webhook_pull_request_ready_for_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


