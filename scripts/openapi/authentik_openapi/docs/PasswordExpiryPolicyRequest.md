# PasswordExpiryPolicyRequest

Password Expiry Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**days** | **int** |  | 
**deny_only** | **bool** |  | [optional] 

## Example

```python
from authentik_openapi.models.password_expiry_policy_request import PasswordExpiryPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordExpiryPolicyRequest from a JSON string
password_expiry_policy_request_instance = PasswordExpiryPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(PasswordExpiryPolicyRequest.to_json())

# convert the object into a dict
password_expiry_policy_request_dict = password_expiry_policy_request_instance.to_dict()
# create an instance of PasswordExpiryPolicyRequest from a dict
password_expiry_policy_request_from_dict = PasswordExpiryPolicyRequest.from_dict(password_expiry_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


