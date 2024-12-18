# AuthorizeDeviceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorized** | **bool** | - If &#x60;true&#x60;, authorize a new device or re-authorize a previously deauthorized device. - If &#x60;false&#x60;, deauthorize an authorized device.  | 

## Example

```python
from tailscale_openapi.models.authorize_device_request import AuthorizeDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizeDeviceRequest from a JSON string
authorize_device_request_instance = AuthorizeDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(AuthorizeDeviceRequest.to_json())

# convert the object into a dict
authorize_device_request_dict = authorize_device_request_instance.to_dict()
# create an instance of AuthorizeDeviceRequest from a dict
authorize_device_request_from_dict = AuthorizeDeviceRequest.from_dict(authorize_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


