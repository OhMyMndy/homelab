# TeamFull

Groups of organization members that gives permissions on specified repositories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the team | 
**node_id** | **str** |  | 
**url** | **str** | URL for the team | 
**html_url** | **str** |  | 
**name** | **str** | Name of the team | 
**slug** | **str** |  | 
**description** | **str** |  | 
**privacy** | **str** | The level of privacy this team should have | [optional] 
**notification_setting** | **str** | The notification setting the team has set | [optional] 
**permission** | **str** | Permission that the team will have for its repositories | 
**members_url** | **str** |  | 
**repositories_url** | **str** |  | 
**parent** | [**NullableTeamSimple**](NullableTeamSimple.md) |  | [optional] 
**members_count** | **int** |  | 
**repos_count** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**organization** | [**TeamOrganization**](TeamOrganization.md) |  | 
**ldap_dn** | **str** | Distinguished Name (DN) that team maps to within LDAP environment | [optional] 

## Example

```python
from github_openapi.models.team_full import TeamFull

# TODO update the JSON string below
json = "{}"
# create an instance of TeamFull from a JSON string
team_full_instance = TeamFull.from_json(json)
# print the JSON string representation of the object
print(TeamFull.to_json())

# convert the object into a dict
team_full_dict = team_full_instance.to_dict()
# create an instance of TeamFull from a dict
team_full_from_dict = TeamFull.from_dict(team_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


