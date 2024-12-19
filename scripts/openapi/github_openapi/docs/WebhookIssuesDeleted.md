# WebhookIssuesDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**Issue**](Issue.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_deleted import WebhookIssuesDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesDeleted from a JSON string
webhook_issues_deleted_instance = WebhookIssuesDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesDeleted.to_json())

# convert the object into a dict
webhook_issues_deleted_dict = webhook_issues_deleted_instance.to_dict()
# create an instance of WebhookIssuesDeleted from a dict
webhook_issues_deleted_from_dict = WebhookIssuesDeleted.from_dict(webhook_issues_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


