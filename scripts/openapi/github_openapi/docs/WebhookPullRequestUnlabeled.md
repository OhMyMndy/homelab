# WebhookPullRequestUnlabeled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**label** | [**WebhooksLabel**](WebhooksLabel.md) |  | [optional] 
**number** | **int** | The pull request number. | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest12**](PullRequest12.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_unlabeled import WebhookPullRequestUnlabeled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestUnlabeled from a JSON string
webhook_pull_request_unlabeled_instance = WebhookPullRequestUnlabeled.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestUnlabeled.to_json())

# convert the object into a dict
webhook_pull_request_unlabeled_dict = webhook_pull_request_unlabeled_instance.to_dict()
# create an instance of WebhookPullRequestUnlabeled from a dict
webhook_pull_request_unlabeled_from_dict = WebhookPullRequestUnlabeled.from_dict(webhook_pull_request_unlabeled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


