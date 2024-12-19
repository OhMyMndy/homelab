# WebhookIssuesReopened


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**Issue8**](Issue8.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_reopened import WebhookIssuesReopened

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesReopened from a JSON string
webhook_issues_reopened_instance = WebhookIssuesReopened.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesReopened.to_json())

# convert the object into a dict
webhook_issues_reopened_dict = webhook_issues_reopened_instance.to_dict()
# create an instance of WebhookIssuesReopened from a dict
webhook_issues_reopened_from_dict = WebhookIssuesReopened.from_dict(webhook_issues_reopened_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


