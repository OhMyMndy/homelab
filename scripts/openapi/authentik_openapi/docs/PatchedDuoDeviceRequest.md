# PatchedDuoDeviceRequest

Serializer for Duo authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human-readable name of this device. | [optional] 

## Example

```python
from authentik_openapi.models.patched_duo_device_request import PatchedDuoDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDuoDeviceRequest from a JSON string
patched_duo_device_request_instance = PatchedDuoDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedDuoDeviceRequest.to_json())

# convert the object into a dict
patched_duo_device_request_dict = patched_duo_device_request_instance.to_dict()
# create an instance of PatchedDuoDeviceRequest from a dict
patched_duo_device_request_from_dict = PatchedDuoDeviceRequest.from_dict(patched_duo_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


