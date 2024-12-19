# WebhookPullRequestReviewRequestRemovedOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** | The pull request number. | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest6**](PullRequest6.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**requested_reviewer** | [**User2**](User2.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_request_removed_one_of import WebhookPullRequestReviewRequestRemovedOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewRequestRemovedOneOf from a JSON string
webhook_pull_request_review_request_removed_one_of_instance = WebhookPullRequestReviewRequestRemovedOneOf.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewRequestRemovedOneOf.to_json())

# convert the object into a dict
webhook_pull_request_review_request_removed_one_of_dict = webhook_pull_request_review_request_removed_one_of_instance.to_dict()
# create an instance of WebhookPullRequestReviewRequestRemovedOneOf from a dict
webhook_pull_request_review_request_removed_one_of_from_dict = WebhookPullRequestReviewRequestRemovedOneOf.from_dict(webhook_pull_request_review_request_removed_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


