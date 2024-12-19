# WebhookIssuesMilestoned


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**Issue5**](Issue5.md) |  | 
**milestone** | [**WebhooksMilestone**](WebhooksMilestone.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_milestoned import WebhookIssuesMilestoned

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesMilestoned from a JSON string
webhook_issues_milestoned_instance = WebhookIssuesMilestoned.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesMilestoned.to_json())

# convert the object into a dict
webhook_issues_milestoned_dict = webhook_issues_milestoned_instance.to_dict()
# create an instance of WebhookIssuesMilestoned from a dict
webhook_issues_milestoned_from_dict = WebhookIssuesMilestoned.from_dict(webhook_issues_milestoned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


