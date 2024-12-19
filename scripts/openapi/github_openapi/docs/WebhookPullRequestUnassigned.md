# WebhookPullRequestUnassigned


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**assignee** | [**WebhooksUserMannequin**](WebhooksUserMannequin.md) |  | [optional] 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** | The pull request number. | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest11**](PullRequest11.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_pull_request_unassigned import WebhookPullRequestUnassigned

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestUnassigned from a JSON string
webhook_pull_request_unassigned_instance = WebhookPullRequestUnassigned.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestUnassigned.to_json())

# convert the object into a dict
webhook_pull_request_unassigned_dict = webhook_pull_request_unassigned_instance.to_dict()
# create an instance of WebhookPullRequestUnassigned from a dict
webhook_pull_request_unassigned_from_dict = WebhookPullRequestUnassigned.from_dict(webhook_pull_request_unassigned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


