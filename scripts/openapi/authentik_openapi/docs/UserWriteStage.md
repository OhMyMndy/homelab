# UserWriteStage

UserWriteStage Serializer

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
**user_creation_mode** | [**UserCreationModeEnum**](UserCreationModeEnum.md) |  | [optional] 
**create_users_as_inactive** | **bool** | When set, newly created users are inactive and cannot login. | [optional] 
**create_users_group** | **str** | Optionally add newly created users to this group. | [optional] 
**user_type** | [**UserTypeEnum**](UserTypeEnum.md) |  | [optional] 
**user_path_template** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.user_write_stage import UserWriteStage

# TODO update the JSON string below
json = "{}"
# create an instance of UserWriteStage from a JSON string
user_write_stage_instance = UserWriteStage.from_json(json)
# print the JSON string representation of the object
print(UserWriteStage.to_json())

# convert the object into a dict
user_write_stage_dict = user_write_stage_instance.to_dict()
# create an instance of UserWriteStage from a dict
user_write_stage_from_dict = UserWriteStage.from_dict(user_write_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


