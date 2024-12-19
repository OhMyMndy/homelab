# WorkflowRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**User2**](User2.md) |  | 
**artifacts_url** | **str** |  | 
**cancel_url** | **str** |  | 
**check_suite_id** | **int** |  | 
**check_suite_node_id** | **str** |  | 
**check_suite_url** | **str** |  | 
**conclusion** | **str** |  | 
**created_at** | **datetime** |  | 
**event** | **str** |  | 
**head_branch** | **str** |  | 
**head_commit** | [**SimpleCommit**](SimpleCommit.md) |  | 
**head_repository** | [**RepositoryLite**](RepositoryLite.md) |  | 
**head_sha** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**jobs_url** | **str** |  | 
**logs_url** | **str** |  | 
**name** | **str** |  | 
**node_id** | **str** |  | 
**path** | **str** |  | 
**previous_attempt_url** | **str** |  | 
**pull_requests** | [**List[WorkflowRunPullRequestsInner]**](WorkflowRunPullRequestsInner.md) |  | 
**referenced_workflows** | [**List[DeploymentWorkflowRunReferencedWorkflowsInner]**](DeploymentWorkflowRunReferencedWorkflowsInner.md) |  | [optional] 
**repository** | [**RepositoryLite**](RepositoryLite.md) |  | 
**rerun_url** | **str** |  | 
**run_attempt** | **int** |  | 
**run_number** | **int** |  | 
**run_started_at** | **datetime** |  | 
**status** | **str** |  | 
**triggering_actor** | [**User2**](User2.md) |  | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 
**workflow_id** | **int** |  | 
**workflow_url** | **str** |  | 
**display_title** | **str** | The event-specific title associated with the run or the run-name if set, or the value of &#x60;run-name&#x60; if it is set in the workflow. | [optional] 

## Example

```python
from github_openapi.models.workflow_run import WorkflowRun

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRun from a JSON string
workflow_run_instance = WorkflowRun.from_json(json)
# print the JSON string representation of the object
print(WorkflowRun.to_json())

# convert the object into a dict
workflow_run_dict = workflow_run_instance.to_dict()
# create an instance of WorkflowRun from a dict
workflow_run_from_dict = WorkflowRun.from_dict(workflow_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


