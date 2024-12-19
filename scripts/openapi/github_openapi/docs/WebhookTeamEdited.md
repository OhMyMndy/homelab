# WebhookTeamEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookTeamEditedChanges**](WebhookTeamEditedChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**repository** | [**Repository15**](Repository15.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**team** | [**WebhooksTeam1**](WebhooksTeam1.md) |  | 

## Example

```python
from github_openapi.models.webhook_team_edited import WebhookTeamEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTeamEdited from a JSON string
webhook_team_edited_instance = WebhookTeamEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookTeamEdited.to_json())

# convert the object into a dict
webhook_team_edited_dict = webhook_team_edited_instance.to_dict()
# create an instance of WebhookTeamEdited from a dict
webhook_team_edited_from_dict = WebhookTeamEdited.from_dict(webhook_team_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


