# PaginatedSCIMProviderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SCIMProvider]**](SCIMProvider.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_scim_provider_list import PaginatedSCIMProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSCIMProviderList from a JSON string
paginated_scim_provider_list_instance = PaginatedSCIMProviderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSCIMProviderList.to_json())

# convert the object into a dict
paginated_scim_provider_list_dict = paginated_scim_provider_list_instance.to_dict()
# create an instance of PaginatedSCIMProviderList from a dict
paginated_scim_provider_list_from_dict = PaginatedSCIMProviderList.from_dict(paginated_scim_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


