# Classroom

A GitHub Classroom classroom

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the classroom. | 
**name** | **str** | The name of the classroom. | 
**archived** | **bool** | Whether classroom is archived. | 
**organization** | [**SimpleClassroomOrganization**](SimpleClassroomOrganization.md) |  | 
**url** | **str** | The URL of the classroom on GitHub Classroom. | 

## Example

```python
from github_openapi.models.classroom import Classroom

# TODO update the JSON string below
json = "{}"
# create an instance of Classroom from a JSON string
classroom_instance = Classroom.from_json(json)
# print the JSON string representation of the object
print(Classroom.to_json())

# convert the object into a dict
classroom_dict = classroom_instance.to_dict()
# create an instance of Classroom from a dict
classroom_from_dict = Classroom.from_dict(classroom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


