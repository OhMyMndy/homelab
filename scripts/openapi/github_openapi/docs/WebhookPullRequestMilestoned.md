# WebhookPullRequestMilestoned


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**milestone** | [**Milestone**](Milestone.md) |  | [optional] 
**number** | **int** | The pull request number. | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**WebhooksPullRequest5**](WebhooksPullRequest5.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_pull_request_milestoned import WebhookPullRequestMilestoned

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestMilestoned from a JSON string
webhook_pull_request_milestoned_instance = WebhookPullRequestMilestoned.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestMilestoned.to_json())

# convert the object into a dict
webhook_pull_request_milestoned_dict = webhook_pull_request_milestoned_instance.to_dict()
# create an instance of WebhookPullRequestMilestoned from a dict
webhook_pull_request_milestoned_from_dict = WebhookPullRequestMilestoned.from_dict(webhook_pull_request_milestoned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


