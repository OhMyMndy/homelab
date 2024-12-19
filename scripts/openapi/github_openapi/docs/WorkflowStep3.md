# WorkflowStep3


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
from github_openapi.models.workflow_step3 import WorkflowStep3

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStep3 from a JSON string
workflow_step3_instance = WorkflowStep3.from_json(json)
# print the JSON string representation of the object
print(WorkflowStep3.to_json())

# convert the object into a dict
workflow_step3_dict = workflow_step3_instance.to_dict()
# create an instance of WorkflowStep3 from a dict
workflow_step3_from_dict = WorkflowStep3.from_dict(workflow_step3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


