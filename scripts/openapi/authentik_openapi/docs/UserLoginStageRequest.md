# UserLoginStageRequest

UserLoginStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**session_duration** | **str** | Determines how long a session lasts. Default of 0 means that the sessions lasts until the browser is closed. (Format: hours&#x3D;-1;minutes&#x3D;-2;seconds&#x3D;-3) | [optional] 
**terminate_other_sessions** | **bool** | Terminate all other sessions of the user logging in. | [optional] 
**remember_me_offset** | **str** | Offset the session will be extended by when the user picks the remember me option. Default of 0 means that the remember me option will not be shown. (Format: hours&#x3D;-1;minutes&#x3D;-2;seconds&#x3D;-3) | [optional] 
**network_binding** | [**NetworkBindingEnum**](NetworkBindingEnum.md) | Bind sessions created by this stage to the configured network | [optional] 
**geoip_binding** | [**GeoipBindingEnum**](GeoipBindingEnum.md) | Bind sessions created by this stage to the configured GeoIP location | [optional] 

## Example

```python
from authentik_openapi.models.user_login_stage_request import UserLoginStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserLoginStageRequest from a JSON string
user_login_stage_request_instance = UserLoginStageRequest.from_json(json)
# print the JSON string representation of the object
print(UserLoginStageRequest.to_json())

# convert the object into a dict
user_login_stage_request_dict = user_login_stage_request_instance.to_dict()
# create an instance of UserLoginStageRequest from a dict
user_login_stage_request_from_dict = UserLoginStageRequest.from_dict(user_login_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


