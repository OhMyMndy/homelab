# FlowRequest

Flow Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**slug** | **str** | Visible in the URL. | 
**title** | **str** | Shown as the Title in Flow pages. | 
**designation** | [**FlowDesignationEnum**](FlowDesignationEnum.md) | Decides what this Flow is used for. For example, the Authentication flow is redirect to when an un-authenticated user visits authentik. | 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**compatibility_mode** | **bool** | Enable compatibility mode, increases compatibility with password managers on mobile devices. | [optional] 
**layout** | [**FlowLayoutEnum**](FlowLayoutEnum.md) |  | [optional] 
**denied_action** | [**DeniedActionEnum**](DeniedActionEnum.md) | Configure what should happen when a flow denies access to a user. | [optional] 
**authentication** | [**AuthenticationEnum**](AuthenticationEnum.md) | Required level of authentication and authorization to access a flow. | [optional] 

## Example

```python
from authentik_openapi.models.flow_request import FlowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRequest from a JSON string
flow_request_instance = FlowRequest.from_json(json)
# print the JSON string representation of the object
print(FlowRequest.to_json())

# convert the object into a dict
flow_request_dict = flow_request_instance.to_dict()
# create an instance of FlowRequest from a dict
flow_request_from_dict = FlowRequest.from_dict(flow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


