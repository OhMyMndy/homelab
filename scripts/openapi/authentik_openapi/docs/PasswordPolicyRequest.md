# PasswordPolicyRequest

Password Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**password_field** | **str** | Field key to check, field keys defined in Prompt stages are available. | [optional] 
**amount_digits** | **int** |  | [optional] 
**amount_uppercase** | **int** |  | [optional] 
**amount_lowercase** | **int** |  | [optional] 
**amount_symbols** | **int** |  | [optional] 
**length_min** | **int** |  | [optional] 
**symbol_charset** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**check_static_rules** | **bool** |  | [optional] 
**check_have_i_been_pwned** | **bool** |  | [optional] 
**check_zxcvbn** | **bool** |  | [optional] 
**hibp_allowed_count** | **int** | How many times the password hash is allowed to be on haveibeenpwned | [optional] 
**zxcvbn_score_threshold** | **int** | If the zxcvbn score is equal or less than this value, the policy will fail. | [optional] 

## Example

```python
from authentik_openapi.models.password_policy_request import PasswordPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyRequest from a JSON string
password_policy_request_instance = PasswordPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyRequest.to_json())

# convert the object into a dict
password_policy_request_dict = password_policy_request_instance.to_dict()
# create an instance of PasswordPolicyRequest from a dict
password_policy_request_from_dict = PasswordPolicyRequest.from_dict(password_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


