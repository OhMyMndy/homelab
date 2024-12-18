# DeviceInviteAcceptedBy

Set when the invite has been accepted. It holds information about the user who accepted the share invite. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The ID of the user who accepted the share invite.  | [optional] 
**login_name** | **str** | The login name of the user who accepted the share invite.  | [optional] 
**profile_pic_url** | **str** | The profile pic URL for the user who accepted the share invite.  | [optional] 

## Example

```python
from tailscale_openapi.models.device_invite_accepted_by import DeviceInviteAcceptedBy

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInviteAcceptedBy from a JSON string
device_invite_accepted_by_instance = DeviceInviteAcceptedBy.from_json(json)
# print the JSON string representation of the object
print(DeviceInviteAcceptedBy.to_json())

# convert the object into a dict
device_invite_accepted_by_dict = device_invite_accepted_by_instance.to_dict()
# create an instance of DeviceInviteAcceptedBy from a dict
device_invite_accepted_by_from_dict = DeviceInviteAcceptedBy.from_dict(device_invite_accepted_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


