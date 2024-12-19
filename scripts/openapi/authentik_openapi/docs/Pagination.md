# Pagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **float** |  | 
**previous** | **float** |  | 
**count** | **float** |  | 
**current** | **float** |  | 
**total_pages** | **float** |  | 
**start_index** | **float** |  | 
**end_index** | **float** |  | 

## Example

```python
from authentik_openapi.models.pagination import Pagination

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination from a JSON string
pagination_instance = Pagination.from_json(json)
# print the JSON string representation of the object
print(Pagination.to_json())

# convert the object into a dict
pagination_dict = pagination_instance.to_dict()
# create an instance of Pagination from a dict
pagination_from_dict = Pagination.from_dict(pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


