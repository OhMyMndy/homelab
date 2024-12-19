# ExpressionPolicyRequest

Group Membership Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**expression** | **str** |  | 

## Example

```python
from authentik_openapi.models.expression_policy_request import ExpressionPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExpressionPolicyRequest from a JSON string
expression_policy_request_instance = ExpressionPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(ExpressionPolicyRequest.to_json())

# convert the object into a dict
expression_policy_request_dict = expression_policy_request_instance.to_dict()
# create an instance of ExpressionPolicyRequest from a dict
expression_policy_request_from_dict = ExpressionPolicyRequest.from_dict(expression_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


