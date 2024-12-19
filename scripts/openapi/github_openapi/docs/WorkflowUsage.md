# WorkflowUsage

Workflow Usage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable** | [**WorkflowUsageBillable**](WorkflowUsageBillable.md) |  | 

## Example

```python
from github_openapi.models.workflow_usage import WorkflowUsage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowUsage from a JSON string
workflow_usage_instance = WorkflowUsage.from_json(json)
# print the JSON string representation of the object
print(WorkflowUsage.to_json())

# convert the object into a dict
workflow_usage_dict = workflow_usage_instance.to_dict()
# create an instance of WorkflowUsage from a dict
workflow_usage_from_dict = WorkflowUsage.from_dict(workflow_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


