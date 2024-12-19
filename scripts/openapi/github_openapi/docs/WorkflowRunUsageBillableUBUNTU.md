# WorkflowRunUsageBillableUBUNTU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_ms** | **int** |  | 
**jobs** | **int** |  | 
**job_runs** | [**List[WorkflowRunUsageBillableUBUNTUJobRunsInner]**](WorkflowRunUsageBillableUBUNTUJobRunsInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.workflow_run_usage_billable_ubuntu import WorkflowRunUsageBillableUBUNTU

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRunUsageBillableUBUNTU from a JSON string
workflow_run_usage_billable_ubuntu_instance = WorkflowRunUsageBillableUBUNTU.from_json(json)
# print the JSON string representation of the object
print(WorkflowRunUsageBillableUBUNTU.to_json())

# convert the object into a dict
workflow_run_usage_billable_ubuntu_dict = workflow_run_usage_billable_ubuntu_instance.to_dict()
# create an instance of WorkflowRunUsageBillableUBUNTU from a dict
workflow_run_usage_billable_ubuntu_from_dict = WorkflowRunUsageBillableUBUNTU.from_dict(workflow_run_usage_billable_ubuntu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


