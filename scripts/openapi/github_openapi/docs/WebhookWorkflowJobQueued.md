# WebhookWorkflowJobQueued


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**workflow_job** | [**WebhookWorkflowJobQueuedWorkflowJob**](WebhookWorkflowJobQueuedWorkflowJob.md) |  | 
**deployment** | [**Deployment**](Deployment.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_workflow_job_queued import WebhookWorkflowJobQueued

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookWorkflowJobQueued from a JSON string
webhook_workflow_job_queued_instance = WebhookWorkflowJobQueued.from_json(json)
# print the JSON string representation of the object
print(WebhookWorkflowJobQueued.to_json())

# convert the object into a dict
webhook_workflow_job_queued_dict = webhook_workflow_job_queued_instance.to_dict()
# create an instance of WebhookWorkflowJobQueued from a dict
webhook_workflow_job_queued_from_dict = WebhookWorkflowJobQueued.from_dict(webhook_workflow_job_queued_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


