# PaginatedSCIMSourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SCIMSource]**](SCIMSource.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_scim_source_list import PaginatedSCIMSourceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSCIMSourceList from a JSON string
paginated_scim_source_list_instance = PaginatedSCIMSourceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSCIMSourceList.to_json())

# convert the object into a dict
paginated_scim_source_list_dict = paginated_scim_source_list_instance.to_dict()
# create an instance of PaginatedSCIMSourceList from a dict
paginated_scim_source_list_from_dict = PaginatedSCIMSourceList.from_dict(paginated_scim_source_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


