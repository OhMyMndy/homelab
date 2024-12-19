# WebhookDeploymentReviewApprovedWorkflowJobRunsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conclusion** | **object** |  | [optional] 
**created_at** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_deployment_review_approved_workflow_job_runs_inner import WebhookDeploymentReviewApprovedWorkflowJobRunsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeploymentReviewApprovedWorkflowJobRunsInner from a JSON string
webhook_deployment_review_approved_workflow_job_runs_inner_instance = WebhookDeploymentReviewApprovedWorkflowJobRunsInner.from_json(json)
# print the JSON string representation of the object
print(WebhookDeploymentReviewApprovedWorkflowJobRunsInner.to_json())

# convert the object into a dict
webhook_deployment_review_approved_workflow_job_runs_inner_dict = webhook_deployment_review_approved_workflow_job_runs_inner_instance.to_dict()
# create an instance of WebhookDeploymentReviewApprovedWorkflowJobRunsInner from a dict
webhook_deployment_review_approved_workflow_job_runs_inner_from_dict = WebhookDeploymentReviewApprovedWorkflowJobRunsInner.from_dict(webhook_deployment_review_approved_workflow_job_runs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


