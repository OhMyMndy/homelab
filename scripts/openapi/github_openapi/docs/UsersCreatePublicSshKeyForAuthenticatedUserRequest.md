# UsersCreatePublicSshKeyForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | A descriptive name for the new key. | [optional] 
**key** | **str** | The public SSH key to add to your GitHub account. | 

## Example

```python
from github_openapi.models.users_create_public_ssh_key_for_authenticated_user_request import UsersCreatePublicSshKeyForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreatePublicSshKeyForAuthenticatedUserRequest from a JSON string
users_create_public_ssh_key_for_authenticated_user_request_instance = UsersCreatePublicSshKeyForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(UsersCreatePublicSshKeyForAuthenticatedUserRequest.to_json())

# convert the object into a dict
users_create_public_ssh_key_for_authenticated_user_request_dict = users_create_public_ssh_key_for_authenticated_user_request_instance.to_dict()
# create an instance of UsersCreatePublicSshKeyForAuthenticatedUserRequest from a dict
users_create_public_ssh_key_for_authenticated_user_request_from_dict = UsersCreatePublicSshKeyForAuthenticatedUserRequest.from_dict(users_create_public_ssh_key_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


