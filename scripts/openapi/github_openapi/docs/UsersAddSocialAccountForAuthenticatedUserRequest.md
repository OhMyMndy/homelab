# UsersAddSocialAccountForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_urls** | **List[str]** | Full URLs for the social media profiles to add. | 

## Example

```python
from github_openapi.models.users_add_social_account_for_authenticated_user_request import UsersAddSocialAccountForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersAddSocialAccountForAuthenticatedUserRequest from a JSON string
users_add_social_account_for_authenticated_user_request_instance = UsersAddSocialAccountForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(UsersAddSocialAccountForAuthenticatedUserRequest.to_json())

# convert the object into a dict
users_add_social_account_for_authenticated_user_request_dict = users_add_social_account_for_authenticated_user_request_instance.to_dict()
# create an instance of UsersAddSocialAccountForAuthenticatedUserRequest from a dict
users_add_social_account_for_authenticated_user_request_from_dict = UsersAddSocialAccountForAuthenticatedUserRequest.from_dict(users_add_social_account_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


