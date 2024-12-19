# WebhookIssuesUnassigned


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action that was performed. | 
**assignee** | [**WebhooksUserMannequin**](WebhooksUserMannequin.md) |  | [optional] 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**WebhooksIssue**](WebhooksIssue.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_unassigned import WebhookIssuesUnassigned

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesUnassigned from a JSON string
webhook_issues_unassigned_instance = WebhookIssuesUnassigned.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesUnassigned.to_json())

# convert the object into a dict
webhook_issues_unassigned_dict = webhook_issues_unassigned_instance.to_dict()
# create an instance of WebhookIssuesUnassigned from a dict
webhook_issues_unassigned_from_dict = WebhookIssuesUnassigned.from_dict(webhook_issues_unassigned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


