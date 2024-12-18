# DevicePostureIdentity

Contains extra identifiers from the device when the tailnet it is connected to has device posture identification collection enabled. If the device has not opted-in to posture identification collection, this will contain {\"disabled\": true}. Learn more about posture identity at https://tailscale.com/kb/1326/device-identity. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial_numbers** | **List[str]** |  | [optional] 
**disabled** | **bool** |  | [optional] 

## Example

```python
from tailscale_openapi.models.device_posture_identity import DevicePostureIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePostureIdentity from a JSON string
device_posture_identity_instance = DevicePostureIdentity.from_json(json)
# print the JSON string representation of the object
print(DevicePostureIdentity.to_json())

# convert the object into a dict
device_posture_identity_dict = device_posture_identity_instance.to_dict()
# create an instance of DevicePostureIdentity from a dict
device_posture_identity_from_dict = DevicePostureIdentity.from_dict(device_posture_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


