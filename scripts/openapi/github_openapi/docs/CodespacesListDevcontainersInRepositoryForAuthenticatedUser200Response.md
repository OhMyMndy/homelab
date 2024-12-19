# CodespacesListDevcontainersInRepositoryForAuthenticatedUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**devcontainers** | [**List[CodespacesListDevcontainersInRepositoryForAuthenticatedUser200ResponseDevcontainersInner]**](CodespacesListDevcontainersInRepositoryForAuthenticatedUser200ResponseDevcontainersInner.md) |  | 

## Example

```python
from github_openapi.models.codespaces_list_devcontainers_in_repository_for_authenticated_user200_response import CodespacesListDevcontainersInRepositoryForAuthenticatedUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesListDevcontainersInRepositoryForAuthenticatedUser200Response from a JSON string
codespaces_list_devcontainers_in_repository_for_authenticated_user200_response_instance = CodespacesListDevcontainersInRepositoryForAuthenticatedUser200Response.from_json(json)
# print the JSON string representation of the object
print(CodespacesListDevcontainersInRepositoryForAuthenticatedUser200Response.to_json())

# convert the object into a dict
codespaces_list_devcontainers_in_repository_for_authenticated_user200_response_dict = codespaces_list_devcontainers_in_repository_for_authenticated_user200_response_instance.to_dict()
# create an instance of CodespacesListDevcontainersInRepositoryForAuthenticatedUser200Response from a dict
codespaces_list_devcontainers_in_repository_for_authenticated_user200_response_from_dict = CodespacesListDevcontainersInRepositoryForAuthenticatedUser200Response.from_dict(codespaces_list_devcontainers_in_repository_for_authenticated_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


