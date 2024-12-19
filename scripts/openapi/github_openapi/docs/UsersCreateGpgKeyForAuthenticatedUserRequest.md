# UsersCreateGpgKeyForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A descriptive name for the new key. | [optional] 
**armored_public_key** | **str** | A GPG key in ASCII-armored format. | 

## Example

```python
from github_openapi.models.users_create_gpg_key_for_authenticated_user_request import UsersCreateGpgKeyForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersCreateGpgKeyForAuthenticatedUserRequest from a JSON string
users_create_gpg_key_for_authenticated_user_request_instance = UsersCreateGpgKeyForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(UsersCreateGpgKeyForAuthenticatedUserRequest.to_json())

# convert the object into a dict
users_create_gpg_key_for_authenticated_user_request_dict = users_create_gpg_key_for_authenticated_user_request_instance.to_dict()
# create an instance of UsersCreateGpgKeyForAuthenticatedUserRequest from a dict
users_create_gpg_key_for_authenticated_user_request_from_dict = UsersCreateGpgKeyForAuthenticatedUserRequest.from_dict(users_create_gpg_key_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


