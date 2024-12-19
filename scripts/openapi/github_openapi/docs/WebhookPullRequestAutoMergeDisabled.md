# WebhookPullRequestAutoMergeDisabled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest1**](PullRequest1.md) |  | 
**reason** | **str** |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_auto_merge_disabled import WebhookPullRequestAutoMergeDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestAutoMergeDisabled from a JSON string
webhook_pull_request_auto_merge_disabled_instance = WebhookPullRequestAutoMergeDisabled.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestAutoMergeDisabled.to_json())

# convert the object into a dict
webhook_pull_request_auto_merge_disabled_dict = webhook_pull_request_auto_merge_disabled_instance.to_dict()
# create an instance of WebhookPullRequestAutoMergeDisabled from a dict
webhook_pull_request_auto_merge_disabled_from_dict = WebhookPullRequestAutoMergeDisabled.from_dict(webhook_pull_request_auto_merge_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


