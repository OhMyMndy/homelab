# WebhookIssuesOpened


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookIssuesOpenedChanges**](WebhookIssuesOpenedChanges.md) |  | [optional] 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**Issue7**](Issue7.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_opened import WebhookIssuesOpened

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesOpened from a JSON string
webhook_issues_opened_instance = WebhookIssuesOpened.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesOpened.to_json())

# convert the object into a dict
webhook_issues_opened_dict = webhook_issues_opened_instance.to_dict()
# create an instance of WebhookIssuesOpened from a dict
webhook_issues_opened_from_dict = WebhookIssuesOpened.from_dict(webhook_issues_opened_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

