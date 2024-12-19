# StaticDeviceTokenRequest

Serializer for static device's tokens

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 

## Example

```python
from authentik_openapi.models.static_device_token_request import StaticDeviceTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StaticDeviceTokenRequest from a JSON string
static_device_token_request_instance = StaticDeviceTokenRequest.from_json(json)
# print the JSON string representation of the object
print(StaticDeviceTokenRequest.to_json())

# convert the object into a dict
static_device_token_request_dict = static_device_token_request_instance.to_dict()
# create an instance of StaticDeviceTokenRequest from a dict
static_device_token_request_from_dict = StaticDeviceTokenRequest.from_dict(static_device_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


