# TeamProject

A team's access to a project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_url** | **str** |  | 
**url** | **str** |  | 
**html_url** | **str** |  | 
**columns_url** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**name** | **str** |  | 
**body** | **str** |  | 
**number** | **int** |  | 
**state** | **str** |  | 
**creator** | [**SimpleUser**](SimpleUser.md) |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**organization_permission** | **str** | The organization permission for this project. Only present when owner is an organization. | [optional] 
**private** | **bool** | Whether the project is private or not. Only present when owner is an organization. | [optional] 
**permissions** | [**TeamProjectPermissions**](TeamProjectPermissions.md) |  | 

## Example

```python
from github_openapi.models.team_project import TeamProject

# TODO update the JSON string below
json = "{}"
# create an instance of TeamProject from a JSON string
team_project_instance = TeamProject.from_json(json)
# print the JSON string representation of the object
print(TeamProject.to_json())

# convert the object into a dict
team_project_dict = team_project_instance.to_dict()
# create an instance of TeamProject from a dict
team_project_from_dict = TeamProject.from_dict(team_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


