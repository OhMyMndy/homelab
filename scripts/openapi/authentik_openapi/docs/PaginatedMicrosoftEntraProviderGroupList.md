# PaginatedMicrosoftEntraProviderGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[MicrosoftEntraProviderGroup]**](MicrosoftEntraProviderGroup.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_microsoft_entra_provider_group_list import PaginatedMicrosoftEntraProviderGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMicrosoftEntraProviderGroupList from a JSON string
paginated_microsoft_entra_provider_group_list_instance = PaginatedMicrosoftEntraProviderGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedMicrosoftEntraProviderGroupList.to_json())

# convert the object into a dict
paginated_microsoft_entra_provider_group_list_dict = paginated_microsoft_entra_provider_group_list_instance.to_dict()
# create an instance of PaginatedMicrosoftEntraProviderGroupList from a dict
paginated_microsoft_entra_provider_group_list_from_dict = PaginatedMicrosoftEntraProviderGroupList.from_dict(paginated_microsoft_entra_provider_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


