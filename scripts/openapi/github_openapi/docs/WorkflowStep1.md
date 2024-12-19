# WorkflowStep1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **str** |  | 
**conclusion** | **str** |  | 
**name** | **str** |  | 
**number** | **int** |  | 
**started_at** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from github_openapi.models.workflow_step1 import WorkflowStep1

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStep1 from a JSON string
workflow_step1_instance = WorkflowStep1.from_json(json)
# print the JSON string representation of the object
print(WorkflowStep1.to_json())

# convert the object into a dict
workflow_step1_dict = workflow_step1_instance.to_dict()
# create an instance of WorkflowStep1 from a dict
workflow_step1_from_dict = WorkflowStep1.from_dict(workflow_step1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


