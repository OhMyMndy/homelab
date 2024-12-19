# DeploymentWorkflowRunReferencedWorkflowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**ref** | **str** |  | [optional] 
**sha** | **str** |  | 

## Example

```python
from github_openapi.models.deployment_workflow_run_referenced_workflows_inner import DeploymentWorkflowRunReferencedWorkflowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentWorkflowRunReferencedWorkflowsInner from a JSON string
deployment_workflow_run_referenced_workflows_inner_instance = DeploymentWorkflowRunReferencedWorkflowsInner.from_json(json)
# print the JSON string representation of the object
print(DeploymentWorkflowRunReferencedWorkflowsInner.to_json())

# convert the object into a dict
deployment_workflow_run_referenced_workflows_inner_dict = deployment_workflow_run_referenced_workflows_inner_instance.to_dict()
# create an instance of DeploymentWorkflowRunReferencedWorkflowsInner from a dict
deployment_workflow_run_referenced_workflows_inner_from_dict = DeploymentWorkflowRunReferencedWorkflowsInner.from_dict(deployment_workflow_run_referenced_workflows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


