# WorkflowRunUsage

Workflow Run Usage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable** | [**WorkflowRunUsageBillable**](WorkflowRunUsageBillable.md) |  | 
**run_duration_ms** | **int** |  | [optional] 

## Example

```python
from github_openapi.models.workflow_run_usage import WorkflowRunUsage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRunUsage from a JSON string
workflow_run_usage_instance = WorkflowRunUsage.from_json(json)
# print the JSON string representation of the object
print(WorkflowRunUsage.to_json())

# convert the object into a dict
workflow_run_usage_dict = workflow_run_usage_instance.to_dict()
# create an instance of WorkflowRunUsage from a dict
workflow_run_usage_from_dict = WorkflowRunUsage.from_dict(workflow_run_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


