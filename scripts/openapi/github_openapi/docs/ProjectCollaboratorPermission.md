# ProjectCollaboratorPermission

Project Collaborator Permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **str** |  | 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 

## Example

```python
from github_openapi.models.project_collaborator_permission import ProjectCollaboratorPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCollaboratorPermission from a JSON string
project_collaborator_permission_instance = ProjectCollaboratorPermission.from_json(json)
# print the JSON string representation of the object
print(ProjectCollaboratorPermission.to_json())

# convert the object into a dict
project_collaborator_permission_dict = project_collaborator_permission_instance.to_dict()
# create an instance of ProjectCollaboratorPermission from a dict
project_collaborator_permission_from_dict = ProjectCollaboratorPermission.from_dict(project_collaborator_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


