# UserServiceAccountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**token** | **str** |  | 
**user_uid** | **str** |  | 
**user_pk** | **int** |  | 
**group_pk** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.user_service_account_response import UserServiceAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserServiceAccountResponse from a JSON string
user_service_account_response_instance = UserServiceAccountResponse.from_json(json)
# print the JSON string representation of the object
print(UserServiceAccountResponse.to_json())

# convert the object into a dict
user_service_account_response_dict = user_service_account_response_instance.to_dict()
# create an instance of UserServiceAccountResponse from a dict
user_service_account_response_from_dict = UserServiceAccountResponse.from_dict(user_service_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


