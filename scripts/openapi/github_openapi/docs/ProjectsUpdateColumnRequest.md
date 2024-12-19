# ProjectsUpdateColumnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the project column | 

## Example

```python
from github_openapi.models.projects_update_column_request import ProjectsUpdateColumnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsUpdateColumnRequest from a JSON string
projects_update_column_request_instance = ProjectsUpdateColumnRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectsUpdateColumnRequest.to_json())

# convert the object into a dict
projects_update_column_request_dict = projects_update_column_request_instance.to_dict()
# create an instance of ProjectsUpdateColumnRequest from a dict
projects_update_column_request_from_dict = ProjectsUpdateColumnRequest.from_dict(projects_update_column_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


