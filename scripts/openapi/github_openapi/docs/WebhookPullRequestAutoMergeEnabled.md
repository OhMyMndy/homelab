# WebhookPullRequestAutoMergeEnabled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequest2**](PullRequest2.md) |  | 
**reason** | **str** |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_auto_merge_enabled import WebhookPullRequestAutoMergeEnabled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestAutoMergeEnabled from a JSON string
webhook_pull_request_auto_merge_enabled_instance = WebhookPullRequestAutoMergeEnabled.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestAutoMergeEnabled.to_json())

# convert the object into a dict
webhook_pull_request_auto_merge_enabled_dict = webhook_pull_request_auto_merge_enabled_instance.to_dict()
# create an instance of WebhookPullRequestAutoMergeEnabled from a dict
webhook_pull_request_auto_merge_enabled_from_dict = WebhookPullRequestAutoMergeEnabled.from_dict(webhook_pull_request_auto_merge_enabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


