# UserAccountRequest

Account adding/removing operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | 

## Example

```python
from authentik_openapi.models.user_account_request import UserAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserAccountRequest from a JSON string
user_account_request_instance = UserAccountRequest.from_json(json)
# print the JSON string representation of the object
print(UserAccountRequest.to_json())

# convert the object into a dict
user_account_request_dict = user_account_request_instance.to_dict()
# create an instance of UserAccountRequest from a dict
user_account_request_from_dict = UserAccountRequest.from_dict(user_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


