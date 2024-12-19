# User

User Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**username** | **str** |  | 
**name** | **str** | User&#39;s display name. | 
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [optional] 
**last_login** | **datetime** |  | [optional] 
**is_superuser** | **bool** |  | [readonly] 
**groups** | **List[str]** |  | [optional] 
**groups_obj** | [**List[UserGroup]**](UserGroup.md) |  | [readonly] 
**email** | **str** |  | [optional] 
**avatar** | **str** | User&#39;s avatar, either a http/https URL or a data URI | [readonly] 
**attributes** | **Dict[str, object]** |  | [optional] 
**uid** | **str** |  | [readonly] 
**path** | **str** |  | [optional] 
**type** | [**UserTypeEnum**](UserTypeEnum.md) |  | [optional] 
**uuid** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


