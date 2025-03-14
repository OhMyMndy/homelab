# PasswordExpiryPolicy

Password Expiry Policy Serializer

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
**days** | **int** |  | 
**deny_only** | **bool** |  | [optional] 

## Example

```python
from authentik_openapi.models.password_expiry_policy import PasswordExpiryPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordExpiryPolicy from a JSON string
password_expiry_policy_instance = PasswordExpiryPolicy.from_json(json)
# print the JSON string representation of the object
print(PasswordExpiryPolicy.to_json())

# convert the object into a dict
password_expiry_policy_dict = password_expiry_policy_instance.to_dict()
# create an instance of PasswordExpiryPolicy from a dict
password_expiry_policy_from_dict = PasswordExpiryPolicy.from_dict(password_expiry_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


