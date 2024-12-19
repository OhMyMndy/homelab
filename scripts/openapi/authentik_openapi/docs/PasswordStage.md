# PasswordStage

PasswordStage Serializer

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
**backends** | [**List[BackendsEnum]**](BackendsEnum.md) | Selection of backends to test the password against. | 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**failed_attempts_before_cancel** | **int** | How many attempts a user has before the flow is canceled. To lock the user out, use a reputation policy and a user_write stage. | [optional] 

## Example

```python
from authentik_openapi.models.password_stage import PasswordStage

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordStage from a JSON string
password_stage_instance = PasswordStage.from_json(json)
# print the JSON string representation of the object
print(PasswordStage.to_json())

# convert the object into a dict
password_stage_dict = password_stage_instance.to_dict()
# create an instance of PasswordStage from a dict
password_stage_from_dict = PasswordStage.from_dict(password_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


