# CreateDeviceInvitesRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multi_use** | **bool** | Whether the invite can be accepted more than once. When set to &#x60;true&#x60;, it results in an invite that can be accepted up to 1,000 times.  | [optional] 
**allow_exit_node** | **bool** | Whether the invited user can use the device as an exit node when it advertises as one.  | [optional] 
**email** | **str** | The email to send the created invite to. If not set, the endpoint generates and returns an invite URL (but doesn&#39;t send it out).  | [optional] 

## Example

```python
from tailscale_openapi.models.create_device_invites_request_inner import CreateDeviceInvitesRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeviceInvitesRequestInner from a JSON string
create_device_invites_request_inner_instance = CreateDeviceInvitesRequestInner.from_json(json)
# print the JSON string representation of the object
print(CreateDeviceInvitesRequestInner.to_json())

# convert the object into a dict
create_device_invites_request_inner_dict = create_device_invites_request_inner_instance.to_dict()
# create an instance of CreateDeviceInvitesRequestInner from a dict
create_device_invites_request_inner_from_dict = CreateDeviceInvitesRequestInner.from_dict(create_device_invites_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


