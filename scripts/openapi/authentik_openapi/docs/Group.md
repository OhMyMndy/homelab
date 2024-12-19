# Group

Group Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**num_pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**is_superuser** | **bool** | Users added to this group will be superusers. | [optional] 
**parent** | **str** |  | [optional] 
**parent_name** | **str** |  | [readonly] 
**users** | **List[int]** |  | [optional] 
**users_obj** | [**List[GroupMember]**](GroupMember.md) |  | [readonly] 
**attributes** | **Dict[str, object]** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**roles_obj** | [**List[Role]**](Role.md) |  | [readonly] 

## Example

```python
from authentik_openapi.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


