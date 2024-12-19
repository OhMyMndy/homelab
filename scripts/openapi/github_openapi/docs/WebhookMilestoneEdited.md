# WebhookMilestoneEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookMilestoneEditedChanges**](WebhookMilestoneEditedChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**milestone** | [**WebhooksMilestone**](WebhooksMilestone.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_milestone_edited import WebhookMilestoneEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMilestoneEdited from a JSON string
webhook_milestone_edited_instance = WebhookMilestoneEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookMilestoneEdited.to_json())

# convert the object into a dict
webhook_milestone_edited_dict = webhook_milestone_edited_instance.to_dict()
# create an instance of WebhookMilestoneEdited from a dict
webhook_milestone_edited_from_dict = WebhookMilestoneEdited.from_dict(webhook_milestone_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


