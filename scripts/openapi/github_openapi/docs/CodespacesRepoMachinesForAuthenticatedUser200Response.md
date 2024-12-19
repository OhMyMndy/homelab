# CodespacesRepoMachinesForAuthenticatedUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**machines** | [**List[CodespaceMachine]**](CodespaceMachine.md) |  | 

## Example

```python
from github_openapi.models.codespaces_repo_machines_for_authenticated_user200_response import CodespacesRepoMachinesForAuthenticatedUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesRepoMachinesForAuthenticatedUser200Response from a JSON string
codespaces_repo_machines_for_authenticated_user200_response_instance = CodespacesRepoMachinesForAuthenticatedUser200Response.from_json(json)
# print the JSON string representation of the object
print(CodespacesRepoMachinesForAuthenticatedUser200Response.to_json())

# convert the object into a dict
codespaces_repo_machines_for_authenticated_user200_response_dict = codespaces_repo_machines_for_authenticated_user200_response_instance.to_dict()
# create an instance of CodespacesRepoMachinesForAuthenticatedUser200Response from a dict
codespaces_repo_machines_for_authenticated_user200_response_from_dict = CodespacesRepoMachinesForAuthenticatedUser200Response.from_dict(codespaces_repo_machines_for_authenticated_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


