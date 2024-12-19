# WebhookMilestoneDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**milestone** | [**WebhooksMilestone**](WebhooksMilestone.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_milestone_deleted import WebhookMilestoneDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMilestoneDeleted from a JSON string
webhook_milestone_deleted_instance = WebhookMilestoneDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookMilestoneDeleted.to_json())

# convert the object into a dict
webhook_milestone_deleted_dict = webhook_milestone_deleted_instance.to_dict()
# create an instance of WebhookMilestoneDeleted from a dict
webhook_milestone_deleted_from_dict = WebhookMilestoneDeleted.from_dict(webhook_milestone_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


