# WebhookDeploymentReviewRequestedWorkflowJobRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conclusion** | **object** |  | 
**created_at** | **str** |  | 
**environment** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_deployment_review_requested_workflow_job_run import WebhookDeploymentReviewRequestedWorkflowJobRun

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeploymentReviewRequestedWorkflowJobRun from a JSON string
webhook_deployment_review_requested_workflow_job_run_instance = WebhookDeploymentReviewRequestedWorkflowJobRun.from_json(json)
# print the JSON string representation of the object
print(WebhookDeploymentReviewRequestedWorkflowJobRun.to_json())

# convert the object into a dict
webhook_deployment_review_requested_workflow_job_run_dict = webhook_deployment_review_requested_workflow_job_run_instance.to_dict()
# create an instance of WebhookDeploymentReviewRequestedWorkflowJobRun from a dict
webhook_deployment_review_requested_workflow_job_run_from_dict = WebhookDeploymentReviewRequestedWorkflowJobRun.from_dict(webhook_deployment_review_requested_workflow_job_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


