# UserOAuthSourceConnection

OAuth Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**user** | **int** |  | 
**source** | [**Source**](Source.md) |  | [readonly] 
**identifier** | **str** |  | 

## Example

```python
from authentik_openapi.models.user_o_auth_source_connection import UserOAuthSourceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of UserOAuthSourceConnection from a JSON string
user_o_auth_source_connection_instance = UserOAuthSourceConnection.from_json(json)
# print the JSON string representation of the object
print(UserOAuthSourceConnection.to_json())

# convert the object into a dict
user_o_auth_source_connection_dict = user_o_auth_source_connection_instance.to_dict()
# create an instance of UserOAuthSourceConnection from a dict
user_o_auth_source_connection_from_dict = UserOAuthSourceConnection.from_dict(user_o_auth_source_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


