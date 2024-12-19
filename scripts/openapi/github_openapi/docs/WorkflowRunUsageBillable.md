# WorkflowRunUsageBillable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ubuntu** | [**WorkflowRunUsageBillableUBUNTU**](WorkflowRunUsageBillableUBUNTU.md) |  | [optional] 
**macos** | [**WorkflowRunUsageBillableUBUNTU**](WorkflowRunUsageBillableUBUNTU.md) |  | [optional] 
**windows** | [**WorkflowRunUsageBillableUBUNTU**](WorkflowRunUsageBillableUBUNTU.md) |  | [optional] 

## Example

```python
from github_openapi.models.workflow_run_usage_billable import WorkflowRunUsageBillable

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRunUsageBillable from a JSON string
workflow_run_usage_billable_instance = WorkflowRunUsageBillable.from_json(json)
# print the JSON string representation of the object
print(WorkflowRunUsageBillable.to_json())

# convert the object into a dict
workflow_run_usage_billable_dict = workflow_run_usage_billable_instance.to_dict()
# create an instance of WorkflowRunUsageBillable from a dict
workflow_run_usage_billable_from_dict = WorkflowRunUsageBillable.from_dict(workflow_run_usage_billable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


