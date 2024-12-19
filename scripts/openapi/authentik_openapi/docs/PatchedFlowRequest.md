# PatchedFlowRequest

Flow Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**slug** | **str** | Visible in the URL. | [optional] 
**title** | **str** | Shown as the Title in Flow pages. | [optional] 
**designation** | [**FlowDesignationEnum**](FlowDesignationEnum.md) | Decides what this Flow is used for. For example, the Authentication flow is redirect to when an un-authenticated user visits authentik. | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**compatibility_mode** | **bool** | Enable compatibility mode, increases compatibility with password managers on mobile devices. | [optional] 
**layout** | [**FlowLayoutEnum**](FlowLayoutEnum.md) |  | [optional] 
**denied_action** | [**DeniedActionEnum**](DeniedActionEnum.md) | Configure what should happen when a flow denies access to a user. | [optional] 
**authentication** | [**AuthenticationEnum**](AuthenticationEnum.md) | Required level of authentication and authorization to access a flow. | [optional] 

## Example

```python
from authentik_openapi.models.patched_flow_request import PatchedFlowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedFlowRequest from a JSON string
patched_flow_request_instance = PatchedFlowRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedFlowRequest.to_json())

# convert the object into a dict
patched_flow_request_dict = patched_flow_request_instance.to_dict()
# create an instance of PatchedFlowRequest from a dict
patched_flow_request_from_dict = PatchedFlowRequest.from_dict(patched_flow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


