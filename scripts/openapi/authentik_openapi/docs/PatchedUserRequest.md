# PatchedUserRequest

User Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**name** | **str** | User&#39;s display name. | [optional] 
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional] 
**last_login** | **datetime** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**email** | **str** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 
**path** | **str** |  | [optional] 
**type** | [**UserTypeEnum**](UserTypeEnum.md) |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_user_request import PatchedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedUserRequest from a JSON string
patched_user_request_instance = PatchedUserRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedUserRequest.to_json())

# convert the object into a dict
patched_user_request_dict = patched_user_request_instance.to_dict()
# create an instance of PatchedUserRequest from a dict
patched_user_request_from_dict = PatchedUserRequest.from_dict(patched_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


