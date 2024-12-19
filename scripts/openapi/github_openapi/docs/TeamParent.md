# TeamParent


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
**repositories_url** | **str** |  | 
**slug** | **str** |  | 
**url** | **str** | URL for the team | 

## Example

```python
from github_openapi.models.team_parent import TeamParent

# TODO update the JSON string below
json = "{}"
# create an instance of TeamParent from a JSON string
team_parent_instance = TeamParent.from_json(json)
# print the JSON string representation of the object
print(TeamParent.to_json())

# convert the object into a dict
team_parent_dict = team_parent_instance.to_dict()
# create an instance of TeamParent from a dict
team_parent_from_dict = TeamParent.from_dict(team_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

