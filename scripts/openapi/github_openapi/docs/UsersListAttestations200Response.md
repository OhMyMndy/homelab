# UsersListAttestations200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestations** | [**List[UsersListAttestations200ResponseAttestationsInner]**](UsersListAttestations200ResponseAttestationsInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.users_list_attestations200_response import UsersListAttestations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsersListAttestations200Response from a JSON string
users_list_attestations200_response_instance = UsersListAttestations200Response.from_json(json)
# print the JSON string representation of the object
print(UsersListAttestations200Response.to_json())

# convert the object into a dict
users_list_attestations200_response_dict = users_list_attestations200_response_instance.to_dict()
# create an instance of UsersListAttestations200Response from a dict
users_list_attestations200_response_from_dict = UsersListAttestations200Response.from_dict(users_list_attestations200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


