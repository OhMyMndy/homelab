# KeyCapabilities

`capabilities` is a mapping of resources to permissible actions. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**KeyCapabilitiesDevices**](KeyCapabilitiesDevices.md) |  | [optional] 

## Example

```python
from tailscale_openapi.models.key_capabilities import KeyCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of KeyCapabilities from a JSON string
key_capabilities_instance = KeyCapabilities.from_json(json)
# print the JSON string representation of the object
print(KeyCapabilities.to_json())

# convert the object into a dict
key_capabilities_dict = key_capabilities_instance.to_dict()
# create an instance of KeyCapabilities from a dict
key_capabilities_from_dict = KeyCapabilities.from_dict(key_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


