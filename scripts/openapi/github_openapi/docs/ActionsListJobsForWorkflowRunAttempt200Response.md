# ActionsListJobsForWorkflowRunAttempt200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**jobs** | [**List[Job]**](Job.md) |  | 

## Example

```python
from github_openapi.models.actions_list_jobs_for_workflow_run_attempt200_response import ActionsListJobsForWorkflowRunAttempt200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsListJobsForWorkflowRunAttempt200Response from a JSON string
actions_list_jobs_for_workflow_run_attempt200_response_instance = ActionsListJobsForWorkflowRunAttempt200Response.from_json(json)
# print the JSON string representation of the object
print(ActionsListJobsForWorkflowRunAttempt200Response.to_json())

# convert the object into a dict
actions_list_jobs_for_workflow_run_attempt200_response_dict = actions_list_jobs_for_workflow_run_attempt200_response_instance.to_dict()
# create an instance of ActionsListJobsForWorkflowRunAttempt200Response from a dict
actions_list_jobs_for_workflow_run_attempt200_response_from_dict = ActionsListJobsForWorkflowRunAttempt200Response.from_dict(actions_list_jobs_for_workflow_run_attempt200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


