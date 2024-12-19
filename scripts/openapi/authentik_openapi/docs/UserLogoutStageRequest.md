# UserLogoutStageRequest

UserLogoutStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 

## Example

```python
from authentik_openapi.models.user_logout_stage_request import UserLogoutStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserLogoutStageRequest from a JSON string
user_logout_stage_request_instance = UserLogoutStageRequest.from_json(json)
# print the JSON string representation of the object
print(UserLogoutStageRequest.to_json())

# convert the object into a dict
user_logout_stage_request_dict = user_logout_stage_request_instance.to_dict()
# create an instance of UserLogoutStageRequest from a dict
user_logout_stage_request_from_dict = UserLogoutStageRequest.from_dict(user_logout_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


