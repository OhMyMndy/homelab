# PolicyTestRequest

Test policy execution for a user with context

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** |  | 
**context** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_openapi.models.policy_test_request import PolicyTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTestRequest from a JSON string
policy_test_request_instance = PolicyTestRequest.from_json(json)
# print the JSON string representation of the object
print(PolicyTestRequest.to_json())

# convert the object into a dict
policy_test_request_dict = policy_test_request_instance.to_dict()
# create an instance of PolicyTestRequest from a dict
policy_test_request_from_dict = PolicyTestRequest.from_dict(policy_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


