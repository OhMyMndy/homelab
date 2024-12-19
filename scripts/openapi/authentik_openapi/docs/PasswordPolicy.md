# PasswordPolicy

Password Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**bound_to** | **int** | Return objects policy is bound to | [readonly] 
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
from authentik_openapi.models.password_policy import PasswordPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicy from a JSON string
password_policy_instance = PasswordPolicy.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicy.to_json())

# convert the object into a dict
password_policy_dict = password_policy_instance.to_dict()
# create an instance of PasswordPolicy from a dict
password_policy_from_dict = PasswordPolicy.from_dict(password_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


