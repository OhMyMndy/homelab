# UsersSetPrimaryEmailVisibilityForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visibility** | **str** | Denotes whether an email is publicly visible. | 

## Example

```python
from github_openapi.models.users_set_primary_email_visibility_for_authenticated_user_request import UsersSetPrimaryEmailVisibilityForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersSetPrimaryEmailVisibilityForAuthenticatedUserRequest from a JSON string
users_set_primary_email_visibility_for_authenticated_user_request_instance = UsersSetPrimaryEmailVisibilityForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(UsersSetPrimaryEmailVisibilityForAuthenticatedUserRequest.to_json())

# convert the object into a dict
users_set_primary_email_visibility_for_authenticated_user_request_dict = users_set_primary_email_visibility_for_authenticated_user_request_instance.to_dict()
# create an instance of UsersSetPrimaryEmailVisibilityForAuthenticatedUserRequest from a dict
users_set_primary_email_visibility_for_authenticated_user_request_from_dict = UsersSetPrimaryEmailVisibilityForAuthenticatedUserRequest.from_dict(users_set_primary_email_visibility_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


