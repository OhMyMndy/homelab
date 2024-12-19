# UserSelfGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [readonly] 
**pk** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.user_self_groups import UserSelfGroups

# TODO update the JSON string below
json = "{}"
# create an instance of UserSelfGroups from a JSON string
user_self_groups_instance = UserSelfGroups.from_json(json)
# print the JSON string representation of the object
print(UserSelfGroups.to_json())

# convert the object into a dict
user_self_groups_dict = user_self_groups_instance.to_dict()
# create an instance of UserSelfGroups from a dict
user_self_groups_from_dict = UserSelfGroups.from_dict(user_self_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


