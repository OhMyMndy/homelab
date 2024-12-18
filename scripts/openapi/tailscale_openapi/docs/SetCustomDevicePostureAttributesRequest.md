# SetCustomDevicePostureAttributesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**SetCustomDevicePostureAttributesRequestValue**](SetCustomDevicePostureAttributesRequestValue.md) |  | [optional] 
**expiry** | **datetime** | An optional expiry time for a given posture attribute. If set, Tailscale will automatically remove the attribute within a few minutes after the specified time.  | [optional] 
**comment** | **str** | An optional comment indicating a reason why an attribute is set, which will be added to the audit log.  | [optional] 

## Example

```python
from tailscale_openapi.models.set_custom_device_posture_attributes_request import SetCustomDevicePostureAttributesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetCustomDevicePostureAttributesRequest from a JSON string
set_custom_device_posture_attributes_request_instance = SetCustomDevicePostureAttributesRequest.from_json(json)
# print the JSON string representation of the object
print(SetCustomDevicePostureAttributesRequest.to_json())

# convert the object into a dict
set_custom_device_posture_attributes_request_dict = set_custom_device_posture_attributes_request_instance.to_dict()
# create an instance of SetCustomDevicePostureAttributesRequest from a dict
set_custom_device_posture_attributes_request_from_dict = SetCustomDevicePostureAttributesRequest.from_dict(set_custom_device_posture_attributes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


