# PatchedPasswordStageRequest

PasswordStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**backends** | [**List[BackendsEnum]**](BackendsEnum.md) | Selection of backends to test the password against. | [optional] 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**failed_attempts_before_cancel** | **int** | How many attempts a user has before the flow is canceled. To lock the user out, use a reputation policy and a user_write stage. | [optional] 

## Example

```python
from authentik_openapi.models.patched_password_stage_request import PatchedPasswordStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPasswordStageRequest from a JSON string
patched_password_stage_request_instance = PatchedPasswordStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPasswordStageRequest.to_json())

# convert the object into a dict
patched_password_stage_request_dict = patched_password_stage_request_instance.to_dict()
# create an instance of PatchedPasswordStageRequest from a dict
patched_password_stage_request_from_dict = PatchedPasswordStageRequest.from_dict(patched_password_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


