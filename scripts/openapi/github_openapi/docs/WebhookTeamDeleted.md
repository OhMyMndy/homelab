# WebhookTeamDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**repository** | [**Repository15**](Repository15.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**team** | [**WebhooksTeam1**](WebhooksTeam1.md) |  | 

## Example

```python
from github_openapi.models.webhook_team_deleted import WebhookTeamDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTeamDeleted from a JSON string
webhook_team_deleted_instance = WebhookTeamDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookTeamDeleted.to_json())

# convert the object into a dict
webhook_team_deleted_dict = webhook_team_deleted_instance.to_dict()
# create an instance of WebhookTeamDeleted from a dict
webhook_team_deleted_from_dict = WebhookTeamDeleted.from_dict(webhook_team_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


