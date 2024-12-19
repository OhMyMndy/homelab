# PolicyTestResult

result of a policy test

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passing** | **bool** |  | 
**messages** | **List[str]** |  | [readonly] 
**log_messages** | [**List[LogEvent]**](LogEvent.md) |  | [readonly] 

## Example

```python
from authentik_openapi.models.policy_test_result import PolicyTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTestResult from a JSON string
policy_test_result_instance = PolicyTestResult.from_json(json)
# print the JSON string representation of the object
print(PolicyTestResult.to_json())

# convert the object into a dict
policy_test_result_dict = policy_test_result_instance.to_dict()
# create an instance of PolicyTestResult from a dict
policy_test_result_from_dict = PolicyTestResult.from_dict(policy_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


