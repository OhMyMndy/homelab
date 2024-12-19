# WebhookMilestoneOpened


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**milestone** | [**WebhooksMilestone3**](WebhooksMilestone3.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_milestone_opened import WebhookMilestoneOpened

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMilestoneOpened from a JSON string
webhook_milestone_opened_instance = WebhookMilestoneOpened.from_json(json)
# print the JSON string representation of the object
print(WebhookMilestoneOpened.to_json())

# convert the object into a dict
webhook_milestone_opened_dict = webhook_milestone_opened_instance.to_dict()
# create an instance of WebhookMilestoneOpened from a dict
webhook_milestone_opened_from_dict = WebhookMilestoneOpened.from_dict(webhook_milestone_opened_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


