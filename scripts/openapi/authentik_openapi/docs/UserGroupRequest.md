# UserGroupRequest

Simplified Group Serializer for user's groups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**is_superuser** | **bool** | Users added to this group will be superusers. | [optional] 
**parent** | **str** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik_openapi.models.user_group_request import UserGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupRequest from a JSON string
user_group_request_instance = UserGroupRequest.from_json(json)
# print the JSON string representation of the object
print(UserGroupRequest.to_json())

# convert the object into a dict
user_group_request_dict = user_group_request_instance.to_dict()
# create an instance of UserGroupRequest from a dict
user_group_request_from_dict = UserGroupRequest.from_dict(user_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


