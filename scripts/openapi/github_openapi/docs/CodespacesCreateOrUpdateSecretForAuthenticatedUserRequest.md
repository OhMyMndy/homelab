# CodespacesCreateOrUpdateSecretForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_value** | **str** | Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get the public key for the authenticated user](https://docs.github.com/rest/codespaces/secrets#get-public-key-for-the-authenticated-user) endpoint. | [optional] 
**key_id** | **str** | ID of the key you used to encrypt the secret. | 
**selected_repository_ids** | [**List[CodespacesCreateOrUpdateSecretForAuthenticatedUserRequestSelectedRepositoryIdsInner]**](CodespacesCreateOrUpdateSecretForAuthenticatedUserRequestSelectedRepositoryIdsInner.md) | An array of repository ids that can access the user secret. You can manage the list of selected repositories using the [List selected repositories for a user secret](https://docs.github.com/rest/codespaces/secrets#list-selected-repositories-for-a-user-secret), [Set selected repositories for a user secret](https://docs.github.com/rest/codespaces/secrets#set-selected-repositories-for-a-user-secret), and [Remove a selected repository from a user secret](https://docs.github.com/rest/codespaces/secrets#remove-a-selected-repository-from-a-user-secret) endpoints. | [optional] 

## Example

```python
from github_openapi.models.codespaces_create_or_update_secret_for_authenticated_user_request import CodespacesCreateOrUpdateSecretForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesCreateOrUpdateSecretForAuthenticatedUserRequest from a JSON string
codespaces_create_or_update_secret_for_authenticated_user_request_instance = CodespacesCreateOrUpdateSecretForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(CodespacesCreateOrUpdateSecretForAuthenticatedUserRequest.to_json())

# convert the object into a dict
codespaces_create_or_update_secret_for_authenticated_user_request_dict = codespaces_create_or_update_secret_for_authenticated_user_request_instance.to_dict()
# create an instance of CodespacesCreateOrUpdateSecretForAuthenticatedUserRequest from a dict
codespaces_create_or_update_secret_for_authenticated_user_request_from_dict = CodespacesCreateOrUpdateSecretForAuthenticatedUserRequest.from_dict(codespaces_create_or_update_secret_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


