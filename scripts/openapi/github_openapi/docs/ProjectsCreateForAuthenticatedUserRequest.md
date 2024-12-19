# ProjectsCreateForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the project | 
**body** | **str** | Body of the project | [optional] 

## Example

```python
from github_openapi.models.projects_create_for_authenticated_user_request import ProjectsCreateForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsCreateForAuthenticatedUserRequest from a JSON string
projects_create_for_authenticated_user_request_instance = ProjectsCreateForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectsCreateForAuthenticatedUserRequest.to_json())

# convert the object into a dict
projects_create_for_authenticated_user_request_dict = projects_create_for_authenticated_user_request_instance.to_dict()
# create an instance of ProjectsCreateForAuthenticatedUserRequest from a dict
projects_create_for_authenticated_user_request_from_dict = ProjectsCreateForAuthenticatedUserRequest.from_dict(projects_create_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


