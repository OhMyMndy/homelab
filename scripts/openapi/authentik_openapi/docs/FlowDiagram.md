# FlowDiagram

response of the flow's diagram action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diagram** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.flow_diagram import FlowDiagram

# TODO update the JSON string below
json = "{}"
# create an instance of FlowDiagram from a JSON string
flow_diagram_instance = FlowDiagram.from_json(json)
# print the JSON string representation of the object
print(FlowDiagram.to_json())

# convert the object into a dict
flow_diagram_dict = flow_diagram_instance.to_dict()
# create an instance of FlowDiagram from a dict
flow_diagram_from_dict = FlowDiagram.from_dict(flow_diagram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


