# PaginatedRACPropertyMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[RACPropertyMapping]**](RACPropertyMapping.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_rac_property_mapping_list import PaginatedRACPropertyMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRACPropertyMappingList from a JSON string
paginated_rac_property_mapping_list_instance = PaginatedRACPropertyMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRACPropertyMappingList.to_json())

# convert the object into a dict
paginated_rac_property_mapping_list_dict = paginated_rac_property_mapping_list_instance.to_dict()
# create an instance of PaginatedRACPropertyMappingList from a dict
paginated_rac_property_mapping_list_from_dict = PaginatedRACPropertyMappingList.from_dict(paginated_rac_property_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


