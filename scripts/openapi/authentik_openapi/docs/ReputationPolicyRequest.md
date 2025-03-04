# ReputationPolicyRequest

Reputation Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**check_ip** | **bool** |  | [optional] 
**check_username** | **bool** |  | [optional] 
**threshold** | **int** |  | [optional] 

## Example

```python
from authentik_openapi.models.reputation_policy_request import ReputationPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReputationPolicyRequest from a JSON string
reputation_policy_request_instance = ReputationPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(ReputationPolicyRequest.to_json())

# convert the object into a dict
reputation_policy_request_dict = reputation_policy_request_instance.to_dict()
# create an instance of ReputationPolicyRequest from a dict
reputation_policy_request_from_dict = ReputationPolicyRequest.from_dict(reputation_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


