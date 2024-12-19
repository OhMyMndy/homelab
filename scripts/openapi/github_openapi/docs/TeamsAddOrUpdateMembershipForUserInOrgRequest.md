# TeamsAddOrUpdateMembershipForUserInOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role that this user should have in the team. | [optional] [default to 'member']

## Example

```python
from github_openapi.models.teams_add_or_update_membership_for_user_in_org_request import TeamsAddOrUpdateMembershipForUserInOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsAddOrUpdateMembershipForUserInOrgRequest from a JSON string
teams_add_or_update_membership_for_user_in_org_request_instance = TeamsAddOrUpdateMembershipForUserInOrgRequest.from_json(json)
# print the JSON string representation of the object
print(TeamsAddOrUpdateMembershipForUserInOrgRequest.to_json())

# convert the object into a dict
teams_add_or_update_membership_for_user_in_org_request_dict = teams_add_or_update_membership_for_user_in_org_request_instance.to_dict()
# create an instance of TeamsAddOrUpdateMembershipForUserInOrgRequest from a dict
teams_add_or_update_membership_for_user_in_org_request_from_dict = TeamsAddOrUpdateMembershipForUserInOrgRequest.from_dict(teams_add_or_update_membership_for_user_in_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


