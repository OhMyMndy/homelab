# ActionsCreateOrUpdateEnvironmentSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_value** | **str** | Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get an environment public key](https://docs.github.com/rest/actions/secrets#get-an-environment-public-key) endpoint. | 
**key_id** | **str** | ID of the key you used to encrypt the secret. | 

## Example

```python
from github_openapi.models.actions_create_or_update_environment_secret_request import ActionsCreateOrUpdateEnvironmentSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsCreateOrUpdateEnvironmentSecretRequest from a JSON string
actions_create_or_update_environment_secret_request_instance = ActionsCreateOrUpdateEnvironmentSecretRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsCreateOrUpdateEnvironmentSecretRequest.to_json())

# convert the object into a dict
actions_create_or_update_environment_secret_request_dict = actions_create_or_update_environment_secret_request_instance.to_dict()
# create an instance of ActionsCreateOrUpdateEnvironmentSecretRequest from a dict
actions_create_or_update_environment_secret_request_from_dict = ActionsCreateOrUpdateEnvironmentSecretRequest.from_dict(actions_create_or_update_environment_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


