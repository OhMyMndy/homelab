# RepoCodespacesSecret

Set repository secrets for GitHub Codespaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the secret. | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.repo_codespaces_secret import RepoCodespacesSecret

# TODO update the JSON string below
json = "{}"
# create an instance of RepoCodespacesSecret from a JSON string
repo_codespaces_secret_instance = RepoCodespacesSecret.from_json(json)
# print the JSON string representation of the object
print(RepoCodespacesSecret.to_json())

# convert the object into a dict
repo_codespaces_secret_dict = repo_codespaces_secret_instance.to_dict()
# create an instance of RepoCodespacesSecret from a dict
repo_codespaces_secret_from_dict = RepoCodespacesSecret.from_dict(repo_codespaces_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


