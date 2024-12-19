# FlowErrorChallenge

Challenge class when an unhandled error occurs during a stage. Normal users are shown an error message, superusers are shown a full stacktrace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'native']
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-flow-error']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**request_id** | **str** |  | 
**error** | **str** |  | [optional] 
**traceback** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.flow_error_challenge import FlowErrorChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of FlowErrorChallenge from a JSON string
flow_error_challenge_instance = FlowErrorChallenge.from_json(json)
# print the JSON string representation of the object
print(FlowErrorChallenge.to_json())

# convert the object into a dict
flow_error_challenge_dict = flow_error_challenge_instance.to_dict()
# create an instance of FlowErrorChallenge from a dict
flow_error_challenge_from_dict = FlowErrorChallenge.from_dict(flow_error_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


