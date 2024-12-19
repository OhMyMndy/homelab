# UserSelf

User Serializer for information a user can retrieve about themselves

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | 
**name** | **str** | User&#39;s display name. | 
**is_active** | **bool** | Designates whether this user should be treated as active. Unselect this instead of deleting accounts. | [readonly] 
**is_superuser** | **bool** |  | [readonly] 
**groups** | [**List[UserSelfGroups]**](UserSelfGroups.md) |  | [readonly] 
**email** | **str** |  | [optional] 
**avatar** | **str** | User&#39;s avatar, either a http/https URL or a data URI | [readonly] 
**uid** | **str** |  | [readonly] 
**settings** | **Dict[str, object]** | Get user settings with brand and group settings applied | [readonly] 
**type** | [**UserTypeEnum**](UserTypeEnum.md) |  | [optional] 
**system_permissions** | **List[str]** | Get all system permissions assigned to the user | [readonly] 

## Example

```python
from authentik_openapi.models.user_self import UserSelf

# TODO update the JSON string below
json = "{}"
# create an instance of UserSelf from a JSON string
user_self_instance = UserSelf.from_json(json)
# print the JSON string representation of the object
print(UserSelf.to_json())

# convert the object into a dict
user_self_dict = user_self_instance.to_dict()
# create an instance of UserSelf from a dict
user_self_from_dict = UserSelf.from_dict(user_self_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


