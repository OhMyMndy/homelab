# AuthenticatorDuoStageRequest

AuthenticatorDuoStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**api_hostname** | **str** |  | 
**admin_integration_key** | **str** |  | [optional] 
**admin_secret_key** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.authenticator_duo_stage_request import AuthenticatorDuoStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorDuoStageRequest from a JSON string
authenticator_duo_stage_request_instance = AuthenticatorDuoStageRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorDuoStageRequest.to_json())

# convert the object into a dict
authenticator_duo_stage_request_dict = authenticator_duo_stage_request_instance.to_dict()
# create an instance of AuthenticatorDuoStageRequest from a dict
authenticator_duo_stage_request_from_dict = AuthenticatorDuoStageRequest.from_dict(authenticator_duo_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


