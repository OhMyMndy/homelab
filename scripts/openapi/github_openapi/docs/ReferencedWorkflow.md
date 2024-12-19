# ReferencedWorkflow

A workflow referenced/reused by the initial caller workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**sha** | **str** |  | 
**ref** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.referenced_workflow import ReferencedWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedWorkflow from a JSON string
referenced_workflow_instance = ReferencedWorkflow.from_json(json)
# print the JSON string representation of the object
print(ReferencedWorkflow.to_json())

# convert the object into a dict
referenced_workflow_dict = referenced_workflow_instance.to_dict()
# create an instance of ReferencedWorkflow from a dict
referenced_workflow_from_dict = ReferencedWorkflow.from_dict(referenced_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


