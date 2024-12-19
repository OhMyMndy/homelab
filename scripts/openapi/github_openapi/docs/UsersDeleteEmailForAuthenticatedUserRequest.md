# UsersDeleteEmailForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** | Email addresses associated with the GitHub user account. | 

## Example

```python
from github_openapi.models.users_delete_email_for_authenticated_user_request import UsersDeleteEmailForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersDeleteEmailForAuthenticatedUserRequest from a JSON string
users_delete_email_for_authenticated_user_request_instance = UsersDeleteEmailForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(UsersDeleteEmailForAuthenticatedUserRequest.to_json())

# convert the object into a dict
users_delete_email_for_authenticated_user_request_dict = users_delete_email_for_authenticated_user_request_instance.to_dict()
# create an instance of UsersDeleteEmailForAuthenticatedUserRequest from a dict
users_delete_email_for_authenticated_user_request_from_dict = UsersDeleteEmailForAuthenticatedUserRequest.from_dict(users_delete_email_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


