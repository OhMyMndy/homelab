# PasswordStageRequest

PasswordStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**backends** | [**List[BackendsEnum]**](BackendsEnum.md) | Selection of backends to test the password against. | 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**failed_attempts_before_cancel** | **int** | How many attempts a user has before the flow is canceled. To lock the user out, use a reputation policy and a user_write stage. | [optional] 

## Example

```python
from authentik_openapi.models.password_stage_request import PasswordStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordStageRequest from a JSON string
password_stage_request_instance = PasswordStageRequest.from_json(json)
# print the JSON string representation of the object
print(PasswordStageRequest.to_json())

# convert the object into a dict
password_stage_request_dict = password_stage_request_instance.to_dict()
# create an instance of PasswordStageRequest from a dict
password_stage_request_from_dict = PasswordStageRequest.from_dict(password_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


