# ProjectsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the project | [optional] 
**body** | **str** | Body of the project | [optional] 
**state** | **str** | State of the project; either &#39;open&#39; or &#39;closed&#39; | [optional] 
**organization_permission** | **str** | The baseline permission that all organization members have on this project | [optional] 
**private** | **bool** | Whether or not this project can be seen by everyone. | [optional] 

## Example

```python
from github_openapi.models.projects_update_request import ProjectsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsUpdateRequest from a JSON string
projects_update_request_instance = ProjectsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectsUpdateRequest.to_json())

# convert the object into a dict
projects_update_request_dict = projects_update_request_instance.to_dict()
# create an instance of ProjectsUpdateRequest from a dict
projects_update_request_from_dict = ProjectsUpdateRequest.from_dict(projects_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


