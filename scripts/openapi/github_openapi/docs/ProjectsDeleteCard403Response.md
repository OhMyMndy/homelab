# ProjectsDeleteCard403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from github_openapi.models.projects_delete_card403_response import ProjectsDeleteCard403Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsDeleteCard403Response from a JSON string
projects_delete_card403_response_instance = ProjectsDeleteCard403Response.from_json(json)
# print the JSON string representation of the object
print(ProjectsDeleteCard403Response.to_json())

# convert the object into a dict
projects_delete_card403_response_dict = projects_delete_card403_response_instance.to_dict()
# create an instance of ProjectsDeleteCard403Response from a dict
projects_delete_card403_response_from_dict = ProjectsDeleteCard403Response.from_dict(projects_delete_card403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


