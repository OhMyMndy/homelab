# Team

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
**parent** | [**TeamParent**](TeamParent.md) |  | [optional] 
**permission** | **str** | Permission that the team will have for its repositories | [optional] 
**privacy** | **str** |  | [optional] 
**repositories_url** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**url** | **str** | URL for the team | [optional] 

## Example

```python
from github_openapi.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print(Team.to_json())

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_from_dict = Team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


