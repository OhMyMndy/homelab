# CreateAuthKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**KeyCapabilities**](KeyCapabilities.md) |  | 
**expiry_seconds** | **float** | Specifies the duration in seconds until the key should expire. Defaults to 90 days if not supplied.  | [optional] 
**description** | **str** | A short string specifying the purpose of the key. Can be a maximum of 50 alphanumeric characters. Hyphens and spaces are also allowed.  | [optional] 

## Example

```python
from tailscale_openapi.models.create_auth_key_request import CreateAuthKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthKeyRequest from a JSON string
create_auth_key_request_instance = CreateAuthKeyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAuthKeyRequest.to_json())

# convert the object into a dict
create_auth_key_request_dict = create_auth_key_request_instance.to_dict()
# create an instance of CreateAuthKeyRequest from a dict
create_auth_key_request_from_dict = CreateAuthKeyRequest.from_dict(create_auth_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


