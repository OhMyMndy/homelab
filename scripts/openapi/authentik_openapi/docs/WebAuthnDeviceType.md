# WebAuthnDeviceType

WebAuthnDeviceType Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aaguid** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from authentik_openapi.models.web_authn_device_type import WebAuthnDeviceType

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthnDeviceType from a JSON string
web_authn_device_type_instance = WebAuthnDeviceType.from_json(json)
# print the JSON string representation of the object
print(WebAuthnDeviceType.to_json())

# convert the object into a dict
web_authn_device_type_dict = web_authn_device_type_instance.to_dict()
# create an instance of WebAuthnDeviceType from a dict
web_authn_device_type_from_dict = WebAuthnDeviceType.from_dict(web_authn_device_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


