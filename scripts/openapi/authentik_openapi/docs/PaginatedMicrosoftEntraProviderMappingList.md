# PaginatedMicrosoftEntraProviderMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[MicrosoftEntraProviderMapping]**](MicrosoftEntraProviderMapping.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_microsoft_entra_provider_mapping_list import PaginatedMicrosoftEntraProviderMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMicrosoftEntraProviderMappingList from a JSON string
paginated_microsoft_entra_provider_mapping_list_instance = PaginatedMicrosoftEntraProviderMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMicrosoftEntraProviderMappingList.to_json())

# convert the object into a dict
paginated_microsoft_entra_provider_mapping_list_dict = paginated_microsoft_entra_provider_mapping_list_instance.to_dict()
# create an instance of PaginatedMicrosoftEntraProviderMappingList from a dict
paginated_microsoft_entra_provider_mapping_list_from_dict = PaginatedMicrosoftEntraProviderMappingList.from_dict(paginated_microsoft_entra_provider_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


