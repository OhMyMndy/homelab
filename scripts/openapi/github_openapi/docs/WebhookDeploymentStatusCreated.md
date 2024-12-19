# WebhookDeploymentStatusCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**check_run** | [**WebhookDeploymentStatusCreatedCheckRun**](WebhookDeploymentStatusCreatedCheckRun.md) |  | [optional] 
**deployment** | [**Deployment1**](Deployment1.md) |  | 
**deployment_status** | [**WebhookDeploymentStatusCreatedDeploymentStatus**](WebhookDeploymentStatusCreatedDeploymentStatus.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**workflow** | [**WebhooksWorkflow**](WebhooksWorkflow.md) |  | [optional] 
**workflow_run** | [**DeploymentWorkflowRun4**](DeploymentWorkflowRun4.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_deployment_status_created import WebhookDeploymentStatusCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeploymentStatusCreated from a JSON string
webhook_deployment_status_created_instance = WebhookDeploymentStatusCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookDeploymentStatusCreated.to_json())

# convert the object into a dict
webhook_deployment_status_created_dict = webhook_deployment_status_created_instance.to_dict()
# create an instance of WebhookDeploymentStatusCreated from a dict
webhook_deployment_status_created_from_dict = WebhookDeploymentStatusCreated.from_dict(webhook_deployment_status_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


