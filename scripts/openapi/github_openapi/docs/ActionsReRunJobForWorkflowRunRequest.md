# ActionsReRunJobForWorkflowRunRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_debug_logging** | **bool** | Whether to enable debug logging for the re-run. | [optional] [default to False]

## Example

```python
from github_openapi.models.actions_re_run_job_for_workflow_run_request import ActionsReRunJobForWorkflowRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsReRunJobForWorkflowRunRequest from a JSON string
actions_re_run_job_for_workflow_run_request_instance = ActionsReRunJobForWorkflowRunRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsReRunJobForWorkflowRunRequest.to_json())

# convert the object into a dict
actions_re_run_job_for_workflow_run_request_dict = actions_re_run_job_for_workflow_run_request_instance.to_dict()
# create an instance of ActionsReRunJobForWorkflowRunRequest from a dict
actions_re_run_job_for_workflow_run_request_from_dict = ActionsReRunJobForWorkflowRunRequest.from_dict(actions_re_run_job_for_workflow_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


