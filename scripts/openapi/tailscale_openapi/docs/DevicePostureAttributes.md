# DevicePostureAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Dict[str, ValidateAndTestPolicyFileRequestOneOfInnerSrcPostureAttrsValue]**](ValidateAndTestPolicyFileRequestOneOfInnerSrcPostureAttrsValue.md) | Contains all the posture attributes assigned to a node. Attribute values can be strings, numbers or booleans.  | [optional] 
**expiries** | **Dict[str, datetime]** | Contains the expiry time for each posture attribute, if set.  | [optional] 

## Example

```python
from tailscale_openapi.models.device_posture_attributes import DevicePostureAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePostureAttributes from a JSON string
device_posture_attributes_instance = DevicePostureAttributes.from_json(json)
# print the JSON string representation of the object
print(DevicePostureAttributes.to_json())

# convert the object into a dict
device_posture_attributes_dict = device_posture_attributes_instance.to_dict()
# create an instance of DevicePostureAttributes from a dict
device_posture_attributes_from_dict = DevicePostureAttributes.from_dict(device_posture_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


