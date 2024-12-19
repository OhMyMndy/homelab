# WebhookIssuesUnlabeled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**WebhooksIssue**](WebhooksIssue.md) |  | 
**label** | [**WebhooksLabel**](WebhooksLabel.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_unlabeled import WebhookIssuesUnlabeled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesUnlabeled from a JSON string
webhook_issues_unlabeled_instance = WebhookIssuesUnlabeled.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesUnlabeled.to_json())

# convert the object into a dict
webhook_issues_unlabeled_dict = webhook_issues_unlabeled_instance.to_dict()
# create an instance of WebhookIssuesUnlabeled from a dict
webhook_issues_unlabeled_from_dict = WebhookIssuesUnlabeled.from_dict(webhook_issues_unlabeled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


