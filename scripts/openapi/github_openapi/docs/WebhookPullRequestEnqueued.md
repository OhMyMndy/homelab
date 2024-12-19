# WebhookPullRequestEnqueued


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest3**](PullRequest3.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_enqueued import WebhookPullRequestEnqueued

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestEnqueued from a JSON string
webhook_pull_request_enqueued_instance = WebhookPullRequestEnqueued.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestEnqueued.to_json())

# convert the object into a dict
webhook_pull_request_enqueued_dict = webhook_pull_request_enqueued_instance.to_dict()
# create an instance of WebhookPullRequestEnqueued from a dict
webhook_pull_request_enqueued_from_dict = WebhookPullRequestEnqueued.from_dict(webhook_pull_request_enqueued_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


