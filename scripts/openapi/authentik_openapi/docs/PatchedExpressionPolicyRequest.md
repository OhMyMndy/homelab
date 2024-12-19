# PatchedExpressionPolicyRequest

Group Membership Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**expression** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_expression_policy_request import PatchedExpressionPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedExpressionPolicyRequest from a JSON string
patched_expression_policy_request_instance = PatchedExpressionPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedExpressionPolicyRequest.to_json())

# convert the object into a dict
patched_expression_policy_request_dict = patched_expression_policy_request_instance.to_dict()
# create an instance of PatchedExpressionPolicyRequest from a dict
patched_expression_policy_request_from_dict = PatchedExpressionPolicyRequest.from_dict(patched_expression_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


