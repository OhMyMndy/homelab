# SessionUser

Response for the /user/me endpoint, returns the currently active user (as `user` property) and, if this user is being impersonated, the original user in the `original` property.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserSelf**](UserSelf.md) |  | 
**original** | [**UserSelf**](UserSelf.md) |  | [optional] 

## Example

```python
from authentik_openapi.models.session_user import SessionUser

# TODO update the JSON string below
json = "{}"
# create an instance of SessionUser from a JSON string
session_user_instance = SessionUser.from_json(json)
# print the JSON string representation of the object
print(SessionUser.to_json())

# convert the object into a dict
session_user_dict = session_user_instance.to_dict()
# create an instance of SessionUser from a dict
session_user_from_dict = SessionUser.from_dict(session_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


