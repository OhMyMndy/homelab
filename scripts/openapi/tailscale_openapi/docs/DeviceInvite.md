# DeviceInvite

A device invite is an invitation that shares a device with an external user (a user not in the device's tailnet).  Each device invite has a unique ID that is used to identify the invite in API calls. You can find all device invite IDs for a particular device by [listing all device invites](#tag/deviceinvites/POST/device/{deviceId}/device-invites) for a device. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the invite. Supply this value wherever {deviceInviteId} is indicated in the endpoint.  | [optional] 
**created** | **datetime** | The creation time of the invite.  | [optional] 
**tailnet_id** | **float** | The ID of the tailnet to which the shared device belongs.  | [optional] 
**device_id** | **float** | The ID of the device being shared.  | [optional] 
**sharer_id** | **float** | The ID of the user who created the share invite.  | [optional] 
**multi_use** | **bool** | Specifies whether this device invite can be accepted more than once.  | [optional] 
**allow_exit_node** | **bool** | Specifies whether the invited user is able to use the device as an exit node when the device is advertising as one.  | [optional] 
**email** | **str** | The email to which the invite was sent. If empty, the invite was not emailed to anyone, but the inviteUrl can be shared manually.  | [optional] 
**last_email_sent_at** | **datetime** | The last time the invite was attempted to be sent to Email. Only ever set if &#x60;email&#x60; is not empty.  | [optional] 
**invite_url** | **str** | The link to accept the invite. Anyone with this link can accept the invite. It is not restricted to the person to which the invite was emailed.  | [optional] 
**accepted** | **bool** | &#x60;true&#x60; when the share invite has been accepted.  | [optional] 
**accepted_by** | [**DeviceInviteAcceptedBy**](DeviceInviteAcceptedBy.md) |  | [optional] 

## Example

```python
from tailscale_openapi.models.device_invite import DeviceInvite

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceInvite from a JSON string
device_invite_instance = DeviceInvite.from_json(json)
# print the JSON string representation of the object
print(DeviceInvite.to_json())

# convert the object into a dict
device_invite_dict = device_invite_instance.to_dict()
# create an instance of DeviceInvite from a dict
device_invite_from_dict = DeviceInvite.from_dict(device_invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


