# WebhookTeamRemovedFromRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**repository** | [**Repository15**](Repository15.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**team** | [**WebhooksTeam1**](WebhooksTeam1.md) |  | 

## Example

```python
from github_openapi.models.webhook_team_removed_from_repository import WebhookTeamRemovedFromRepository

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTeamRemovedFromRepository from a JSON string
webhook_team_removed_from_repository_instance = WebhookTeamRemovedFromRepository.from_json(json)
# print the JSON string representation of the object
print(WebhookTeamRemovedFromRepository.to_json())

# convert the object into a dict
webhook_team_removed_from_repository_dict = webhook_team_removed_from_repository_instance.to_dict()
# create an instance of WebhookTeamRemovedFromRepository from a dict
webhook_team_removed_from_repository_from_dict = WebhookTeamRemovedFromRepository.from_dict(webhook_team_removed_from_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


