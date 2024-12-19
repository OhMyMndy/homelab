# UsersDeleteEmailForAuthenticatedUserRequestOneOf

Deletes one or more email addresses from your GitHub account. Must contain at least one email address. **Note:** Alternatively, you can pass a single email address or an `array` of emails addresses directly, but we recommend that you pass an object using the `emails` key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** | Email addresses associated with the GitHub user account. | 

## Example

```python
from github_openapi.models.users_delete_email_for_authenticated_user_request_one_of import UsersDeleteEmailForAuthenticatedUserRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of UsersDeleteEmailForAuthenticatedUserRequestOneOf from a JSON string
users_delete_email_for_authenticated_user_request_one_of_instance = UsersDeleteEmailForAuthenticatedUserRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(UsersDeleteEmailForAuthenticatedUserRequestOneOf.to_json())

# convert the object into a dict
users_delete_email_for_authenticated_user_request_one_of_dict = users_delete_email_for_authenticated_user_request_one_of_instance.to_dict()
# create an instance of UsersDeleteEmailForAuthenticatedUserRequestOneOf from a dict
users_delete_email_for_authenticated_user_request_one_of_from_dict = UsersDeleteEmailForAuthenticatedUserRequestOneOf.from_dict(users_delete_email_for_authenticated_user_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


