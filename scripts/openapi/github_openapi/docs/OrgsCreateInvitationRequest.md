# OrgsCreateInvitationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitee_id** | **int** | **Required unless you provide &#x60;email&#x60;**. GitHub user ID for the person you are inviting. | [optional] 
**email** | **str** | **Required unless you provide &#x60;invitee_id&#x60;**. Email address of the person you are inviting, which can be an existing GitHub user. | [optional] 
**role** | **str** | The role for the new member.   * &#x60;admin&#x60; - Organization owners with full administrative rights to the organization and complete access to all repositories and teams.    * &#x60;direct_member&#x60; - Non-owner organization members with ability to see other members and join teams by invitation.    * &#x60;billing_manager&#x60; - Non-owner organization members with ability to manage the billing settings of your organization.   * &#x60;reinstate&#x60; - The previous role assigned to the invitee before they were removed from your organization. Can be one of the roles listed above. Only works if the invitee was previously part of your organization. | [optional] [default to 'direct_member']
**team_ids** | **List[int]** | Specify IDs for the teams you want to invite new members to. | [optional] 

## Example

```python
from github_openapi.models.orgs_create_invitation_request import OrgsCreateInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgsCreateInvitationRequest from a JSON string
orgs_create_invitation_request_instance = OrgsCreateInvitationRequest.from_json(json)
# print the JSON string representation of the object
print(OrgsCreateInvitationRequest.to_json())

# convert the object into a dict
orgs_create_invitation_request_dict = orgs_create_invitation_request_instance.to_dict()
# create an instance of OrgsCreateInvitationRequest from a dict
orgs_create_invitation_request_from_dict = OrgsCreateInvitationRequest.from_dict(orgs_create_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


