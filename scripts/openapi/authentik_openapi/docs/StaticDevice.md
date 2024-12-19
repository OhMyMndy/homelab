# StaticDevice

Serializer for static authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human-readable name of this device. | 
**token_set** | [**List[StaticDeviceToken]**](StaticDeviceToken.md) |  | [readonly] 
**pk** | **int** |  | [readonly] 

## Example

```python
from authentik_openapi.models.static_device import StaticDevice

# TODO update the JSON string below
json = "{}"
# create an instance of StaticDevice from a JSON string
static_device_instance = StaticDevice.from_json(json)
# print the JSON string representation of the object
print(StaticDevice.to_json())

# convert the object into a dict
static_device_dict = static_device_instance.to_dict()
# create an instance of StaticDevice from a dict
static_device_from_dict = StaticDevice.from_dict(static_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


