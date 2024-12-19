# PatchedSMSDeviceRequest

Serializer for sms authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human-readable name of this device. | [optional] 

## Example

```python
from authentik_openapi.models.patched_sms_device_request import PatchedSMSDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSMSDeviceRequest from a JSON string
patched_sms_device_request_instance = PatchedSMSDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSMSDeviceRequest.to_json())

# convert the object into a dict
patched_sms_device_request_dict = patched_sms_device_request_instance.to_dict()
# create an instance of PatchedSMSDeviceRequest from a dict
patched_sms_device_request_from_dict = PatchedSMSDeviceRequest.from_dict(patched_sms_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


