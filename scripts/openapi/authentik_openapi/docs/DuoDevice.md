# DuoDevice

Serializer for Duo authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**name** | **str** | The human-readable name of this device. | 

## Example

```python
from authentik_openapi.models.duo_device import DuoDevice

# TODO update the JSON string below
json = "{}"
# create an instance of DuoDevice from a JSON string
duo_device_instance = DuoDevice.from_json(json)
# print the JSON string representation of the object
print(DuoDevice.to_json())

# convert the object into a dict
duo_device_dict = duo_device_instance.to_dict()
# create an instance of DuoDevice from a dict
duo_device_from_dict = DuoDevice.from_dict(duo_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


