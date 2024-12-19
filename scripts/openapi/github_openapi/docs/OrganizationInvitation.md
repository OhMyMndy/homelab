# OrganizationInvitation

Organization Invitation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**login** | **str** |  | 
**email** | **str** |  | 
**role** | **str** |  | 
**created_at** | **str** |  | 
**failed_at** | **str** |  | [optional] 
**failed_reason** | **str** |  | [optional] 
**inviter** | [**SimpleUser**](SimpleUser.md) |  | 
**team_count** | **int** |  | 
**node_id** | **str** |  | 
**invitation_teams_url** | **str** |  | 
**invitation_source** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.organization_invitation import OrganizationInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationInvitation from a JSON string
organization_invitation_instance = OrganizationInvitation.from_json(json)
# print the JSON string representation of the object
print(OrganizationInvitation.to_json())

# convert the object into a dict
organization_invitation_dict = organization_invitation_instance.to_dict()
# create an instance of OrganizationInvitation from a dict
organization_invitation_from_dict = OrganizationInvitation.from_dict(organization_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


