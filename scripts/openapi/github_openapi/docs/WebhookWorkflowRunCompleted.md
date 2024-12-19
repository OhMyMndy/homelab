# WebhookWorkflowRunCompleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**workflow** | [**WebhooksWorkflow**](WebhooksWorkflow.md) |  | 
**workflow_run** | [**WorkflowRun**](WorkflowRun.md) |  | 

## Example

```python
from github_openapi.models.webhook_workflow_run_completed import WebhookWorkflowRunCompleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookWorkflowRunCompleted from a JSON string
webhook_workflow_run_completed_instance = WebhookWorkflowRunCompleted.from_json(json)
# print the JSON string representation of the object
print(WebhookWorkflowRunCompleted.to_json())

# convert the object into a dict
webhook_workflow_run_completed_dict = webhook_workflow_run_completed_instance.to_dict()
# create an instance of WebhookWorkflowRunCompleted from a dict
webhook_workflow_run_completed_from_dict = WebhookWorkflowRunCompleted.from_dict(webhook_workflow_run_completed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


