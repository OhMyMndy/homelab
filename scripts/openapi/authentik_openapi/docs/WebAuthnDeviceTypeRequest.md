# WebAuthnDeviceTypeRequest

WebAuthnDeviceType Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aaguid** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from authentik_openapi.models.web_authn_device_type_request import WebAuthnDeviceTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthnDeviceTypeRequest from a JSON string
web_authn_device_type_request_instance = WebAuthnDeviceTypeRequest.from_json(json)
# print the JSON string representation of the object
print(WebAuthnDeviceTypeRequest.to_json())

# convert the object into a dict
web_authn_device_type_request_dict = web_authn_device_type_request_instance.to_dict()
# create an instance of WebAuthnDeviceTypeRequest from a dict
web_authn_device_type_request_from_dict = WebAuthnDeviceTypeRequest.from_dict(web_authn_device_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


