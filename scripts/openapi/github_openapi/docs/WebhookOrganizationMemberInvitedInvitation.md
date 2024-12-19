# WebhookOrganizationMemberInvitedInvitation

The invitation for the user or email if the action is `member_invited`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**email** | **str** |  | 
**failed_at** | **datetime** |  | 
**failed_reason** | **str** |  | 
**id** | **float** |  | 
**invitation_teams_url** | **str** |  | 
**inviter** | [**User2**](User2.md) |  | 
**login** | **str** |  | 
**node_id** | **str** |  | 
**role** | **str** |  | 
**team_count** | **float** |  | 
**invitation_source** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_organization_member_invited_invitation import WebhookOrganizationMemberInvitedInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOrganizationMemberInvitedInvitation from a JSON string
webhook_organization_member_invited_invitation_instance = WebhookOrganizationMemberInvitedInvitation.from_json(json)
# print the JSON string representation of the object
print(WebhookOrganizationMemberInvitedInvitation.to_json())

# convert the object into a dict
webhook_organization_member_invited_invitation_dict = webhook_organization_member_invited_invitation_instance.to_dict()
# create an instance of WebhookOrganizationMemberInvitedInvitation from a dict
webhook_organization_member_invited_invitation_from_dict = WebhookOrganizationMemberInvitedInvitation.from_dict(webhook_organization_member_invited_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


