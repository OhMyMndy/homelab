# Workflow

A GitHub Actions workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**node_id** | **str** |  | 
**name** | **str** |  | 
**path** | **str** |  | 
**state** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 
**html_url** | **str** |  | 
**badge_url** | **str** |  | 
**deleted_at** | **datetime** |  | [optional] 

## Example

```python
from github_openapi.models.workflow import Workflow

# TODO update the JSON string below
json = "{}"
# create an instance of Workflow from a JSON string
workflow_instance = Workflow.from_json(json)
# print the JSON string representation of the object
print(Workflow.to_json())

# convert the object into a dict
workflow_dict = workflow_instance.to_dict()
# create an instance of Workflow from a dict
workflow_from_dict = Workflow.from_dict(workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


