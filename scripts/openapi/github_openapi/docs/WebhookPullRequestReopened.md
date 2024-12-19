# WebhookPullRequestReopened


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
from github_openapi.models.webhook_pull_request_reopened import WebhookPullRequestReopened

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReopened from a JSON string
webhook_pull_request_reopened_instance = WebhookPullRequestReopened.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReopened.to_json())

# convert the object into a dict
webhook_pull_request_reopened_dict = webhook_pull_request_reopened_instance.to_dict()
# create an instance of WebhookPullRequestReopened from a dict
webhook_pull_request_reopened_from_dict = WebhookPullRequestReopened.from_dict(webhook_pull_request_reopened_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


