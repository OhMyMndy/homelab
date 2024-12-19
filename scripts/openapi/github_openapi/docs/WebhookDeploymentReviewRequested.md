# WebhookDeploymentReviewRequested


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**environment** | **str** |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**requestor** | [**WebhooksUser**](WebhooksUser.md) |  | 
**reviewers** | [**List[WebhookDeploymentReviewRequestedReviewersInner]**](WebhookDeploymentReviewRequestedReviewersInner.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**since** | **str** |  | 
**workflow_job_run** | [**WebhookDeploymentReviewRequestedWorkflowJobRun**](WebhookDeploymentReviewRequestedWorkflowJobRun.md) |  | 
**workflow_run** | [**DeploymentWorkflowRun3**](DeploymentWorkflowRun3.md) |  | 

## Example

```python
from github_openapi.models.webhook_deployment_review_requested import WebhookDeploymentReviewRequested

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeploymentReviewRequested from a JSON string
webhook_deployment_review_requested_instance = WebhookDeploymentReviewRequested.from_json(json)
# print the JSON string representation of the object
print(WebhookDeploymentReviewRequested.to_json())

# convert the object into a dict
webhook_deployment_review_requested_dict = webhook_deployment_review_requested_instance.to_dict()
# create an instance of WebhookDeploymentReviewRequested from a dict
webhook_deployment_review_requested_from_dict = WebhookDeploymentReviewRequested.from_dict(webhook_deployment_review_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


