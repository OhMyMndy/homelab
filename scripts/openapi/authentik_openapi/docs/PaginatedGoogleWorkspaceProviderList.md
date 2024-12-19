# PaginatedGoogleWorkspaceProviderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[GoogleWorkspaceProvider]**](GoogleWorkspaceProvider.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_google_workspace_provider_list import PaginatedGoogleWorkspaceProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGoogleWorkspaceProviderList from a JSON string
paginated_google_workspace_provider_list_instance = PaginatedGoogleWorkspaceProviderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGoogleWorkspaceProviderList.to_json())

# convert the object into a dict
paginated_google_workspace_provider_list_dict = paginated_google_workspace_provider_list_instance.to_dict()
# create an instance of PaginatedGoogleWorkspaceProviderList from a dict
paginated_google_workspace_provider_list_from_dict = PaginatedGoogleWorkspaceProviderList.from_dict(paginated_google_workspace_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


