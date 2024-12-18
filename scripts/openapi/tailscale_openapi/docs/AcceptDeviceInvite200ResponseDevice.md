# AcceptDeviceInvite200ResponseDevice

Information about the device being shared. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &#x60;nodeId&#x60; for the device.  | [optional] 
**os** | **str** | The operating system that the device is running.  | [optional] 
**name** | **str** | The name of the device.  | [optional] 
**fqdn** | **str** | The MagicDNS name of the device. Learn more about MagicDNS at https://tailscale.com/kb/1081/.  | [optional] 
**ipv4** | **str** | The IPv4 address of the device.  | [optional] 
**ipv6** | **str** | The IPv6 address of the device.  | [optional] 
**include_exit_node** | **bool** | Specifies whether the invited user is able to use the device as an exit node when the device is advertising as one.  | [optional] 

## Example

```python
from tailscale_openapi.models.accept_device_invite200_response_device import AcceptDeviceInvite200ResponseDevice

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptDeviceInvite200ResponseDevice from a JSON string
accept_device_invite200_response_device_instance = AcceptDeviceInvite200ResponseDevice.from_json(json)
# print the JSON string representation of the object
print(AcceptDeviceInvite200ResponseDevice.to_json())

# convert the object into a dict
accept_device_invite200_response_device_dict = accept_device_invite200_response_device_instance.to_dict()
# create an instance of AcceptDeviceInvite200ResponseDevice from a dict
accept_device_invite200_response_device_from_dict = AcceptDeviceInvite200ResponseDevice.from_dict(accept_device_invite200_response_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


