# TeamRoleAssignment

The Relationship a Team has with a role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment** | **str** | Determines if the team has a direct, indirect, or mixed relationship to a role | [optional] 
**id** | **int** |  | 
**node_id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**description** | **str** |  | 
**privacy** | **str** |  | [optional] 
**notification_setting** | **str** |  | [optional] 
**permission** | **str** |  | 
**permissions** | [**TeamPermissions**](TeamPermissions.md) |  | [optional] 
**url** | **str** |  | 
**html_url** | **str** |  | 
**members_url** | **str** |  | 
**repositories_url** | **str** |  | 
**parent** | [**NullableTeamSimple**](NullableTeamSimple.md) |  | 

## Example

```python
from github_openapi.models.team_role_assignment import TeamRoleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRoleAssignment from a JSON string
team_role_assignment_instance = TeamRoleAssignment.from_json(json)
# print the JSON string representation of the object
print(TeamRoleAssignment.to_json())

# convert the object into a dict
team_role_assignment_dict = team_role_assignment_instance.to_dict()
# create an instance of TeamRoleAssignment from a dict
team_role_assignment_from_dict = TeamRoleAssignment.from_dict(team_role_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


