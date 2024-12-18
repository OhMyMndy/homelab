# SetDeviceNameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name for the device.  This can be provided as either the fully qualified domain name for the device (e.g. \&quot;nodename.your-domain.ts.net\&quot;) or just the base name (e.g. \&quot;nodename\&quot;).  If &#x60;name&#x60; is unset or provided empty, the device&#39;s name is reset to be generated from its OS hostname.  | 

## Example

```python
from tailscale_openapi.models.set_device_name_request import SetDeviceNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDeviceNameRequest from a JSON string
set_device_name_request_instance = SetDeviceNameRequest.from_json(json)
# print the JSON string representation of the object
print(SetDeviceNameRequest.to_json())

# convert the object into a dict
set_device_name_request_dict = set_device_name_request_instance.to_dict()
# create an instance of SetDeviceNameRequest from a dict
set_device_name_request_from_dict = SetDeviceNameRequest.from_dict(set_device_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


