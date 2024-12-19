# PaginatedMicrosoftEntraProviderUserList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[MicrosoftEntraProviderUser]**](MicrosoftEntraProviderUser.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_microsoft_entra_provider_user_list import PaginatedMicrosoftEntraProviderUserList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMicrosoftEntraProviderUserList from a JSON string
paginated_microsoft_entra_provider_user_list_instance = PaginatedMicrosoftEntraProviderUserList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMicrosoftEntraProviderUserList.to_json())

# convert the object into a dict
paginated_microsoft_entra_provider_user_list_dict = paginated_microsoft_entra_provider_user_list_instance.to_dict()
# create an instance of PaginatedMicrosoftEntraProviderUserList from a dict
paginated_microsoft_entra_provider_user_list_from_dict = PaginatedMicrosoftEntraProviderUserList.from_dict(paginated_microsoft_entra_provider_user_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


