# SetCustomDevicePostureAttributesRequestValue

A value can be either a string, number or boolean.  A string value can have a maximum length of 50 characters, and can only contain letters, numbers, underscores, and periods.  A number value is an integer and must be a JSON safe number (up to 2^53 - 1). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tailscale_openapi.models.set_custom_device_posture_attributes_request_value import SetCustomDevicePostureAttributesRequestValue

# TODO update the JSON string below
json = "{}"
# create an instance of SetCustomDevicePostureAttributesRequestValue from a JSON string
set_custom_device_posture_attributes_request_value_instance = SetCustomDevicePostureAttributesRequestValue.from_json(json)
# print the JSON string representation of the object
print(SetCustomDevicePostureAttributesRequestValue.to_json())

# convert the object into a dict
set_custom_device_posture_attributes_request_value_dict = set_custom_device_posture_attributes_request_value_instance.to_dict()
# create an instance of SetCustomDevicePostureAttributesRequestValue from a dict
set_custom_device_posture_attributes_request_value_from_dict = SetCustomDevicePostureAttributesRequestValue.from_dict(set_custom_device_posture_attributes_request_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


