# ProjectsV2Item

An item belonging to a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**node_id** | **str** |  | [optional] 
**project_node_id** | **str** |  | [optional] 
**content_node_id** | **str** |  | 
**content_type** | [**ProjectsV2ItemContentType**](ProjectsV2ItemContentType.md) |  | 
**creator** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**archived_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.projects_v2_item import ProjectsV2Item

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsV2Item from a JSON string
projects_v2_item_instance = ProjectsV2Item.from_json(json)
# print the JSON string representation of the object
print(ProjectsV2Item.to_json())

# convert the object into a dict
projects_v2_item_dict = projects_v2_item_instance.to_dict()
# create an instance of ProjectsV2Item from a dict
projects_v2_item_from_dict = ProjectsV2Item.from_dict(projects_v2_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


