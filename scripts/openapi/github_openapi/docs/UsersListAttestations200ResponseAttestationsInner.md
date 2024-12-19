# UsersListAttestations200ResponseAttestationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle** | [**SigstoreBundle0**](SigstoreBundle0.md) |  | [optional] 
**repository_id** | **int** |  | [optional] 
**bundle_url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.users_list_attestations200_response_attestations_inner import UsersListAttestations200ResponseAttestationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UsersListAttestations200ResponseAttestationsInner from a JSON string
users_list_attestations200_response_attestations_inner_instance = UsersListAttestations200ResponseAttestationsInner.from_json(json)
# print the JSON string representation of the object
print(UsersListAttestations200ResponseAttestationsInner.to_json())

# convert the object into a dict
users_list_attestations200_response_attestations_inner_dict = users_list_attestations200_response_attestations_inner_instance.to_dict()
# create an instance of UsersListAttestations200ResponseAttestationsInner from a dict
users_list_attestations200_response_attestations_inner_from_dict = UsersListAttestations200ResponseAttestationsInner.from_dict(users_list_attestations200_response_attestations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


