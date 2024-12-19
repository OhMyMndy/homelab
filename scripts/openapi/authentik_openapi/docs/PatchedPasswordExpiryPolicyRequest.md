# PatchedPasswordExpiryPolicyRequest

Password Expiry Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**days** | **int** |  | [optional] 
**deny_only** | **bool** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_password_expiry_policy_request import PatchedPasswordExpiryPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPasswordExpiryPolicyRequest from a JSON string
patched_password_expiry_policy_request_instance = PatchedPasswordExpiryPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPasswordExpiryPolicyRequest.to_json())

# convert the object into a dict
patched_password_expiry_policy_request_dict = patched_password_expiry_policy_request_instance.to_dict()
# create an instance of PatchedPasswordExpiryPolicyRequest from a dict
patched_password_expiry_policy_request_from_dict = PatchedPasswordExpiryPolicyRequest.from_dict(patched_password_expiry_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


