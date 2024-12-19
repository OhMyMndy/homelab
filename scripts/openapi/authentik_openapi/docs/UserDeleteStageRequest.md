# UserDeleteStageRequest

UserDeleteStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 

## Example

```python
from authentik_openapi.models.user_delete_stage_request import UserDeleteStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserDeleteStageRequest from a JSON string
user_delete_stage_request_instance = UserDeleteStageRequest.from_json(json)
# print the JSON string representation of the object
print(UserDeleteStageRequest.to_json())

# convert the object into a dict
user_delete_stage_request_dict = user_delete_stage_request_instance.to_dict()
# create an instance of UserDeleteStageRequest from a dict
user_delete_stage_request_from_dict = UserDeleteStageRequest.from_dict(user_delete_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


