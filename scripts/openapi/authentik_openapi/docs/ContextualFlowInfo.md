# ContextualFlowInfo

Contextual flow information for a challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**background** | **str** |  | [optional] 
**cancel_url** | **str** |  | 
**layout** | [**ContextualFlowInfoLayoutEnum**](ContextualFlowInfoLayoutEnum.md) |  | 

## Example

```python
from authentik_openapi.models.contextual_flow_info import ContextualFlowInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContextualFlowInfo from a JSON string
contextual_flow_info_instance = ContextualFlowInfo.from_json(json)
# print the JSON string representation of the object
print(ContextualFlowInfo.to_json())

# convert the object into a dict
contextual_flow_info_dict = contextual_flow_info_instance.to_dict()
# create an instance of ContextualFlowInfo from a dict
contextual_flow_info_from_dict = ContextualFlowInfo.from_dict(contextual_flow_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


