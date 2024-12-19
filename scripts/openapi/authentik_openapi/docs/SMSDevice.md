# SMSDevice

Serializer for sms authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human-readable name of this device. | 
**pk** | **int** |  | [readonly] 
**phone_number** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.sms_device import SMSDevice

# TODO update the JSON string below
json = "{}"
# create an instance of SMSDevice from a JSON string
sms_device_instance = SMSDevice.from_json(json)
# print the JSON string representation of the object
print(SMSDevice.to_json())

# convert the object into a dict
sms_device_dict = sms_device_instance.to_dict()
# create an instance of SMSDevice from a dict
sms_device_from_dict = SMSDevice.from_dict(sms_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


