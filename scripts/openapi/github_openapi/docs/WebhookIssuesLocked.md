# WebhookIssuesLocked


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**Issue4**](Issue4.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_locked import WebhookIssuesLocked

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesLocked from a JSON string
webhook_issues_locked_instance = WebhookIssuesLocked.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesLocked.to_json())

# convert the object into a dict
webhook_issues_locked_dict = webhook_issues_locked_instance.to_dict()
# create an instance of WebhookIssuesLocked from a dict
webhook_issues_locked_from_dict = WebhookIssuesLocked.from_dict(webhook_issues_locked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


