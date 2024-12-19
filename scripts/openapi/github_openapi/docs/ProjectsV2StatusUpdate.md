# ProjectsV2StatusUpdate

An status update belonging to a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**node_id** | **str** |  | 
**project_node_id** | **str** |  | [optional] 
**creator** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**status** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**target_date** | **date** |  | [optional] 
**body** | **str** | Body of the status update | [optional] 

## Example

```python
from github_openapi.models.projects_v2_status_update import ProjectsV2StatusUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsV2StatusUpdate from a JSON string
projects_v2_status_update_instance = ProjectsV2StatusUpdate.from_json(json)
# print the JSON string representation of the object
print(ProjectsV2StatusUpdate.to_json())

# convert the object into a dict
projects_v2_status_update_dict = projects_v2_status_update_instance.to_dict()
# create an instance of ProjectsV2StatusUpdate from a dict
projects_v2_status_update_from_dict = ProjectsV2StatusUpdate.from_dict(projects_v2_status_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


