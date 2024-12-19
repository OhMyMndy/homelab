# PaginatedExtraUserObjectPermissionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[ExtraUserObjectPermission]**](ExtraUserObjectPermission.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_extra_user_object_permission_list import PaginatedExtraUserObjectPermissionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedExtraUserObjectPermissionList from a JSON string
paginated_extra_user_object_permission_list_instance = PaginatedExtraUserObjectPermissionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedExtraUserObjectPermissionList.to_json())

# convert the object into a dict
paginated_extra_user_object_permission_list_dict = paginated_extra_user_object_permission_list_instance.to_dict()
# create an instance of PaginatedExtraUserObjectPermissionList from a dict
paginated_extra_user_object_permission_list_from_dict = PaginatedExtraUserObjectPermissionList.from_dict(paginated_extra_user_object_permission_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


