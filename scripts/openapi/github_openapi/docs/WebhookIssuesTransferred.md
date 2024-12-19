# WebhookIssuesTransferred


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookIssuesTransferredChanges**](WebhookIssuesTransferredChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**WebhooksIssue2**](WebhooksIssue2.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_transferred import WebhookIssuesTransferred

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesTransferred from a JSON string
webhook_issues_transferred_instance = WebhookIssuesTransferred.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesTransferred.to_json())

# convert the object into a dict
webhook_issues_transferred_dict = webhook_issues_transferred_instance.to_dict()
# create an instance of WebhookIssuesTransferred from a dict
webhook_issues_transferred_from_dict = WebhookIssuesTransferred.from_dict(webhook_issues_transferred_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


