# PaginatedSCIMProviderUserList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SCIMProviderUser]**](SCIMProviderUser.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_scim_provider_user_list import PaginatedSCIMProviderUserList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSCIMProviderUserList from a JSON string
paginated_scim_provider_user_list_instance = PaginatedSCIMProviderUserList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSCIMProviderUserList.to_json())

# convert the object into a dict
paginated_scim_provider_user_list_dict = paginated_scim_provider_user_list_instance.to_dict()
# create an instance of PaginatedSCIMProviderUserList from a dict
paginated_scim_provider_user_list_from_dict = PaginatedSCIMProviderUserList.from_dict(paginated_scim_provider_user_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


