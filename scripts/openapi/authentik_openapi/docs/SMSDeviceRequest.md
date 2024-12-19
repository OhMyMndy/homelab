# SMSDeviceRequest

Serializer for sms authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human-readable name of this device. | 

## Example

```python
from authentik_openapi.models.sms_device_request import SMSDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SMSDeviceRequest from a JSON string
sms_device_request_instance = SMSDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(SMSDeviceRequest.to_json())

# convert the object into a dict
sms_device_request_dict = sms_device_request_instance.to_dict()
# create an instance of SMSDeviceRequest from a dict
sms_device_request_from_dict = SMSDeviceRequest.from_dict(sms_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


