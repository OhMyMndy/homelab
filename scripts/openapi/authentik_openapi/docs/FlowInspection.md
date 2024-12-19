# FlowInspection

Serializer for inspect endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plans** | [**List[FlowInspectorPlan]**](FlowInspectorPlan.md) |  | 
**current_plan** | [**FlowInspectorPlan**](FlowInspectorPlan.md) |  | [optional] 
**is_completed** | **bool** |  | 

## Example

```python
from authentik_openapi.models.flow_inspection import FlowInspection

# TODO update the JSON string below
json = "{}"
# create an instance of FlowInspection from a JSON string
flow_inspection_instance = FlowInspection.from_json(json)
# print the JSON string representation of the object
print(FlowInspection.to_json())

# convert the object into a dict
flow_inspection_dict = flow_inspection_instance.to_dict()
# create an instance of FlowInspection from a dict
flow_inspection_from_dict = FlowInspection.from_dict(flow_inspection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


