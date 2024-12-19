# PaginatedOutpostList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Outpost]**](Outpost.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_outpost_list import PaginatedOutpostList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOutpostList from a JSON string
paginated_outpost_list_instance = PaginatedOutpostList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOutpostList.to_json())

# convert the object into a dict
paginated_outpost_list_dict = paginated_outpost_list_instance.to_dict()
# create an instance of PaginatedOutpostList from a dict
paginated_outpost_list_from_dict = PaginatedOutpostList.from_dict(paginated_outpost_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


