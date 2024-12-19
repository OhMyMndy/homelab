# AuthenticatorStaticStageRequest

AuthenticatorStaticStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**token_count** | **int** |  | [optional] 
**token_length** | **int** |  | [optional] 

## Example

```python
from authentik_openapi.models.authenticator_static_stage_request import AuthenticatorStaticStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorStaticStageRequest from a JSON string
authenticator_static_stage_request_instance = AuthenticatorStaticStageRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorStaticStageRequest.to_json())

# convert the object into a dict
authenticator_static_stage_request_dict = authenticator_static_stage_request_instance.to_dict()
# create an instance of AuthenticatorStaticStageRequest from a dict
authenticator_static_stage_request_from_dict = AuthenticatorStaticStageRequest.from_dict(authenticator_static_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


