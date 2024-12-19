# WebhookWorkflowJobInProgressWorkflowJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_run_url** | **str** |  | 
**completed_at** | **str** |  | 
**conclusion** | **str** |  | 
**created_at** | **str** | The time that the job created. | 
**head_sha** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**labels** | **List[str]** |  | 
**name** | **str** |  | 
**node_id** | **str** |  | 
**run_attempt** | **int** |  | 
**run_id** | **int** |  | 
**run_url** | **str** |  | 
**runner_group_id** | **float** |  | 
**runner_group_name** | **str** |  | 
**runner_id** | **float** |  | 
**runner_name** | **str** |  | 
**started_at** | **str** |  | 
**status** | **str** |  | 
**head_branch** | **str** | The name of the current branch. | 
**workflow_name** | **str** | The name of the workflow. | 
**steps** | [**List[WorkflowStep2]**](WorkflowStep2.md) |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_workflow_job_in_progress_workflow_job import WebhookWorkflowJobInProgressWorkflowJob

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookWorkflowJobInProgressWorkflowJob from a JSON string
webhook_workflow_job_in_progress_workflow_job_instance = WebhookWorkflowJobInProgressWorkflowJob.from_json(json)
# print the JSON string representation of the object
print(WebhookWorkflowJobInProgressWorkflowJob.to_json())

# convert the object into a dict
webhook_workflow_job_in_progress_workflow_job_dict = webhook_workflow_job_in_progress_workflow_job_instance.to_dict()
# create an instance of WebhookWorkflowJobInProgressWorkflowJob from a dict
webhook_workflow_job_in_progress_workflow_job_from_dict = WebhookWorkflowJobInProgressWorkflowJob.from_dict(webhook_workflow_job_in_progress_workflow_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


