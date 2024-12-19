# UserPasswordSetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 

## Example

```python
from authentik_openapi.models.user_password_set_request import UserPasswordSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserPasswordSetRequest from a JSON string
user_password_set_request_instance = UserPasswordSetRequest.from_json(json)
# print the JSON string representation of the object
print(UserPasswordSetRequest.to_json())

# convert the object into a dict
user_password_set_request_dict = user_password_set_request_instance.to_dict()
# create an instance of UserPasswordSetRequest from a dict
user_password_set_request_from_dict = UserPasswordSetRequest.from_dict(user_password_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


