# TeamPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pull** | **bool** |  | 
**triage** | **bool** |  | 
**push** | **bool** |  | 
**maintain** | **bool** |  | 
**admin** | **bool** |  | 

## Example

```python
from github_openapi.models.team_permissions import TeamPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPermissions from a JSON string
team_permissions_instance = TeamPermissions.from_json(json)
# print the JSON string representation of the object
print(TeamPermissions.to_json())

# convert the object into a dict
team_permissions_dict = team_permissions_instance.to_dict()
# create an instance of TeamPermissions from a dict
team_permissions_from_dict = TeamPermissions.from_dict(team_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


