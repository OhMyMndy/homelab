# FlowInspectorPlan

Serializer for an active FlowPlan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_stage** | [**FlowStageBinding**](FlowStageBinding.md) |  | [readonly] 
**next_planned_stage** | [**FlowStageBinding**](FlowStageBinding.md) |  | [readonly] 
**plan_context** | **Dict[str, object]** | Get the plan&#39;s context, sanitized | [readonly] 
**session_id** | **str** | Get a unique session ID | [readonly] 

## Example

```python
from authentik_openapi.models.flow_inspector_plan import FlowInspectorPlan

# TODO update the JSON string below
json = "{}"
# create an instance of FlowInspectorPlan from a JSON string
flow_inspector_plan_instance = FlowInspectorPlan.from_json(json)
# print the JSON string representation of the object
print(FlowInspectorPlan.to_json())

# convert the object into a dict
flow_inspector_plan_dict = flow_inspector_plan_instance.to_dict()
# create an instance of FlowInspectorPlan from a dict
flow_inspector_plan_from_dict = FlowInspectorPlan.from_dict(flow_inspector_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


