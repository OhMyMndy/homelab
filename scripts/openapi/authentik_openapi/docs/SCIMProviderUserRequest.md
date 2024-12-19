# SCIMProviderUserRequest

SCIMProviderUser Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scim_id** | **str** |  | 
**user** | **int** |  | 
**provider** | **int** |  | 

## Example

```python
from authentik_openapi.models.scim_provider_user_request import SCIMProviderUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMProviderUserRequest from a JSON string
scim_provider_user_request_instance = SCIMProviderUserRequest.from_json(json)
# print the JSON string representation of the object
print(SCIMProviderUserRequest.to_json())

# convert the object into a dict
scim_provider_user_request_dict = scim_provider_user_request_instance.to_dict()
# create an instance of SCIMProviderUserRequest from a dict
scim_provider_user_request_from_dict = SCIMProviderUserRequest.from_dict(scim_provider_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


