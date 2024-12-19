# WebhookWorkflowJobCompleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**workflow_job** | [**WebhookWorkflowJobCompletedWorkflowJob**](WebhookWorkflowJobCompletedWorkflowJob.md) |  | 
**deployment** | [**Deployment**](Deployment.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_workflow_job_completed import WebhookWorkflowJobCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookWorkflowJobCompleted from a JSON string
webhook_workflow_job_completed_instance = WebhookWorkflowJobCompleted.from_json(json)
# print the JSON string representation of the object
print(WebhookWorkflowJobCompleted.to_json())

# convert the object into a dict
webhook_workflow_job_completed_dict = webhook_workflow_job_completed_instance.to_dict()
# create an instance of WebhookWorkflowJobCompleted from a dict
webhook_workflow_job_completed_from_dict = WebhookWorkflowJobCompleted.from_dict(webhook_workflow_job_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


