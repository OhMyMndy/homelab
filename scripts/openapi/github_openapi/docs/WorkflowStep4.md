# WorkflowStep4


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
from github_openapi.models.workflow_step4 import WorkflowStep4

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStep4 from a JSON string
workflow_step4_instance = WorkflowStep4.from_json(json)
# print the JSON string representation of the object
print(WorkflowStep4.to_json())

# convert the object into a dict
workflow_step4_dict = workflow_step4_instance.to_dict()
# create an instance of WorkflowStep4 from a dict
workflow_step4_from_dict = WorkflowStep4.from_dict(workflow_step4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


