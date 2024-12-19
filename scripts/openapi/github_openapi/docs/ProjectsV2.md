# ProjectsV2

A projects v2 project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**node_id** | **str** |  | 
**owner** | [**SimpleUser**](SimpleUser.md) |  | 
**creator** | [**SimpleUser**](SimpleUser.md) |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**public** | **bool** |  | 
**closed_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**number** | **int** |  | 
**short_description** | **str** |  | 
**deleted_at** | **datetime** |  | 
**deleted_by** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 

## Example

```python
from github_openapi.models.projects_v2 import ProjectsV2

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsV2 from a JSON string
projects_v2_instance = ProjectsV2.from_json(json)
# print the JSON string representation of the object
print(ProjectsV2.to_json())

# convert the object into a dict
projects_v2_dict = projects_v2_instance.to_dict()
# create an instance of ProjectsV2 from a dict
projects_v2_from_dict = ProjectsV2.from_dict(projects_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


