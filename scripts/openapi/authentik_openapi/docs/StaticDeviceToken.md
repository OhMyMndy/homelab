# StaticDeviceToken

Serializer for static device's tokens

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 

## Example

```python
from authentik_openapi.models.static_device_token import StaticDeviceToken

# TODO update the JSON string below
json = "{}"
# create an instance of StaticDeviceToken from a JSON string
static_device_token_instance = StaticDeviceToken.from_json(json)
# print the JSON string representation of the object
print(StaticDeviceToken.to_json())

# convert the object into a dict
static_device_token_dict = static_device_token_instance.to_dict()
# create an instance of StaticDeviceToken from a dict
static_device_token_from_dict = StaticDeviceToken.from_dict(static_device_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


