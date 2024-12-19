# WebhookDeploymentReviewRejectedWorkflowJobRunsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conclusion** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_deployment_review_rejected_workflow_job_runs_inner import WebhookDeploymentReviewRejectedWorkflowJobRunsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeploymentReviewRejectedWorkflowJobRunsInner from a JSON string
webhook_deployment_review_rejected_workflow_job_runs_inner_instance = WebhookDeploymentReviewRejectedWorkflowJobRunsInner.from_json(json)
# print the JSON string representation of the object
print(WebhookDeploymentReviewRejectedWorkflowJobRunsInner.to_json())

# convert the object into a dict
webhook_deployment_review_rejected_workflow_job_runs_inner_dict = webhook_deployment_review_rejected_workflow_job_runs_inner_instance.to_dict()
# create an instance of WebhookDeploymentReviewRejectedWorkflowJobRunsInner from a dict
webhook_deployment_review_rejected_workflow_job_runs_inner_from_dict = WebhookDeploymentReviewRejectedWorkflowJobRunsInner.from_dict(webhook_deployment_review_rejected_workflow_job_runs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


