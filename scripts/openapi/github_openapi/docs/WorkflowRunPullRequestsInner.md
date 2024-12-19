# WorkflowRunPullRequestsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | [**CheckRunPullRequestBase**](CheckRunPullRequestBase.md) |  | 
**head** | [**CheckRunPullRequestBase**](CheckRunPullRequestBase.md) |  | 
**id** | **float** |  | 
**number** | **float** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.workflow_run_pull_requests_inner import WorkflowRunPullRequestsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRunPullRequestsInner from a JSON string
workflow_run_pull_requests_inner_instance = WorkflowRunPullRequestsInner.from_json(json)
# print the JSON string representation of the object
print(WorkflowRunPullRequestsInner.to_json())

# convert the object into a dict
workflow_run_pull_requests_inner_dict = workflow_run_pull_requests_inner_instance.to_dict()
# create an instance of WorkflowRunPullRequestsInner from a dict
workflow_run_pull_requests_inner_from_dict = WorkflowRunPullRequestsInner.from_dict(workflow_run_pull_requests_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


