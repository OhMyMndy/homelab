# PaginatedSCIMSourceUserList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SCIMSourceUser]**](SCIMSourceUser.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_scim_source_user_list import PaginatedSCIMSourceUserList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSCIMSourceUserList from a JSON string
paginated_scim_source_user_list_instance = PaginatedSCIMSourceUserList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSCIMSourceUserList.to_json())

# convert the object into a dict
paginated_scim_source_user_list_dict = paginated_scim_source_user_list_instance.to_dict()
# create an instance of PaginatedSCIMSourceUserList from a dict
paginated_scim_source_user_list_from_dict = PaginatedSCIMSourceUserList.from_dict(paginated_scim_source_user_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


