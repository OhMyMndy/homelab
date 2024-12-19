# WebhookPullRequestDequeued


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest3**](PullRequest3.md) |  | 
**reason** | **str** |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_dequeued import WebhookPullRequestDequeued

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestDequeued from a JSON string
webhook_pull_request_dequeued_instance = WebhookPullRequestDequeued.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestDequeued.to_json())

# convert the object into a dict
webhook_pull_request_dequeued_dict = webhook_pull_request_dequeued_instance.to_dict()
# create an instance of WebhookPullRequestDequeued from a dict
webhook_pull_request_dequeued_from_dict = WebhookPullRequestDequeued.from_dict(webhook_pull_request_dequeued_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


