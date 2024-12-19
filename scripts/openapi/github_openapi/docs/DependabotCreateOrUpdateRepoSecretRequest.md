# DependabotCreateOrUpdateRepoSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_value** | **str** | Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get a repository public key](https://docs.github.com/rest/dependabot/secrets#get-a-repository-public-key) endpoint. | [optional] 
**key_id** | **str** | ID of the key you used to encrypt the secret. | [optional] 

## Example

```python
from github_openapi.models.dependabot_create_or_update_repo_secret_request import DependabotCreateOrUpdateRepoSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DependabotCreateOrUpdateRepoSecretRequest from a JSON string
dependabot_create_or_update_repo_secret_request_instance = DependabotCreateOrUpdateRepoSecretRequest.from_json(json)
# print the JSON string representation of the object
print(DependabotCreateOrUpdateRepoSecretRequest.to_json())

# convert the object into a dict
dependabot_create_or_update_repo_secret_request_dict = dependabot_create_or_update_repo_secret_request_instance.to_dict()
# create an instance of DependabotCreateOrUpdateRepoSecretRequest from a dict
dependabot_create_or_update_repo_secret_request_from_dict = DependabotCreateOrUpdateRepoSecretRequest.from_dict(dependabot_create_or_update_repo_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


