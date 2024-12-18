# UserInvite

A user invite is an active invitation that lets a user join a tailnet with a preassigned [user role](https://tailscale.com/kb/1138/user-roles).  Each user invite has a unique ID that is used to identify the invite in API calls. You can find all user invite IDs for a particular tailnet by [listing user invites](#tag/userinvites/get/tailnet/{tailnet}/user-invites). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the invite. Supply this value wherever &#x60;userInviteId&#x60; is indicated in the endpoint.  | 
**role** | **str** | The tailnet user role to assign to the invited user upon accepting the invite.  | 
**tailnet_id** | **float** | The ID of the tailnet to which the user was invited.  | 
**inviter_id** | **float** | The ID of the user who created the invite.  | 
**email** | **str** | The email to which the invite was sent. If empty, the invite was not emailed to anyone, but the inviteUrl can be shared manually.  | [optional] 
**last_email_sent_at** | **datetime** | The last time the invite was attempted to be sent to Email. Only ever set if &#x60;email&#x60; is not empty.  | [optional] 
**invite_url** | **str** | Included when &#x60;email&#x60; is not part of the tailnet&#39;s domain, or when &#x60;email&#x60; is empty. It is the link to accept the invite.  When included, anyone with this link can accept the invite. It is not restricted to the person to which the invite was emailed.  When &#x60;email&#x60; is part of the tailnet&#39;s domain (has the same @domain.com suffix as the tailnet), the user can join the tailnet automatically by logging in with their domain email at https://login.tailscale.com/start. They&#39;ll be assigned the specified &#x60;role&#x60; upon signing in for the first time.  | [optional] 

## Example

```python
from tailscale_openapi.models.user_invite import UserInvite

# TODO update the JSON string below
json = "{}"
# create an instance of UserInvite from a JSON string
user_invite_instance = UserInvite.from_json(json)
# print the JSON string representation of the object
print(UserInvite.to_json())

# convert the object into a dict
user_invite_dict = user_invite_instance.to_dict()
# create an instance of UserInvite from a dict
user_invite_from_dict = UserInvite.from_dict(user_invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


