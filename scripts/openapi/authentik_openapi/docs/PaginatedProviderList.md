# PaginatedProviderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Provider]**](Provider.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_provider_list import PaginatedProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProviderList from a JSON string
paginated_provider_list_instance = PaginatedProviderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedProviderList.to_json())

# convert the object into a dict
paginated_provider_list_dict = paginated_provider_list_instance.to_dict()
# create an instance of PaginatedProviderList from a dict
paginated_provider_list_from_dict = PaginatedProviderList.from_dict(paginated_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


