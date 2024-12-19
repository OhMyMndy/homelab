# FlowSet

Stripped down flow serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**policybindingmodel_ptr_id** | **str** |  | [readonly] 
**name** | **str** |  | 
**slug** | **str** | Visible in the URL. | 
**title** | **str** | Shown as the Title in Flow pages. | 
**designation** | [**FlowDesignationEnum**](FlowDesignationEnum.md) | Decides what this Flow is used for. For example, the Authentication flow is redirect to when an un-authenticated user visits authentik. | 
**background** | **str** | Get the URL to the background image. If the name is /static or starts with http it is returned as-is | [readonly] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**compatibility_mode** | **bool** | Enable compatibility mode, increases compatibility with password managers on mobile devices. | [optional] 
**export_url** | **str** | Get export URL for flow | [readonly] 
**layout** | [**FlowLayoutEnum**](FlowLayoutEnum.md) |  | [optional] 
**denied_action** | [**DeniedActionEnum**](DeniedActionEnum.md) | Configure what should happen when a flow denies access to a user. | [optional] 

## Example

```python
from authentik_openapi.models.flow_set import FlowSet

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSet from a JSON string
flow_set_instance = FlowSet.from_json(json)
# print the JSON string representation of the object
print(FlowSet.to_json())

# convert the object into a dict
flow_set_dict = flow_set_instance.to_dict()
# create an instance of FlowSet from a dict
flow_set_from_dict = FlowSet.from_dict(flow_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


