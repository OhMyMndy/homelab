# WebhookPullRequestUnlocked


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** | The pull request number. | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest13**](PullRequest13.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_unlocked import WebhookPullRequestUnlocked

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestUnlocked from a JSON string
webhook_pull_request_unlocked_instance = WebhookPullRequestUnlocked.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestUnlocked.to_json())

# convert the object into a dict
webhook_pull_request_unlocked_dict = webhook_pull_request_unlocked_instance.to_dict()
# create an instance of WebhookPullRequestUnlocked from a dict
webhook_pull_request_unlocked_from_dict = WebhookPullRequestUnlocked.from_dict(webhook_pull_request_unlocked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


