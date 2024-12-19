# WebhookIssuesClosed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action that was performed. | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**WebhookIssuesClosedIssue**](WebhookIssuesClosedIssue.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_closed import WebhookIssuesClosed

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesClosed from a JSON string
webhook_issues_closed_instance = WebhookIssuesClosed.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesClosed.to_json())

# convert the object into a dict
webhook_issues_closed_dict = webhook_issues_closed_instance.to_dict()
# create an instance of WebhookIssuesClosed from a dict
webhook_issues_closed_from_dict = WebhookIssuesClosed.from_dict(webhook_issues_closed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


