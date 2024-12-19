# WebAuthnDeviceRequest

Serializer for WebAuthn authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from authentik_openapi.models.web_authn_device_request import WebAuthnDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthnDeviceRequest from a JSON string
web_authn_device_request_instance = WebAuthnDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(WebAuthnDeviceRequest.to_json())

# convert the object into a dict
web_authn_device_request_dict = web_authn_device_request_instance.to_dict()
# create an instance of WebAuthnDeviceRequest from a dict
web_authn_device_request_from_dict = WebAuthnDeviceRequest.from_dict(web_authn_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


