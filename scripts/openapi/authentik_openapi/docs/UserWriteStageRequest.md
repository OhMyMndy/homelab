# UserWriteStageRequest

UserWriteStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**user_creation_mode** | [**UserCreationModeEnum**](UserCreationModeEnum.md) |  | [optional] 
**create_users_as_inactive** | **bool** | When set, newly created users are inactive and cannot login. | [optional] 
**create_users_group** | **str** | Optionally add newly created users to this group. | [optional] 
**user_type** | [**UserTypeEnum**](UserTypeEnum.md) |  | [optional] 
**user_path_template** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.user_write_stage_request import UserWriteStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserWriteStageRequest from a JSON string
user_write_stage_request_instance = UserWriteStageRequest.from_json(json)
# print the JSON string representation of the object
print(UserWriteStageRequest.to_json())

# convert the object into a dict
user_write_stage_request_dict = user_write_stage_request_instance.to_dict()
# create an instance of UserWriteStageRequest from a dict
user_write_stage_request_from_dict = UserWriteStageRequest.from_dict(user_write_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


