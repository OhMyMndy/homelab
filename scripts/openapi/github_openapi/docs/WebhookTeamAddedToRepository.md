# WebhookTeamAddedToRepository


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
from github_openapi.models.webhook_team_added_to_repository import WebhookTeamAddedToRepository

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTeamAddedToRepository from a JSON string
webhook_team_added_to_repository_instance = WebhookTeamAddedToRepository.from_json(json)
# print the JSON string representation of the object
print(WebhookTeamAddedToRepository.to_json())

# convert the object into a dict
webhook_team_added_to_repository_dict = webhook_team_added_to_repository_instance.to_dict()
# create an instance of WebhookTeamAddedToRepository from a dict
webhook_team_added_to_repository_from_dict = WebhookTeamAddedToRepository.from_dict(webhook_team_added_to_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


