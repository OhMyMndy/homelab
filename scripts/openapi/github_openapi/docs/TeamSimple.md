# TeamSimple

Groups of organization members that gives permissions on specified repositories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the team | 
**node_id** | **str** |  | 
**url** | **str** | URL for the team | 
**members_url** | **str** |  | 
**name** | **str** | Name of the team | 
**description** | **str** | Description of the team | 
**permission** | **str** | Permission that the team will have for its repositories | 
**privacy** | **str** | The level of privacy this team should have | [optional] 
**notification_setting** | **str** | The notification setting the team has set | [optional] 
**html_url** | **str** |  | 
**repositories_url** | **str** |  | 
**slug** | **str** |  | 
**ldap_dn** | **str** | Distinguished Name (DN) that team maps to within LDAP environment | [optional] 

## Example

```python
from github_openapi.models.team_simple import TeamSimple

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSimple from a JSON string
team_simple_instance = TeamSimple.from_json(json)
# print the JSON string representation of the object
print(TeamSimple.to_json())

# convert the object into a dict
team_simple_dict = team_simple_instance.to_dict()
# create an instance of TeamSimple from a dict
team_simple_from_dict = TeamSimple.from_dict(team_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


