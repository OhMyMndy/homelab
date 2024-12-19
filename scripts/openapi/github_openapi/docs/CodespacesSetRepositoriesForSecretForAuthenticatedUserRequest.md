# CodespacesSetRepositoriesForSecretForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_repository_ids** | **List[int]** | An array of repository ids for which a codespace can access the secret. You can manage the list of selected repositories using the [List selected repositories for a user secret](https://docs.github.com/rest/codespaces/secrets#list-selected-repositories-for-a-user-secret), [Add a selected repository to a user secret](https://docs.github.com/rest/codespaces/secrets#add-a-selected-repository-to-a-user-secret), and [Remove a selected repository from a user secret](https://docs.github.com/rest/codespaces/secrets#remove-a-selected-repository-from-a-user-secret) endpoints. | 

## Example

```python
from github_openapi.models.codespaces_set_repositories_for_secret_for_authenticated_user_request import CodespacesSetRepositoriesForSecretForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesSetRepositoriesForSecretForAuthenticatedUserRequest from a JSON string
codespaces_set_repositories_for_secret_for_authenticated_user_request_instance = CodespacesSetRepositoriesForSecretForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(CodespacesSetRepositoriesForSecretForAuthenticatedUserRequest.to_json())

# convert the object into a dict
codespaces_set_repositories_for_secret_for_authenticated_user_request_dict = codespaces_set_repositories_for_secret_for_authenticated_user_request_instance.to_dict()
# create an instance of CodespacesSetRepositoriesForSecretForAuthenticatedUserRequest from a dict
codespaces_set_repositories_for_secret_for_authenticated_user_request_from_dict = CodespacesSetRepositoriesForSecretForAuthenticatedUserRequest.from_dict(codespaces_set_repositories_for_secret_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


