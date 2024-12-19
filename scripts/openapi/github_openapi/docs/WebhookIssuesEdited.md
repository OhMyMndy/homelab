# WebhookIssuesEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookIssuesEditedChanges**](WebhookIssuesEditedChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**Issue2**](Issue2.md) |  | 
**label** | [**WebhooksLabel**](WebhooksLabel.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_edited import WebhookIssuesEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesEdited from a JSON string
webhook_issues_edited_instance = WebhookIssuesEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesEdited.to_json())

# convert the object into a dict
webhook_issues_edited_dict = webhook_issues_edited_instance.to_dict()
# create an instance of WebhookIssuesEdited from a dict
webhook_issues_edited_from_dict = WebhookIssuesEdited.from_dict(webhook_issues_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


