# UserOAuthSourceConnectionRequest

OAuth Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | 
**identifier** | **str** |  | 
**access_token** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.user_o_auth_source_connection_request import UserOAuthSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserOAuthSourceConnectionRequest from a JSON string
user_o_auth_source_connection_request_instance = UserOAuthSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(UserOAuthSourceConnectionRequest.to_json())

# convert the object into a dict
user_o_auth_source_connection_request_dict = user_o_auth_source_connection_request_instance.to_dict()
# create an instance of UserOAuthSourceConnectionRequest from a dict
user_o_auth_source_connection_request_from_dict = UserOAuthSourceConnectionRequest.from_dict(user_o_auth_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


