# TOTPDeviceRequest

Serializer for totp authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human-readable name of this device. | 

## Example

```python
from authentik_openapi.models.totp_device_request import TOTPDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TOTPDeviceRequest from a JSON string
totp_device_request_instance = TOTPDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(TOTPDeviceRequest.to_json())

# convert the object into a dict
totp_device_request_dict = totp_device_request_instance.to_dict()
# create an instance of TOTPDeviceRequest from a dict
totp_device_request_from_dict = TOTPDeviceRequest.from_dict(totp_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


