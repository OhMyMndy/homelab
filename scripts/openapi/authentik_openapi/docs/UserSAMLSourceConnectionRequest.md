# UserSAMLSourceConnectionRequest

SAML Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | 
**identifier** | **str** |  | 

## Example

```python
from authentik_openapi.models.user_saml_source_connection_request import UserSAMLSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSAMLSourceConnectionRequest from a JSON string
user_saml_source_connection_request_instance = UserSAMLSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(UserSAMLSourceConnectionRequest.to_json())

# convert the object into a dict
user_saml_source_connection_request_dict = user_saml_source_connection_request_instance.to_dict()
# create an instance of UserSAMLSourceConnectionRequest from a dict
user_saml_source_connection_request_from_dict = UserSAMLSourceConnectionRequest.from_dict(user_saml_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


