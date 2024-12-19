# ProjectsCreateForOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the project. | 
**body** | **str** | The description of the project. | [optional] 

## Example

```python
from github_openapi.models.projects_create_for_org_request import ProjectsCreateForOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsCreateForOrgRequest from a JSON string
projects_create_for_org_request_instance = ProjectsCreateForOrgRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectsCreateForOrgRequest.to_json())

# convert the object into a dict
projects_create_for_org_request_dict = projects_create_for_org_request_instance.to_dict()
# create an instance of ProjectsCreateForOrgRequest from a dict
projects_create_for_org_request_from_dict = ProjectsCreateForOrgRequest.from_dict(projects_create_for_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


