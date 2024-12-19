# SimpleClassroom

A GitHub Classroom classroom

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the classroom. | 
**name** | **str** | The name of the classroom. | 
**archived** | **bool** | Returns whether classroom is archived or not. | 
**url** | **str** | The url of the classroom on GitHub Classroom. | 

## Example

```python
from github_openapi.models.simple_classroom import SimpleClassroom

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleClassroom from a JSON string
simple_classroom_instance = SimpleClassroom.from_json(json)
# print the JSON string representation of the object
print(SimpleClassroom.to_json())

# convert the object into a dict
simple_classroom_dict = simple_classroom_instance.to_dict()
# create an instance of SimpleClassroom from a dict
simple_classroom_from_dict = SimpleClassroom.from_dict(simple_classroom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


