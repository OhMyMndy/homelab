# CreateUserInvitesRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Optionally specifies a user role to assign the invited user.  | [optional] [default to 'member']
**email** | **str** | Optionally specifies the email to send the created invite. If not set, the endpoint generates and returns an invite URL, but does not email it out.  | [optional] 

## Example

```python
from tailscale_openapi.models.create_user_invites_request_inner import CreateUserInvitesRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserInvitesRequestInner from a JSON string
create_user_invites_request_inner_instance = CreateUserInvitesRequestInner.from_json(json)
# print the JSON string representation of the object
print(CreateUserInvitesRequestInner.to_json())

# convert the object into a dict
create_user_invites_request_inner_dict = create_user_invites_request_inner_instance.to_dict()
# create an instance of CreateUserInvitesRequestInner from a dict
create_user_invites_request_inner_from_dict = CreateUserInvitesRequestInner.from_dict(create_user_invites_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


