# WebhookPullRequestEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookPullRequestEditedChanges**](WebhookPullRequestEditedChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**number** | **int** | The pull request number. | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pull_request** | [**PullRequestWebhook**](PullRequestWebhook.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_pull_request_edited import WebhookPullRequestEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestEdited from a JSON string
webhook_pull_request_edited_instance = WebhookPullRequestEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestEdited.to_json())

# convert the object into a dict
webhook_pull_request_edited_dict = webhook_pull_request_edited_instance.to_dict()
# create an instance of WebhookPullRequestEdited from a dict
webhook_pull_request_edited_from_dict = WebhookPullRequestEdited.from_dict(webhook_pull_request_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


