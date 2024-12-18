# KeyCapabilitiesDevices

`devices` specifies the key's permissions over devices. This field is only populated for auth keys. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create** | [**KeyCapabilitiesDevicesCreate**](KeyCapabilitiesDevicesCreate.md) |  | [optional] 

## Example

```python
from tailscale_openapi.models.key_capabilities_devices import KeyCapabilitiesDevices

# TODO update the JSON string below
json = "{}"
# create an instance of KeyCapabilitiesDevices from a JSON string
key_capabilities_devices_instance = KeyCapabilitiesDevices.from_json(json)
# print the JSON string representation of the object
print(KeyCapabilitiesDevices.to_json())

# convert the object into a dict
key_capabilities_devices_dict = key_capabilities_devices_instance.to_dict()
# create an instance of KeyCapabilitiesDevices from a dict
key_capabilities_devices_from_dict = KeyCapabilitiesDevices.from_dict(key_capabilities_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


