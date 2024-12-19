# UserObjectPermission

User-bound object level permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**codename** | **str** |  | [readonly] 
**model** | **str** |  | [readonly] 
**app_label** | **str** |  | [readonly] 
**object_pk** | **str** |  | [readonly] 
**name** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.user_object_permission import UserObjectPermission

# TODO update the JSON string below
json = "{}"
# create an instance of UserObjectPermission from a JSON string
user_object_permission_instance = UserObjectPermission.from_json(json)
# print the JSON string representation of the object
print(UserObjectPermission.to_json())

# convert the object into a dict
user_object_permission_dict = user_object_permission_instance.to_dict()
# create an instance of UserObjectPermission from a dict
user_object_permission_from_dict = UserObjectPermission.from_dict(user_object_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


