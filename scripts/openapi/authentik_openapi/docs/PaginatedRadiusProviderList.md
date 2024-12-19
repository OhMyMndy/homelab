# PaginatedRadiusProviderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[RadiusProvider]**](RadiusProvider.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_radius_provider_list import PaginatedRadiusProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRadiusProviderList from a JSON string
paginated_radius_provider_list_instance = PaginatedRadiusProviderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRadiusProviderList.to_json())

# convert the object into a dict
paginated_radius_provider_list_dict = paginated_radius_provider_list_instance.to_dict()
# create an instance of PaginatedRadiusProviderList from a dict
paginated_radius_provider_list_from_dict = PaginatedRadiusProviderList.from_dict(paginated_radius_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


