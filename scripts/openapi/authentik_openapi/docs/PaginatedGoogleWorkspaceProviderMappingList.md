# PaginatedGoogleWorkspaceProviderMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[GoogleWorkspaceProviderMapping]**](GoogleWorkspaceProviderMapping.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_google_workspace_provider_mapping_list import PaginatedGoogleWorkspaceProviderMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGoogleWorkspaceProviderMappingList from a JSON string
paginated_google_workspace_provider_mapping_list_instance = PaginatedGoogleWorkspaceProviderMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGoogleWorkspaceProviderMappingList.to_json())

# convert the object into a dict
paginated_google_workspace_provider_mapping_list_dict = paginated_google_workspace_provider_mapping_list_instance.to_dict()
# create an instance of PaginatedGoogleWorkspaceProviderMappingList from a dict
paginated_google_workspace_provider_mapping_list_from_dict = PaginatedGoogleWorkspaceProviderMappingList.from_dict(paginated_google_workspace_provider_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


