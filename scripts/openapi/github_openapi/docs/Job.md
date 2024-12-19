# Job

Information of a job execution in a workflow run

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the job. | 
**run_id** | **int** | The id of the associated workflow run. | 
**run_url** | **str** |  | 
**run_attempt** | **int** | Attempt number of the associated workflow run, 1 for first attempt and higher if the workflow was re-run. | [optional] 
**node_id** | **str** |  | 
**head_sha** | **str** | The SHA of the commit that is being run. | 
**url** | **str** |  | 
**html_url** | **str** |  | 
**status** | **str** | The phase of the lifecycle that the job is currently in. | 
**conclusion** | **str** | The outcome of the job. | 
**created_at** | **datetime** | The time that the job created, in ISO 8601 format. | 
**started_at** | **datetime** | The time that the job started, in ISO 8601 format. | 
**completed_at** | **datetime** | The time that the job finished, in ISO 8601 format. | 
**name** | **str** | The name of the job. | 
**steps** | [**List[JobStepsInner]**](JobStepsInner.md) | Steps in this job. | [optional] 
**check_run_url** | **str** |  | 
**labels** | **List[str]** | Labels for the workflow job. Specified by the \&quot;runs_on\&quot; attribute in the action&#39;s workflow file. | 
**runner_id** | **int** | The ID of the runner to which this job has been assigned. (If a runner hasn&#39;t yet been assigned, this will be null.) | 
**runner_name** | **str** | The name of the runner to which this job has been assigned. (If a runner hasn&#39;t yet been assigned, this will be null.) | 
**runner_group_id** | **int** | The ID of the runner group to which this job has been assigned. (If a runner hasn&#39;t yet been assigned, this will be null.) | 
**runner_group_name** | **str** | The name of the runner group to which this job has been assigned. (If a runner hasn&#39;t yet been assigned, this will be null.) | 
**workflow_name** | **str** | The name of the workflow. | 
**head_branch** | **str** | The name of the current branch. | 

## Example

```python
from github_openapi.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_from_dict = Job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


