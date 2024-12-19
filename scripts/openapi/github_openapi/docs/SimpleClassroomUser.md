# SimpleClassroomUser

A GitHub user simplified for Classroom.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**login** | **str** |  | 
**avatar_url** | **str** |  | 
**html_url** | **str** |  | 

## Example

```python
from github_openapi.models.simple_classroom_user import SimpleClassroomUser

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleClassroomUser from a JSON string
simple_classroom_user_instance = SimpleClassroomUser.from_json(json)
# print the JSON string representation of the object
print(SimpleClassroomUser.to_json())

# convert the object into a dict
simple_classroom_user_dict = simple_classroom_user_instance.to_dict()
# create an instance of SimpleClassroomUser from a dict
simple_classroom_user_from_dict = SimpleClassroomUser.from_dict(simple_classroom_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


