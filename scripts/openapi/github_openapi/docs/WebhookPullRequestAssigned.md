# WebhookPullRequestAssigned


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**assignee** | [**WebhooksUser**](WebhooksUser.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** | The pull request number. | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest**](PullRequest.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_assigned import WebhookPullRequestAssigned

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestAssigned from a JSON string
webhook_pull_request_assigned_instance = WebhookPullRequestAssigned.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestAssigned.to_json())

# convert the object into a dict
webhook_pull_request_assigned_dict = webhook_pull_request_assigned_instance.to_dict()
# create an instance of WebhookPullRequestAssigned from a dict
webhook_pull_request_assigned_from_dict = WebhookPullRequestAssigned.from_dict(webhook_pull_request_assigned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


