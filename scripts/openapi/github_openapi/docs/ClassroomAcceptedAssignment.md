# ClassroomAcceptedAssignment

A GitHub Classroom accepted assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the repository. | 
**submitted** | **bool** | Whether an accepted assignment has been submitted. | 
**passing** | **bool** | Whether a submission passed. | 
**commit_count** | **int** | Count of student commits. | 
**grade** | **str** | Most recent grade. | 
**students** | [**List[SimpleClassroomUser]**](SimpleClassroomUser.md) |  | 
**repository** | [**SimpleClassroomRepository**](SimpleClassroomRepository.md) |  | 
**assignment** | [**SimpleClassroomAssignment**](SimpleClassroomAssignment.md) |  | 

## Example

```python
from github_openapi.models.classroom_accepted_assignment import ClassroomAcceptedAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of ClassroomAcceptedAssignment from a JSON string
classroom_accepted_assignment_instance = ClassroomAcceptedAssignment.from_json(json)
# print the JSON string representation of the object
print(ClassroomAcceptedAssignment.to_json())

# convert the object into a dict
classroom_accepted_assignment_dict = classroom_accepted_assignment_instance.to_dict()
# create an instance of ClassroomAcceptedAssignment from a dict
classroom_accepted_assignment_from_dict = ClassroomAcceptedAssignment.from_dict(classroom_accepted_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


