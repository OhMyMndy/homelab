# PolicyBindingRequest

PolicyBinding Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** |  | [optional] 
**group** | **str** |  | [optional] 
**user** | **int** |  | [optional] 
**target** | **str** |  | 
**negate** | **bool** | Negates the outcome of the policy. Messages are unaffected. | [optional] 
**enabled** | **bool** |  | [optional] 
**order** | **int** |  | 
**timeout** | **int** | Timeout after which Policy execution is terminated. | [optional] 
**failure_result** | **bool** | Result if the Policy execution fails. | [optional] 

## Example

```python
from authentik_openapi.models.policy_binding_request import PolicyBindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyBindingRequest from a JSON string
policy_binding_request_instance = PolicyBindingRequest.from_json(json)
# print the JSON string representation of the object
print(PolicyBindingRequest.to_json())

# convert the object into a dict
policy_binding_request_dict = policy_binding_request_instance.to_dict()
# create an instance of PolicyBindingRequest from a dict
policy_binding_request_from_dict = PolicyBindingRequest.from_dict(policy_binding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


