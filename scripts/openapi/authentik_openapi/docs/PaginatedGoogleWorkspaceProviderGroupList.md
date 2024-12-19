# PaginatedGoogleWorkspaceProviderGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[GoogleWorkspaceProviderGroup]**](GoogleWorkspaceProviderGroup.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_google_workspace_provider_group_list import PaginatedGoogleWorkspaceProviderGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGoogleWorkspaceProviderGroupList from a JSON string
paginated_google_workspace_provider_group_list_instance = PaginatedGoogleWorkspaceProviderGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGoogleWorkspaceProviderGroupList.to_json())

# convert the object into a dict
paginated_google_workspace_provider_group_list_dict = paginated_google_workspace_provider_group_list_instance.to_dict()
# create an instance of PaginatedGoogleWorkspaceProviderGroupList from a dict
paginated_google_workspace_provider_group_list_from_dict = PaginatedGoogleWorkspaceProviderGroupList.from_dict(paginated_google_workspace_provider_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


