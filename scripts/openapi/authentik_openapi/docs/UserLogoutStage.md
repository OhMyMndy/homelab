# UserLogoutStage

UserLogoutStage Serializer

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

## Example

```python
from authentik_openapi.models.user_logout_stage import UserLogoutStage

# TODO update the JSON string below
json = "{}"
# create an instance of UserLogoutStage from a JSON string
user_logout_stage_instance = UserLogoutStage.from_json(json)
# print the JSON string representation of the object
print(UserLogoutStage.to_json())

# convert the object into a dict
user_logout_stage_dict = user_logout_stage_instance.to_dict()
# create an instance of UserLogoutStage from a dict
user_logout_stage_from_dict = UserLogoutStage.from_dict(user_logout_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


