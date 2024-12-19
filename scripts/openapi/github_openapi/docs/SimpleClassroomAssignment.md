# SimpleClassroomAssignment

A GitHub Classroom assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the repository. | 
**public_repo** | **bool** | Whether an accepted assignment creates a public repository. | 
**title** | **str** | Assignment title. | 
**type** | **str** | Whether it&#39;s a Group Assignment or Individual Assignment. | 
**invite_link** | **str** | The link that a student can use to accept the assignment. | 
**invitations_enabled** | **bool** | Whether the invitation link is enabled. Visiting an enabled invitation link will accept the assignment. | 
**slug** | **str** | Sluggified name of the assignment. | 
**students_are_repo_admins** | **bool** | Whether students are admins on created repository on accepted assignment. | 
**feedback_pull_requests_enabled** | **bool** | Whether feedback pull request will be created on assignment acceptance. | 
**max_teams** | **int** | The maximum allowable teams for the assignment. | [optional] 
**max_members** | **int** | The maximum allowable members per team. | [optional] 
**editor** | **str** | The selected editor for the assignment. | 
**accepted** | **int** | The number of students that have accepted the assignment. | 
**submitted** | **int** | The number of students that have submitted the assignment. | 
**passing** | **int** | The number of students that have passed the assignment. | 
**language** | **str** | The programming language used in the assignment. | 
**deadline** | **datetime** | The time at which the assignment is due. | 
**classroom** | [**SimpleClassroom**](SimpleClassroom.md) |  | 

## Example

```python
from github_openapi.models.simple_classroom_assignment import SimpleClassroomAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleClassroomAssignment from a JSON string
simple_classroom_assignment_instance = SimpleClassroomAssignment.from_json(json)
# print the JSON string representation of the object
print(SimpleClassroomAssignment.to_json())

# convert the object into a dict
simple_classroom_assignment_dict = simple_classroom_assignment_instance.to_dict()
# create an instance of SimpleClassroomAssignment from a dict
simple_classroom_assignment_from_dict = SimpleClassroomAssignment.from_dict(simple_classroom_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


