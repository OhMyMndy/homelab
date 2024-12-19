# WebhookIssuesUnlocked


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**Issue10**](Issue10.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_unlocked import WebhookIssuesUnlocked

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesUnlocked from a JSON string
webhook_issues_unlocked_instance = WebhookIssuesUnlocked.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesUnlocked.to_json())

# convert the object into a dict
webhook_issues_unlocked_dict = webhook_issues_unlocked_instance.to_dict()
# create an instance of WebhookIssuesUnlocked from a dict
webhook_issues_unlocked_from_dict = WebhookIssuesUnlocked.from_dict(webhook_issues_unlocked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


