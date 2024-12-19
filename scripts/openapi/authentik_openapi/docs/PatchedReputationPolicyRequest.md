# PatchedReputationPolicyRequest

Reputation Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**check_ip** | **bool** |  | [optional] 
**check_username** | **bool** |  | [optional] 
**threshold** | **int** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_reputation_policy_request import PatchedReputationPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedReputationPolicyRequest from a JSON string
patched_reputation_policy_request_instance = PatchedReputationPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedReputationPolicyRequest.to_json())

# convert the object into a dict
patched_reputation_policy_request_dict = patched_reputation_policy_request_instance.to_dict()
# create an instance of PatchedReputationPolicyRequest from a dict
patched_reputation_policy_request_from_dict = PatchedReputationPolicyRequest.from_dict(patched_reputation_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


