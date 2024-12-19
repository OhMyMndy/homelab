# WebhookPullRequestLabeled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**label** | [**WebhooksLabel**](WebhooksLabel.md) |  | [optional] 
**number** | **int** | The pull request number. | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest4**](PullRequest4.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_labeled import WebhookPullRequestLabeled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestLabeled from a JSON string
webhook_pull_request_labeled_instance = WebhookPullRequestLabeled.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestLabeled.to_json())

# convert the object into a dict
webhook_pull_request_labeled_dict = webhook_pull_request_labeled_instance.to_dict()
# create an instance of WebhookPullRequestLabeled from a dict
webhook_pull_request_labeled_from_dict = WebhookPullRequestLabeled.from_dict(webhook_pull_request_labeled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


