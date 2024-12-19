# UsersAddEmailForAuthenticatedUserRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** | Adds one or more email addresses to your GitHub account. Must contain at least one email address. **Note:** Alternatively, you can pass a single email address or an &#x60;array&#x60; of emails addresses directly, but we recommend that you pass an object using the &#x60;emails&#x60; key. | 

## Example

```python
from github_openapi.models.users_add_email_for_authenticated_user_request_one_of import UsersAddEmailForAuthenticatedUserRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of UsersAddEmailForAuthenticatedUserRequestOneOf from a JSON string
users_add_email_for_authenticated_user_request_one_of_instance = UsersAddEmailForAuthenticatedUserRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(UsersAddEmailForAuthenticatedUserRequestOneOf.to_json())

# convert the object into a dict
users_add_email_for_authenticated_user_request_one_of_dict = users_add_email_for_authenticated_user_request_one_of_instance.to_dict()
# create an instance of UsersAddEmailForAuthenticatedUserRequestOneOf from a dict
users_add_email_for_authenticated_user_request_one_of_from_dict = UsersAddEmailForAuthenticatedUserRequestOneOf.from_dict(users_add_email_for_authenticated_user_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


