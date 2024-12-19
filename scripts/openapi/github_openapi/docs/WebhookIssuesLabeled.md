# WebhookIssuesLabeled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**Issue3**](Issue3.md) |  | 
**label** | [**WebhooksLabel**](WebhooksLabel.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_labeled import WebhookIssuesLabeled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesLabeled from a JSON string
webhook_issues_labeled_instance = WebhookIssuesLabeled.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesLabeled.to_json())

# convert the object into a dict
webhook_issues_labeled_dict = webhook_issues_labeled_instance.to_dict()
# create an instance of WebhookIssuesLabeled from a dict
webhook_issues_labeled_from_dict = WebhookIssuesLabeled.from_dict(webhook_issues_labeled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


