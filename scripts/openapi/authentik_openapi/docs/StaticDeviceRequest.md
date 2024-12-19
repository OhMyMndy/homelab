# StaticDeviceRequest

Serializer for static authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human-readable name of this device. | 

## Example

```python
from authentik_openapi.models.static_device_request import StaticDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StaticDeviceRequest from a JSON string
static_device_request_instance = StaticDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(StaticDeviceRequest.to_json())

# convert the object into a dict
static_device_request_dict = static_device_request_instance.to_dict()
# create an instance of StaticDeviceRequest from a dict
static_device_request_from_dict = StaticDeviceRequest.from_dict(static_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


