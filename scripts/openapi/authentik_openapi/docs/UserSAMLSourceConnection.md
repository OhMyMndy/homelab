# UserSAMLSourceConnection

SAML Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**user** | **int** |  | 
**source** | [**Source**](Source.md) |  | [readonly] 
**identifier** | **str** |  | 

## Example

```python
from authentik_openapi.models.user_saml_source_connection import UserSAMLSourceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of UserSAMLSourceConnection from a JSON string
user_saml_source_connection_instance = UserSAMLSourceConnection.from_json(json)
# print the JSON string representation of the object
print(UserSAMLSourceConnection.to_json())

# convert the object into a dict
user_saml_source_connection_dict = user_saml_source_connection_instance.to_dict()
# create an instance of UserSAMLSourceConnection from a dict
user_saml_source_connection_from_dict = UserSAMLSourceConnection.from_dict(user_saml_source_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


