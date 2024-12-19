# Team1

Groups of organization members that gives permissions on specified repositories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **bool** |  | [optional] 
**description** | **str** | Description of the team | 
**html_url** | **str** |  | 
**id** | **int** | Unique identifier of the team | 
**members_url** | **str** |  | 
**name** | **str** | Name of the team | 
**node_id** | **str** |  | 
**parent** | [**TeamParent**](TeamParent.md) |  | [optional] 
**permission** | **str** | Permission that the team will have for its repositories | 
**privacy** | **str** |  | 
**repositories_url** | **str** |  | 
**slug** | **str** |  | 
**url** | **str** | URL for the team | 

## Example

```python
from github_openapi.models.team1 import Team1

# TODO update the JSON string below
json = "{}"
# create an instance of Team1 from a JSON string
team1_instance = Team1.from_json(json)
# print the JSON string representation of the object
print(Team1.to_json())

# convert the object into a dict
team1_dict = team1_instance.to_dict()
# create an instance of Team1 from a dict
team1_from_dict = Team1.from_dict(team1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


