# PolicyBinding

PolicyBinding Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**policy** | **str** |  | [optional] 
**group** | **str** |  | [optional] 
**user** | **int** |  | [optional] 
**policy_obj** | [**Policy**](Policy.md) |  | [readonly] 
**group_obj** | [**Group**](Group.md) |  | [readonly] 
**user_obj** | [**User**](User.md) |  | [readonly] 
**target** | **str** |  | 
**negate** | **bool** | Negates the outcome of the policy. Messages are unaffected. | [optional] 
**enabled** | **bool** |  | [optional] 
**order** | **int** |  | 
**timeout** | **int** | Timeout after which Policy execution is terminated. | [optional] 
**failure_result** | **bool** | Result if the Policy execution fails. | [optional] 

## Example

```python
from authentik_openapi.models.policy_binding import PolicyBinding

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyBinding from a JSON string
policy_binding_instance = PolicyBinding.from_json(json)
# print the JSON string representation of the object
print(PolicyBinding.to_json())

# convert the object into a dict
policy_binding_dict = policy_binding_instance.to_dict()
# create an instance of PolicyBinding from a dict
policy_binding_from_dict = PolicyBinding.from_dict(policy_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


