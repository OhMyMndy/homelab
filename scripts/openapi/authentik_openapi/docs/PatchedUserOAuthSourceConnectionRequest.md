# PatchedUserOAuthSourceConnectionRequest

OAuth Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_user_o_auth_source_connection_request import PatchedUserOAuthSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUserOAuthSourceConnectionRequest from a JSON string
patched_user_o_auth_source_connection_request_instance = PatchedUserOAuthSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedUserOAuthSourceConnectionRequest.to_json())

# convert the object into a dict
patched_user_o_auth_source_connection_request_dict = patched_user_o_auth_source_connection_request_instance.to_dict()
# create an instance of PatchedUserOAuthSourceConnectionRequest from a dict
patched_user_o_auth_source_connection_request_from_dict = PatchedUserOAuthSourceConnectionRequest.from_dict(patched_user_o_auth_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


