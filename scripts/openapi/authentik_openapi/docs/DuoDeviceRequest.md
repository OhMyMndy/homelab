# DuoDeviceRequest

Serializer for Duo authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human-readable name of this device. | 

## Example

```python
from authentik_openapi.models.duo_device_request import DuoDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DuoDeviceRequest from a JSON string
duo_device_request_instance = DuoDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(DuoDeviceRequest.to_json())

# convert the object into a dict
duo_device_request_dict = duo_device_request_instance.to_dict()
# create an instance of DuoDeviceRequest from a dict
duo_device_request_from_dict = DuoDeviceRequest.from_dict(duo_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


