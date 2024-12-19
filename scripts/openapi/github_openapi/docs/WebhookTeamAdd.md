# WebhookTeamAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**team** | [**WebhooksTeam1**](WebhooksTeam1.md) |  | 

## Example

```python
from github_openapi.models.webhook_team_add import WebhookTeamAdd

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTeamAdd from a JSON string
webhook_team_add_instance = WebhookTeamAdd.from_json(json)
# print the JSON string representation of the object
print(WebhookTeamAdd.to_json())

# convert the object into a dict
webhook_team_add_dict = webhook_team_add_instance.to_dict()
# create an instance of WebhookTeamAdd from a dict
webhook_team_add_from_dict = WebhookTeamAdd.from_dict(webhook_team_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


