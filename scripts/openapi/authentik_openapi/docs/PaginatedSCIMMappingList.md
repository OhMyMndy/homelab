# PaginatedSCIMMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SCIMMapping]**](SCIMMapping.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_scim_mapping_list import PaginatedSCIMMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSCIMMappingList from a JSON string
paginated_scim_mapping_list_instance = PaginatedSCIMMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSCIMMappingList.to_json())

# convert the object into a dict
paginated_scim_mapping_list_dict = paginated_scim_mapping_list_instance.to_dict()
# create an instance of PaginatedSCIMMappingList from a dict
paginated_scim_mapping_list_from_dict = PaginatedSCIMMappingList.from_dict(paginated_scim_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


