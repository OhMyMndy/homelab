# WebhookPullRequestOpened


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
from github_openapi.models.webhook_pull_request_opened import WebhookPullRequestOpened

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestOpened from a JSON string
webhook_pull_request_opened_instance = WebhookPullRequestOpened.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestOpened.to_json())

# convert the object into a dict
webhook_pull_request_opened_dict = webhook_pull_request_opened_instance.to_dict()
# create an instance of WebhookPullRequestOpened from a dict
webhook_pull_request_opened_from_dict = WebhookPullRequestOpened.from_dict(webhook_pull_request_opened_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


