# UsersCreateSshSigningKeyForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | A descriptive name for the new key. | [optional] 
**key** | **str** | The public SSH key to add to your GitHub account. For more information, see \&quot;[Checking for existing SSH keys](https://docs.github.com/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys).\&quot; | 

## Example

```python
from github_openapi.models.users_create_ssh_signing_key_for_authenticated_user_request import UsersCreateSshSigningKeyForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateSshSigningKeyForAuthenticatedUserRequest from a JSON string
users_create_ssh_signing_key_for_authenticated_user_request_instance = UsersCreateSshSigningKeyForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(UsersCreateSshSigningKeyForAuthenticatedUserRequest.to_json())

# convert the object into a dict
users_create_ssh_signing_key_for_authenticated_user_request_dict = users_create_ssh_signing_key_for_authenticated_user_request_instance.to_dict()
# create an instance of UsersCreateSshSigningKeyForAuthenticatedUserRequest from a dict
users_create_ssh_signing_key_for_authenticated_user_request_from_dict = UsersCreateSshSigningKeyForAuthenticatedUserRequest.from_dict(users_create_ssh_signing_key_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


