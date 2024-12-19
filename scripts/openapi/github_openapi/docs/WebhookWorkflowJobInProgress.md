# WebhookWorkflowJobInProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**workflow_job** | [**WebhookWorkflowJobInProgressWorkflowJob**](WebhookWorkflowJobInProgressWorkflowJob.md) |  | 
**deployment** | [**Deployment**](Deployment.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_workflow_job_in_progress import WebhookWorkflowJobInProgress

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookWorkflowJobInProgress from a JSON string
webhook_workflow_job_in_progress_instance = WebhookWorkflowJobInProgress.from_json(json)
# print the JSON string representation of the object
print(WebhookWorkflowJobInProgress.to_json())

# convert the object into a dict
webhook_workflow_job_in_progress_dict = webhook_workflow_job_in_progress_instance.to_dict()
# create an instance of WebhookWorkflowJobInProgress from a dict
webhook_workflow_job_in_progress_from_dict = WebhookWorkflowJobInProgress.from_dict(webhook_workflow_job_in_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


