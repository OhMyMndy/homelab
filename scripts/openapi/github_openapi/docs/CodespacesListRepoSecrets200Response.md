# CodespacesListRepoSecrets200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**secrets** | [**List[RepoCodespacesSecret]**](RepoCodespacesSecret.md) |  | 

## Example

```python
from github_openapi.models.codespaces_list_repo_secrets200_response import CodespacesListRepoSecrets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesListRepoSecrets200Response from a JSON string
codespaces_list_repo_secrets200_response_instance = CodespacesListRepoSecrets200Response.from_json(json)
# print the JSON string representation of the object
print(CodespacesListRepoSecrets200Response.to_json())

# convert the object into a dict
codespaces_list_repo_secrets200_response_dict = codespaces_list_repo_secrets200_response_instance.to_dict()
# create an instance of CodespacesListRepoSecrets200Response from a dict
codespaces_list_repo_secrets200_response_from_dict = CodespacesListRepoSecrets200Response.from_dict(codespaces_list_repo_secrets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


