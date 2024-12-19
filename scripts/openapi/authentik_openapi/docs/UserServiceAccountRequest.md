# UserServiceAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**create_group** | **bool** |  | [optional] [default to False]
**expiring** | **bool** |  | [optional] [default to True]
**expires** | **datetime** | If not provided, valid for 360 days | [optional] 

## Example

```python
from authentik_openapi.models.user_service_account_request import UserServiceAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserServiceAccountRequest from a JSON string
user_service_account_request_instance = UserServiceAccountRequest.from_json(json)
# print the JSON string representation of the object
print(UserServiceAccountRequest.to_json())

# convert the object into a dict
user_service_account_request_dict = user_service_account_request_instance.to_dict()
# create an instance of UserServiceAccountRequest from a dict
user_service_account_request_from_dict = UserServiceAccountRequest.from_dict(user_service_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


