# CodespacesCreateOrUpdateRepoSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_value** | **str** | Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get a repository public key](https://docs.github.com/rest/codespaces/repository-secrets#get-a-repository-public-key) endpoint. | [optional] 
**key_id** | **str** | ID of the key you used to encrypt the secret. | [optional] 

## Example

```python
from github_openapi.models.codespaces_create_or_update_repo_secret_request import CodespacesCreateOrUpdateRepoSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesCreateOrUpdateRepoSecretRequest from a JSON string
codespaces_create_or_update_repo_secret_request_instance = CodespacesCreateOrUpdateRepoSecretRequest.from_json(json)
# print the JSON string representation of the object
print(CodespacesCreateOrUpdateRepoSecretRequest.to_json())

# convert the object into a dict
codespaces_create_or_update_repo_secret_request_dict = codespaces_create_or_update_repo_secret_request_instance.to_dict()
# create an instance of CodespacesCreateOrUpdateRepoSecretRequest from a dict
codespaces_create_or_update_repo_secret_request_from_dict = CodespacesCreateOrUpdateRepoSecretRequest.from_dict(codespaces_create_or_update_repo_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


