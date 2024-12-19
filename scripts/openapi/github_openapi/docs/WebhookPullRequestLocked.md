# WebhookPullRequestLocked


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** | The pull request number. | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest5**](PullRequest5.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_locked import WebhookPullRequestLocked

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestLocked from a JSON string
webhook_pull_request_locked_instance = WebhookPullRequestLocked.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestLocked.to_json())

# convert the object into a dict
webhook_pull_request_locked_dict = webhook_pull_request_locked_instance.to_dict()
# create an instance of WebhookPullRequestLocked from a dict
webhook_pull_request_locked_from_dict = WebhookPullRequestLocked.from_dict(webhook_pull_request_locked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


