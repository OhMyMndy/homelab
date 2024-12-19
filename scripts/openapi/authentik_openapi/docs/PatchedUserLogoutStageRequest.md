# PatchedUserLogoutStageRequest

UserLogoutStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_user_logout_stage_request import PatchedUserLogoutStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUserLogoutStageRequest from a JSON string
patched_user_logout_stage_request_instance = PatchedUserLogoutStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedUserLogoutStageRequest.to_json())

# convert the object into a dict
patched_user_logout_stage_request_dict = patched_user_logout_stage_request_instance.to_dict()
# create an instance of PatchedUserLogoutStageRequest from a dict
patched_user_logout_stage_request_from_dict = PatchedUserLogoutStageRequest.from_dict(patched_user_logout_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


