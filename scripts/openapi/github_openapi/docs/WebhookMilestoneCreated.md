# WebhookMilestoneCreated


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
from github_openapi.models.webhook_milestone_created import WebhookMilestoneCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMilestoneCreated from a JSON string
webhook_milestone_created_instance = WebhookMilestoneCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookMilestoneCreated.to_json())

# convert the object into a dict
webhook_milestone_created_dict = webhook_milestone_created_instance.to_dict()
# create an instance of WebhookMilestoneCreated from a dict
webhook_milestone_created_from_dict = WebhookMilestoneCreated.from_dict(webhook_milestone_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


