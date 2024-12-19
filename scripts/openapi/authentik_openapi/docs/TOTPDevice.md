# TOTPDevice

Serializer for totp authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human-readable name of this device. | 
**pk** | **int** |  | [readonly] 

## Example

```python
from authentik_openapi.models.totp_device import TOTPDevice

# TODO update the JSON string below
json = "{}"
# create an instance of TOTPDevice from a JSON string
totp_device_instance = TOTPDevice.from_json(json)
# print the JSON string representation of the object
print(TOTPDevice.to_json())

# convert the object into a dict
totp_device_dict = totp_device_instance.to_dict()
# create an instance of TOTPDevice from a dict
totp_device_from_dict = TOTPDevice.from_dict(totp_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


