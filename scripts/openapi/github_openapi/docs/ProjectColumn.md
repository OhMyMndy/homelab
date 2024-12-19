# ProjectColumn

Project columns contain cards of work.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**project_url** | **str** |  | 
**cards_url** | **str** |  | 
**id** | **int** | The unique identifier of the project column | 
**node_id** | **str** |  | 
**name** | **str** | Name of the project column | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.project_column import ProjectColumn

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectColumn from a JSON string
project_column_instance = ProjectColumn.from_json(json)
# print the JSON string representation of the object
print(ProjectColumn.to_json())

# convert the object into a dict
project_column_dict = project_column_instance.to_dict()
# create an instance of ProjectColumn from a dict
project_column_from_dict = ProjectColumn.from_dict(project_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


