# AcceptDeviceInvite200ResponseAcceptedBy

The user accepting the device share invite. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the user who accepted the share invite.  | [optional] 
**display_name** | **str** | The display name of the user who accepted the share invite.  | [optional] 
**login_name** | **str** | The email address of the user who accepted the share invite.  | [optional] 
**profile_pic_url** | **str** | The profile pic URL for the user who accepted the share invite.  | [optional] 

## Example

```python
from tailscale_openapi.models.accept_device_invite200_response_accepted_by import AcceptDeviceInvite200ResponseAcceptedBy

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptDeviceInvite200ResponseAcceptedBy from a JSON string
accept_device_invite200_response_accepted_by_instance = AcceptDeviceInvite200ResponseAcceptedBy.from_json(json)
# print the JSON string representation of the object
print(AcceptDeviceInvite200ResponseAcceptedBy.to_json())

# convert the object into a dict
accept_device_invite200_response_accepted_by_dict = accept_device_invite200_response_accepted_by_instance.to_dict()
# create an instance of AcceptDeviceInvite200ResponseAcceptedBy from a dict
accept_device_invite200_response_accepted_by_from_dict = AcceptDeviceInvite200ResponseAcceptedBy.from_dict(accept_device_invite200_response_accepted_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


