# WebhooksTeam

Groups of organization members that gives permissions on specified repositories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **bool** |  | [optional] 
**description** | **str** | Description of the team | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** | Unique identifier of the team | 
**members_url** | **str** |  | [optional] 
**name** | **str** | Name of the team | 
**node_id** | **str** |  | [optional] 
**parent** | [**WebhooksTeamParent**](WebhooksTeamParent.md) |  | [optional] 
**permission** | **str** | Permission that the team will have for its repositories | [optional] 
**privacy** | **str** |  | [optional] 
**notification_setting** | **str** |  | [optional] 
**repositories_url** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**url** | **str** | URL for the team | [optional] 

## Example

```python
from github_openapi.models.webhooks_team import WebhooksTeam

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksTeam from a JSON string
webhooks_team_instance = WebhooksTeam.from_json(json)
# print the JSON string representation of the object
print(WebhooksTeam.to_json())

# convert the object into a dict
webhooks_team_dict = webhooks_team_instance.to_dict()
# create an instance of WebhooksTeam from a dict
webhooks_team_from_dict = WebhooksTeam.from_dict(webhooks_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


