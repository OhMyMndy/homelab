# TeamProjectPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | **bool** |  | 
**write** | **bool** |  | 
**admin** | **bool** |  | 

## Example

```python
from github_openapi.models.team_project_permissions import TeamProjectPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of TeamProjectPermissions from a JSON string
team_project_permissions_instance = TeamProjectPermissions.from_json(json)
# print the JSON string representation of the object
print(TeamProjectPermissions.to_json())

# convert the object into a dict
team_project_permissions_dict = team_project_permissions_instance.to_dict()
# create an instance of TeamProjectPermissions from a dict
team_project_permissions_from_dict = TeamProjectPermissions.from_dict(team_project_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


