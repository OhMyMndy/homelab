# WebhookDeploymentReviewApproved


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
**workflow_job_runs** | [**List[WebhookDeploymentReviewApprovedWorkflowJobRunsInner]**](WebhookDeploymentReviewApprovedWorkflowJobRunsInner.md) |  | [optional] 
**workflow_run** | [**DeploymentWorkflowRun1**](DeploymentWorkflowRun1.md) |  | 

## Example

```python
from github_openapi.models.webhook_deployment_review_approved import WebhookDeploymentReviewApproved

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeploymentReviewApproved from a JSON string
webhook_deployment_review_approved_instance = WebhookDeploymentReviewApproved.from_json(json)
# print the JSON string representation of the object
print(WebhookDeploymentReviewApproved.to_json())

# convert the object into a dict
webhook_deployment_review_approved_dict = webhook_deployment_review_approved_instance.to_dict()
# create an instance of WebhookDeploymentReviewApproved from a dict
webhook_deployment_review_approved_from_dict = WebhookDeploymentReviewApproved.from_dict(webhook_deployment_review_approved_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


