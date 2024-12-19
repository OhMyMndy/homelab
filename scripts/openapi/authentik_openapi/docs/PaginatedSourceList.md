# PaginatedSourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Source]**](Source.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_source_list import PaginatedSourceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSourceList from a JSON string
paginated_source_list_instance = PaginatedSourceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSourceList.to_json())

# convert the object into a dict
paginated_source_list_dict = paginated_source_list_instance.to_dict()
# create an instance of PaginatedSourceList from a dict
paginated_source_list_from_dict = PaginatedSourceList.from_dict(paginated_source_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


