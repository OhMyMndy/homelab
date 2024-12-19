# WebhookDeploymentReviewRejected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**approver** | [**WebhooksApprover**](WebhooksApprover.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**reviewers** | [**List[WebhooksReviewersInner]**](WebhooksReviewersInner.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**since** | **str** |  | 
**workflow_job_run** | [**WebhooksWorkflowJobRun**](WebhooksWorkflowJobRun.md) |  | [optional] 
**workflow_job_runs** | [**List[WebhookDeploymentReviewRejectedWorkflowJobRunsInner]**](WebhookDeploymentReviewRejectedWorkflowJobRunsInner.md) |  | [optional] 
**workflow_run** | [**DeploymentWorkflowRun2**](DeploymentWorkflowRun2.md) |  | 

## Example

```python
from github_openapi.models.webhook_deployment_review_rejected import WebhookDeploymentReviewRejected

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeploymentReviewRejected from a JSON string
webhook_deployment_review_rejected_instance = WebhookDeploymentReviewRejected.from_json(json)
# print the JSON string representation of the object
print(WebhookDeploymentReviewRejected.to_json())

# convert the object into a dict
webhook_deployment_review_rejected_dict = webhook_deployment_review_rejected_instance.to_dict()
# create an instance of WebhookDeploymentReviewRejected from a dict
webhook_deployment_review_rejected_from_dict = WebhookDeploymentReviewRejected.from_dict(webhook_deployment_review_rejected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


