# WebhookPullRequestSynchronize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**after** | **str** |  | 
**before** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** | The pull request number. | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest10**](PullRequest10.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_synchronize import WebhookPullRequestSynchronize

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestSynchronize from a JSON string
webhook_pull_request_synchronize_instance = WebhookPullRequestSynchronize.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestSynchronize.to_json())

# convert the object into a dict
webhook_pull_request_synchronize_dict = webhook_pull_request_synchronize_instance.to_dict()
# create an instance of WebhookPullRequestSynchronize from a dict
webhook_pull_request_synchronize_from_dict = WebhookPullRequestSynchronize.from_dict(webhook_pull_request_synchronize_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


