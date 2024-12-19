# WebhookIssuesDemilestoned


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**Issue1**](Issue1.md) |  | 
**milestone** | [**WebhooksMilestone**](WebhooksMilestone.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_demilestoned import WebhookIssuesDemilestoned

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesDemilestoned from a JSON string
webhook_issues_demilestoned_instance = WebhookIssuesDemilestoned.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesDemilestoned.to_json())

# convert the object into a dict
webhook_issues_demilestoned_dict = webhook_issues_demilestoned_instance.to_dict()
# create an instance of WebhookIssuesDemilestoned from a dict
webhook_issues_demilestoned_from_dict = WebhookIssuesDemilestoned.from_dict(webhook_issues_demilestoned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


