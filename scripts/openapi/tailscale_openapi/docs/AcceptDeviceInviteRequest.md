# AcceptDeviceInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invite** | **str** | The URL of the invite (in the form &#x60;https://login.tailscale.com/admin/invite/{code}&#x60;) or the &#x60;{code}&#x60; component of the URL.  | 

## Example

```python
from tailscale_openapi.models.accept_device_invite_request import AcceptDeviceInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptDeviceInviteRequest from a JSON string
accept_device_invite_request_instance = AcceptDeviceInviteRequest.from_json(json)
# print the JSON string representation of the object
print(AcceptDeviceInviteRequest.to_json())

# convert the object into a dict
accept_device_invite_request_dict = accept_device_invite_request_instance.to_dict()
# create an instance of AcceptDeviceInviteRequest from a dict
accept_device_invite_request_from_dict = AcceptDeviceInviteRequest.from_dict(accept_device_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


