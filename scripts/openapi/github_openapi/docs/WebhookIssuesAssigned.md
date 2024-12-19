# WebhookIssuesAssigned


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action that was performed. | 
**assignee** | [**WebhooksUser**](WebhooksUser.md) |  | [optional] 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**WebhooksIssue**](WebhooksIssue.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_assigned import WebhookIssuesAssigned

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesAssigned from a JSON string
webhook_issues_assigned_instance = WebhookIssuesAssigned.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesAssigned.to_json())

# convert the object into a dict
webhook_issues_assigned_dict = webhook_issues_assigned_instance.to_dict()
# create an instance of WebhookIssuesAssigned from a dict
webhook_issues_assigned_from_dict = WebhookIssuesAssigned.from_dict(webhook_issues_assigned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


