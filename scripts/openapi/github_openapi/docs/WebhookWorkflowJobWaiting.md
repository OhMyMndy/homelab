# WebhookWorkflowJobWaiting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**workflow_job** | [**WebhookWorkflowJobWaitingWorkflowJob**](WebhookWorkflowJobWaitingWorkflowJob.md) |  | 
**deployment** | [**Deployment**](Deployment.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_workflow_job_waiting import WebhookWorkflowJobWaiting

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookWorkflowJobWaiting from a JSON string
webhook_workflow_job_waiting_instance = WebhookWorkflowJobWaiting.from_json(json)
# print the JSON string representation of the object
print(WebhookWorkflowJobWaiting.to_json())

# convert the object into a dict
webhook_workflow_job_waiting_dict = webhook_workflow_job_waiting_instance.to_dict()
# create an instance of WebhookWorkflowJobWaiting from a dict
webhook_workflow_job_waiting_from_dict = WebhookWorkflowJobWaiting.from_dict(webhook_workflow_job_waiting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


