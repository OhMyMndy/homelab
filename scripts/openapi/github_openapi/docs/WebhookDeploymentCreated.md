# WebhookDeploymentCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**deployment** | [**Deployment**](Deployment.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**workflow** | [**WebhooksWorkflow**](WebhooksWorkflow.md) |  | 
**workflow_run** | [**DeploymentWorkflowRun**](DeploymentWorkflowRun.md) |  | 

## Example

```python
from github_openapi.models.webhook_deployment_created import WebhookDeploymentCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeploymentCreated from a JSON string
webhook_deployment_created_instance = WebhookDeploymentCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookDeploymentCreated.to_json())

# convert the object into a dict
webhook_deployment_created_dict = webhook_deployment_created_instance.to_dict()
# create an instance of WebhookDeploymentCreated from a dict
webhook_deployment_created_from_dict = WebhookDeploymentCreated.from_dict(webhook_deployment_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


