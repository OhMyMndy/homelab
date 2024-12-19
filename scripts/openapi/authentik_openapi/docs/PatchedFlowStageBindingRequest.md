# PatchedFlowStageBindingRequest

FlowStageBinding Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** |  | [optional] 
**stage** | **str** |  | [optional] 
**evaluate_on_plan** | **bool** | Evaluate policies during the Flow planning process. | [optional] 
**re_evaluate_policies** | **bool** | Evaluate policies when the Stage is present to the user. | [optional] 
**order** | **int** |  | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**invalid_response_action** | [**InvalidResponseActionEnum**](InvalidResponseActionEnum.md) | Configure how the flow executor should handle an invalid response to a challenge. RETRY returns the error message and a similar challenge to the executor. RESTART restarts the flow from the beginning, and RESTART_WITH_CONTEXT restarts the flow while keeping the current context. | [optional] 

## Example

```python
from authentik_openapi.models.patched_flow_stage_binding_request import PatchedFlowStageBindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedFlowStageBindingRequest from a JSON string
patched_flow_stage_binding_request_instance = PatchedFlowStageBindingRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedFlowStageBindingRequest.to_json())

# convert the object into a dict
patched_flow_stage_binding_request_dict = patched_flow_stage_binding_request_instance.to_dict()
# create an instance of PatchedFlowStageBindingRequest from a dict
patched_flow_stage_binding_request_from_dict = PatchedFlowStageBindingRequest.from_dict(patched_flow_stage_binding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


