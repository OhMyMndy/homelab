# WebhookPullRequestClosed


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
from github_openapi.models.webhook_pull_request_closed import WebhookPullRequestClosed

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestClosed from a JSON string
webhook_pull_request_closed_instance = WebhookPullRequestClosed.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestClosed.to_json())

# convert the object into a dict
webhook_pull_request_closed_dict = webhook_pull_request_closed_instance.to_dict()
# create an instance of WebhookPullRequestClosed from a dict
webhook_pull_request_closed_from_dict = WebhookPullRequestClosed.from_dict(webhook_pull_request_closed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


