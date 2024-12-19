# PolicyRequest

Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 

## Example

```python
from authentik_openapi.models.policy_request import PolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRequest from a JSON string
policy_request_instance = PolicyRequest.from_json(json)
# print the JSON string representation of the object
print(PolicyRequest.to_json())

# convert the object into a dict
policy_request_dict = policy_request_instance.to_dict()
# create an instance of PolicyRequest from a dict
policy_request_from_dict = PolicyRequest.from_dict(policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


