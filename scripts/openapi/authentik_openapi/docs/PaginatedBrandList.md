# PaginatedBrandList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Brand]**](Brand.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_brand_list import PaginatedBrandList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBrandList from a JSON string
paginated_brand_list_instance = PaginatedBrandList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBrandList.to_json())

# convert the object into a dict
paginated_brand_list_dict = paginated_brand_list_instance.to_dict()
# create an instance of PaginatedBrandList from a dict
paginated_brand_list_from_dict = PaginatedBrandList.from_dict(paginated_brand_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


