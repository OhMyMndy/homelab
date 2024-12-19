# PatchedUserWriteStageRequest

UserWriteStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**user_creation_mode** | [**UserCreationModeEnum**](UserCreationModeEnum.md) |  | [optional] 
**create_users_as_inactive** | **bool** | When set, newly created users are inactive and cannot login. | [optional] 
**create_users_group** | **str** | Optionally add newly created users to this group. | [optional] 
**user_type** | [**UserTypeEnum**](UserTypeEnum.md) |  | [optional] 
**user_path_template** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_user_write_stage_request import PatchedUserWriteStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUserWriteStageRequest from a JSON string
patched_user_write_stage_request_instance = PatchedUserWriteStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedUserWriteStageRequest.to_json())

# convert the object into a dict
patched_user_write_stage_request_dict = patched_user_write_stage_request_instance.to_dict()
# create an instance of PatchedUserWriteStageRequest from a dict
patched_user_write_stage_request_from_dict = PatchedUserWriteStageRequest.from_dict(patched_user_write_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


