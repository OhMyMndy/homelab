# WorkflowRun1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**User**](User.md) |  | 
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
**head_repository** | [**RepositoryLite1**](RepositoryLite1.md) |  | 
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
**repository** | [**RepositoryLite2**](RepositoryLite2.md) |  | 
**rerun_url** | **str** |  | 
**run_attempt** | **int** |  | 
**run_number** | **int** |  | 
**run_started_at** | **datetime** |  | 
**status** | **str** |  | 
**triggering_actor** | [**User**](User.md) |  | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 
**workflow_id** | **int** |  | 
**workflow_url** | **str** |  | 

## Example

```python
from github_openapi.models.workflow_run1 import WorkflowRun1

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRun1 from a JSON string
workflow_run1_instance = WorkflowRun1.from_json(json)
# print the JSON string representation of the object
print(WorkflowRun1.to_json())

# convert the object into a dict
workflow_run1_dict = workflow_run1_instance.to_dict()
# create an instance of WorkflowRun1 from a dict
workflow_run1_from_dict = WorkflowRun1.from_dict(workflow_run1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


