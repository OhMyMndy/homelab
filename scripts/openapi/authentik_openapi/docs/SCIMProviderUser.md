# SCIMProviderUser

SCIMProviderUser Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**scim_id** | **str** |  | 
**user** | **int** |  | 
**user_obj** | [**GroupMember**](GroupMember.md) |  | [readonly] 
**provider** | **int** |  | 

## Example

```python
from authentik_openapi.models.scim_provider_user import SCIMProviderUser

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMProviderUser from a JSON string
scim_provider_user_instance = SCIMProviderUser.from_json(json)
# print the JSON string representation of the object
print(SCIMProviderUser.to_json())

# convert the object into a dict
scim_provider_user_dict = scim_provider_user_instance.to_dict()
# create an instance of SCIMProviderUser from a dict
scim_provider_user_from_dict = SCIMProviderUser.from_dict(scim_provider_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


