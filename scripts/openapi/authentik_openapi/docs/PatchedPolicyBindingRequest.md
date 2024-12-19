# PatchedPolicyBindingRequest

PolicyBinding Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** |  | [optional] 
**group** | **str** |  | [optional] 
**user** | **int** |  | [optional] 
**target** | **str** |  | [optional] 
**negate** | **bool** | Negates the outcome of the policy. Messages are unaffected. | [optional] 
**enabled** | **bool** |  | [optional] 
**order** | **int** |  | [optional] 
**timeout** | **int** | Timeout after which Policy execution is terminated. | [optional] 
**failure_result** | **bool** | Result if the Policy execution fails. | [optional] 

## Example

```python
from authentik_openapi.models.patched_policy_binding_request import PatchedPolicyBindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPolicyBindingRequest from a JSON string
patched_policy_binding_request_instance = PatchedPolicyBindingRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPolicyBindingRequest.to_json())

# convert the object into a dict
patched_policy_binding_request_dict = patched_policy_binding_request_instance.to_dict()
# create an instance of PatchedPolicyBindingRequest from a dict
patched_policy_binding_request_from_dict = PatchedPolicyBindingRequest.from_dict(patched_policy_binding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


