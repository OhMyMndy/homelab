# PaginatedMicrosoftEntraProviderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[MicrosoftEntraProvider]**](MicrosoftEntraProvider.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_microsoft_entra_provider_list import PaginatedMicrosoftEntraProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMicrosoftEntraProviderList from a JSON string
paginated_microsoft_entra_provider_list_instance = PaginatedMicrosoftEntraProviderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMicrosoftEntraProviderList.to_json())

# convert the object into a dict
paginated_microsoft_entra_provider_list_dict = paginated_microsoft_entra_provider_list_instance.to_dict()
# create an instance of PaginatedMicrosoftEntraProviderList from a dict
paginated_microsoft_entra_provider_list_from_dict = PaginatedMicrosoftEntraProviderList.from_dict(paginated_microsoft_entra_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


