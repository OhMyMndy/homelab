# PatchedWebAuthnDeviceRequest

Serializer for WebAuthn authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_web_authn_device_request import PatchedWebAuthnDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedWebAuthnDeviceRequest from a JSON string
patched_web_authn_device_request_instance = PatchedWebAuthnDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedWebAuthnDeviceRequest.to_json())

# convert the object into a dict
patched_web_authn_device_request_dict = patched_web_authn_device_request_instance.to_dict()
# create an instance of PatchedWebAuthnDeviceRequest from a dict
patched_web_authn_device_request_from_dict = PatchedWebAuthnDeviceRequest.from_dict(patched_web_authn_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


