# PatchedAuthenticatorStaticStageRequest

AuthenticatorStaticStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**token_count** | **int** |  | [optional] 
**token_length** | **int** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_authenticator_static_stage_request import PatchedAuthenticatorStaticStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedAuthenticatorStaticStageRequest from a JSON string
patched_authenticator_static_stage_request_instance = PatchedAuthenticatorStaticStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedAuthenticatorStaticStageRequest.to_json())

# convert the object into a dict
patched_authenticator_static_stage_request_dict = patched_authenticator_static_stage_request_instance.to_dict()
# create an instance of PatchedAuthenticatorStaticStageRequest from a dict
patched_authenticator_static_stage_request_from_dict = PatchedAuthenticatorStaticStageRequest.from_dict(patched_authenticator_static_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


