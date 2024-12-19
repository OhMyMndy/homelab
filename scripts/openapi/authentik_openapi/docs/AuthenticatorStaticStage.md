# AuthenticatorStaticStage

AuthenticatorStaticStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object type so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**flow_set** | [**List[FlowSet]**](FlowSet.md) |  | [optional] 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**token_count** | **int** |  | [optional] 
**token_length** | **int** |  | [optional] 

## Example

```python
from authentik_openapi.models.authenticator_static_stage import AuthenticatorStaticStage

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorStaticStage from a JSON string
authenticator_static_stage_instance = AuthenticatorStaticStage.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorStaticStage.to_json())

# convert the object into a dict
authenticator_static_stage_dict = authenticator_static_stage_instance.to_dict()
# create an instance of AuthenticatorStaticStage from a dict
authenticator_static_stage_from_dict = AuthenticatorStaticStage.from_dict(authenticator_static_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


