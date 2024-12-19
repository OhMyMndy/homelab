# PaginatedSCIMSourceGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SCIMSourceGroup]**](SCIMSourceGroup.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_scim_source_group_list import PaginatedSCIMSourceGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSCIMSourceGroupList from a JSON string
paginated_scim_source_group_list_instance = PaginatedSCIMSourceGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSCIMSourceGroupList.to_json())

# convert the object into a dict
paginated_scim_source_group_list_dict = paginated_scim_source_group_list_instance.to_dict()
# create an instance of PaginatedSCIMSourceGroupList from a dict
paginated_scim_source_group_list_from_dict = PaginatedSCIMSourceGroupList.from_dict(paginated_scim_source_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


