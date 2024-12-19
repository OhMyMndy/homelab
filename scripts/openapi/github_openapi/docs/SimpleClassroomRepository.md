# SimpleClassroomRepository

A GitHub repository view for Classroom

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique identifier of the repository. | 
**full_name** | **str** | The full, globally unique name of the repository. | 
**html_url** | **str** | The URL to view the repository on GitHub.com. | 
**node_id** | **str** | The GraphQL identifier of the repository. | 
**private** | **bool** | Whether the repository is private. | 
**default_branch** | **str** | The default branch for the repository. | 

## Example

```python
from github_openapi.models.simple_classroom_repository import SimpleClassroomRepository

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleClassroomRepository from a JSON string
simple_classroom_repository_instance = SimpleClassroomRepository.from_json(json)
# print the JSON string representation of the object
print(SimpleClassroomRepository.to_json())

# convert the object into a dict
simple_classroom_repository_dict = simple_classroom_repository_instance.to_dict()
# create an instance of SimpleClassroomRepository from a dict
simple_classroom_repository_from_dict = SimpleClassroomRepository.from_dict(simple_classroom_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


