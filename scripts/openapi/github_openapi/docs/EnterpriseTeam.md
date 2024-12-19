# EnterpriseTeam

Group of enterprise owners and/or members

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**url** | **str** |  | 
**sync_to_organizations** | **str** |  | 
**group_id** | **str** |  | [optional] 
**html_url** | **str** |  | 
**members_url** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.enterprise_team import EnterpriseTeam

# TODO update the JSON string below
json = "{}"
# create an instance of EnterpriseTeam from a JSON string
enterprise_team_instance = EnterpriseTeam.from_json(json)
# print the JSON string representation of the object
print(EnterpriseTeam.to_json())

# convert the object into a dict
enterprise_team_dict = enterprise_team_instance.to_dict()
# create an instance of EnterpriseTeam from a dict
enterprise_team_from_dict = EnterpriseTeam.from_dict(enterprise_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


