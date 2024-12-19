# DummyPolicyRequest

Dummy Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**result** | **bool** |  | [optional] 
**wait_min** | **int** |  | [optional] 
**wait_max** | **int** |  | [optional] 

## Example

```python
from authentik_openapi.models.dummy_policy_request import DummyPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DummyPolicyRequest from a JSON string
dummy_policy_request_instance = DummyPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(DummyPolicyRequest.to_json())

# convert the object into a dict
dummy_policy_request_dict = dummy_policy_request_instance.to_dict()
# create an instance of DummyPolicyRequest from a dict
dummy_policy_request_from_dict = DummyPolicyRequest.from_dict(dummy_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


