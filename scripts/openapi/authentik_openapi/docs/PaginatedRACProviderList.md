# PaginatedRACProviderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[RACProvider]**](RACProvider.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_rac_provider_list import PaginatedRACProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRACProviderList from a JSON string
paginated_rac_provider_list_instance = PaginatedRACProviderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRACProviderList.to_json())

# convert the object into a dict
paginated_rac_provider_list_dict = paginated_rac_provider_list_instance.to_dict()
# create an instance of PaginatedRACProviderList from a dict
paginated_rac_provider_list_from_dict = PaginatedRACProviderList.from_dict(paginated_rac_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


