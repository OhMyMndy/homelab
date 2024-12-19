# TeamMembership

Team Membership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**role** | **str** | The role of the user in the team. | [default to 'member']
**state** | **str** | The state of the user&#39;s membership in the team. | 

## Example

```python
from github_openapi.models.team_membership import TeamMembership

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMembership from a JSON string
team_membership_instance = TeamMembership.from_json(json)
# print the JSON string representation of the object
print(TeamMembership.to_json())

# convert the object into a dict
team_membership_dict = team_membership_instance.to_dict()
# create an instance of TeamMembership from a dict
team_membership_from_dict = TeamMembership.from_dict(team_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


