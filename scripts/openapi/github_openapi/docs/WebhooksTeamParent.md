# WebhooksTeamParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the team | 
**html_url** | **str** |  | 
**id** | **int** | Unique identifier of the team | 
**members_url** | **str** |  | 
**name** | **str** | Name of the team | 
**node_id** | **str** |  | 
**permission** | **str** | Permission that the team will have for its repositories | 
**privacy** | **str** |  | 
**notification_setting** | **str** | Whether team members will receive notifications when their team is @mentioned | 
**repositories_url** | **str** |  | 
**slug** | **str** |  | 
**url** | **str** | URL for the team | 

## Example

```python
from github_openapi.models.webhooks_team_parent import WebhooksTeamParent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksTeamParent from a JSON string
webhooks_team_parent_instance = WebhooksTeamParent.from_json(json)
# print the JSON string representation of the object
print(WebhooksTeamParent.to_json())

# convert the object into a dict
webhooks_team_parent_dict = webhooks_team_parent_instance.to_dict()
# create an instance of WebhooksTeamParent from a dict
webhooks_team_parent_from_dict = WebhooksTeamParent.from_dict(webhooks_team_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


