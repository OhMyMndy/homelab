# WorkflowRun2PullRequestsInner


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
from github_openapi.models.workflow_run2_pull_requests_inner import WorkflowRun2PullRequestsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRun2PullRequestsInner from a JSON string
workflow_run2_pull_requests_inner_instance = WorkflowRun2PullRequestsInner.from_json(json)
# print the JSON string representation of the object
print(WorkflowRun2PullRequestsInner.to_json())

# convert the object into a dict
workflow_run2_pull_requests_inner_dict = workflow_run2_pull_requests_inner_instance.to_dict()
# create an instance of WorkflowRun2PullRequestsInner from a dict
workflow_run2_pull_requests_inner_from_dict = WorkflowRun2PullRequestsInner.from_dict(workflow_run2_pull_requests_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


