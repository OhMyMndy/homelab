# UsersDeleteSocialAccountForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_urls** | **List[str]** | Full URLs for the social media profiles to delete. | 

## Example

```python
from github_openapi.models.users_delete_social_account_for_authenticated_user_request import UsersDeleteSocialAccountForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersDeleteSocialAccountForAuthenticatedUserRequest from a JSON string
users_delete_social_account_for_authenticated_user_request_instance = UsersDeleteSocialAccountForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(UsersDeleteSocialAccountForAuthenticatedUserRequest.to_json())

# convert the object into a dict
users_delete_social_account_for_authenticated_user_request_dict = users_delete_social_account_for_authenticated_user_request_instance.to_dict()
# create an instance of UsersDeleteSocialAccountForAuthenticatedUserRequest from a dict
users_delete_social_account_for_authenticated_user_request_from_dict = UsersDeleteSocialAccountForAuthenticatedUserRequest.from_dict(users_delete_social_account_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


