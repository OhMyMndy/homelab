# UserRoleAssignment

The Relationship a User has with a role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment** | **str** | Determines if the user has a direct, indirect, or mixed relationship to a role | [optional] 
**inherited_from** | [**List[TeamSimple]**](TeamSimple.md) | Team the user has gotten the role through | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**login** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**avatar_url** | **str** |  | 
**gravatar_id** | **str** |  | 
**url** | **str** |  | 
**html_url** | **str** |  | 
**followers_url** | **str** |  | 
**following_url** | **str** |  | 
**gists_url** | **str** |  | 
**starred_url** | **str** |  | 
**subscriptions_url** | **str** |  | 
**organizations_url** | **str** |  | 
**repos_url** | **str** |  | 
**events_url** | **str** |  | 
**received_events_url** | **str** |  | 
**type** | **str** |  | 
**site_admin** | **bool** |  | 
**starred_at** | **str** |  | [optional] 
**user_view_type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.user_role_assignment import UserRoleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoleAssignment from a JSON string
user_role_assignment_instance = UserRoleAssignment.from_json(json)
# print the JSON string representation of the object
print(UserRoleAssignment.to_json())

# convert the object into a dict
user_role_assignment_dict = user_role_assignment_instance.to_dict()
# create an instance of UserRoleAssignment from a dict
user_role_assignment_from_dict = UserRoleAssignment.from_dict(user_role_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


