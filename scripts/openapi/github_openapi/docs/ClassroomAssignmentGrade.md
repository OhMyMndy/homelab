# ClassroomAssignmentGrade

Grade for a student or groups GitHub Classroom assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_name** | **str** | Name of the assignment | 
**assignment_url** | **str** | URL of the assignment | 
**starter_code_url** | **str** | URL of the starter code for the assignment | 
**github_username** | **str** | GitHub username of the student | 
**roster_identifier** | **str** | Roster identifier of the student | 
**student_repository_name** | **str** | Name of the student&#39;s assignment repository | 
**student_repository_url** | **str** | URL of the student&#39;s assignment repository | 
**submission_timestamp** | **str** | Timestamp of the student&#39;s assignment submission | 
**points_awarded** | **int** | Number of points awarded to the student | 
**points_available** | **int** | Number of points available for the assignment | 
**group_name** | **str** | If a group assignment, name of the group the student is in | [optional] 

## Example

```python
from github_openapi.models.classroom_assignment_grade import ClassroomAssignmentGrade

# TODO update the JSON string below
json = "{}"
# create an instance of ClassroomAssignmentGrade from a JSON string
classroom_assignment_grade_instance = ClassroomAssignmentGrade.from_json(json)
# print the JSON string representation of the object
print(ClassroomAssignmentGrade.to_json())

# convert the object into a dict
classroom_assignment_grade_dict = classroom_assignment_grade_instance.to_dict()
# create an instance of ClassroomAssignmentGrade from a dict
classroom_assignment_grade_from_dict = ClassroomAssignmentGrade.from_dict(classroom_assignment_grade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


