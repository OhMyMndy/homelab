# ProjectsAddCollaboratorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **str** | The permission to grant the collaborator. | [optional] [default to 'write']

## Example

```python
from github_openapi.models.projects_add_collaborator_request import ProjectsAddCollaboratorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsAddCollaboratorRequest from a JSON string
projects_add_collaborator_request_instance = ProjectsAddCollaboratorRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectsAddCollaboratorRequest.to_json())

# convert the object into a dict
projects_add_collaborator_request_dict = projects_add_collaborator_request_instance.to_dict()
# create an instance of ProjectsAddCollaboratorRequest from a dict
projects_add_collaborator_request_from_dict = ProjectsAddCollaboratorRequest.from_dict(projects_add_collaborator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


