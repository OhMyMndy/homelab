# AcceptDeviceInvite200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**AcceptDeviceInvite200ResponseDevice**](AcceptDeviceInvite200ResponseDevice.md) |  | [optional] 
**sharer** | [**AcceptDeviceInvite200ResponseSharer**](AcceptDeviceInvite200ResponseSharer.md) |  | [optional] 
**accepted_by** | [**AcceptDeviceInvite200ResponseAcceptedBy**](AcceptDeviceInvite200ResponseAcceptedBy.md) |  | [optional] 

## Example

```python
from tailscale_openapi.models.accept_device_invite200_response import AcceptDeviceInvite200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptDeviceInvite200Response from a JSON string
accept_device_invite200_response_instance = AcceptDeviceInvite200Response.from_json(json)
# print the JSON string representation of the object
print(AcceptDeviceInvite200Response.to_json())

# convert the object into a dict
accept_device_invite200_response_dict = accept_device_invite200_response_instance.to_dict()
# create an instance of AcceptDeviceInvite200Response from a dict
accept_device_invite200_response_from_dict = AcceptDeviceInvite200Response.from_dict(accept_device_invite200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


