# WorkflowUsageBillable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ubuntu** | [**WorkflowUsageBillableUBUNTU**](WorkflowUsageBillableUBUNTU.md) |  | [optional] 
**macos** | [**WorkflowUsageBillableUBUNTU**](WorkflowUsageBillableUBUNTU.md) |  | [optional] 
**windows** | [**WorkflowUsageBillableUBUNTU**](WorkflowUsageBillableUBUNTU.md) |  | [optional] 

## Example

```python
from github_openapi.models.workflow_usage_billable import WorkflowUsageBillable

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowUsageBillable from a JSON string
workflow_usage_billable_instance = WorkflowUsageBillable.from_json(json)
# print the JSON string representation of the object
print(WorkflowUsageBillable.to_json())

# convert the object into a dict
workflow_usage_billable_dict = workflow_usage_billable_instance.to_dict()
# create an instance of WorkflowUsageBillable from a dict
workflow_usage_billable_from_dict = WorkflowUsageBillable.from_dict(workflow_usage_billable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


