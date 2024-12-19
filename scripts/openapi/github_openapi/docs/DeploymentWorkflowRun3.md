# DeploymentWorkflowRun3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**User2**](User2.md) |  | 
**artifacts_url** | **str** |  | [optional] 
**cancel_url** | **str** |  | [optional] 
**check_suite_id** | **int** |  | 
**check_suite_node_id** | **str** |  | 
**check_suite_url** | **str** |  | [optional] 
**conclusion** | **str** |  | 
**created_at** | **datetime** |  | 
**event** | **str** |  | 
**head_branch** | **str** |  | 
**head_commit** | **object** |  | [optional] 
**head_repository** | [**DeploymentWorkflowRun1HeadRepository**](DeploymentWorkflowRun1HeadRepository.md) |  | [optional] 
**head_sha** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**jobs_url** | **str** |  | [optional] 
**logs_url** | **str** |  | [optional] 
**name** | **str** |  | 
**node_id** | **str** |  | 
**path** | **str** |  | 
**previous_attempt_url** | **str** |  | [optional] 
**pull_requests** | [**List[CheckRunPullRequest]**](CheckRunPullRequest.md) |  | 
**referenced_workflows** | [**List[DeploymentWorkflowRunReferencedWorkflowsInner]**](DeploymentWorkflowRunReferencedWorkflowsInner.md) |  | [optional] 
**repository** | [**DeploymentWorkflowRun1HeadRepository**](DeploymentWorkflowRun1HeadRepository.md) |  | [optional] 
**rerun_url** | **str** |  | [optional] 
**run_attempt** | **int** |  | 
**run_number** | **int** |  | 
**run_started_at** | **datetime** |  | 
**status** | **str** |  | 
**triggering_actor** | [**User2**](User2.md) |  | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 
**workflow_id** | **int** |  | 
**workflow_url** | **str** |  | [optional] 
**display_title** | **str** |  | 

## Example

```python
from github_openapi.models.deployment_workflow_run3 import DeploymentWorkflowRun3

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentWorkflowRun3 from a JSON string
deployment_workflow_run3_instance = DeploymentWorkflowRun3.from_json(json)
# print the JSON string representation of the object
print(DeploymentWorkflowRun3.to_json())

# convert the object into a dict
deployment_workflow_run3_dict = deployment_workflow_run3_instance.to_dict()
# create an instance of DeploymentWorkflowRun3 from a dict
deployment_workflow_run3_from_dict = DeploymentWorkflowRun3.from_dict(deployment_workflow_run3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


