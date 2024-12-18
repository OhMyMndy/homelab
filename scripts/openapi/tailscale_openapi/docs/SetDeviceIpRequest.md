# SetDeviceIpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | **str** | The new IPv4 address for the device.  | 

## Example

```python
from tailscale_openapi.models.set_device_ip_request import SetDeviceIpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDeviceIpRequest from a JSON string
set_device_ip_request_instance = SetDeviceIpRequest.from_json(json)
# print the JSON string representation of the object
print(SetDeviceIpRequest.to_json())

# convert the object into a dict
set_device_ip_request_dict = set_device_ip_request_instance.to_dict()
# create an instance of SetDeviceIpRequest from a dict
set_device_ip_request_from_dict = SetDeviceIpRequest.from_dict(set_device_ip_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


