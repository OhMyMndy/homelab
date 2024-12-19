# WebhookWorkflowRunRequested


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
**workflow_run** | [**WorkflowRun2**](WorkflowRun2.md) |  | 

## Example

```python
from github_openapi.models.webhook_workflow_run_requested import WebhookWorkflowRunRequested

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookWorkflowRunRequested from a JSON string
webhook_workflow_run_requested_instance = WebhookWorkflowRunRequested.from_json(json)
# print the JSON string representation of the object
print(WebhookWorkflowRunRequested.to_json())

# convert the object into a dict
webhook_workflow_run_requested_dict = webhook_workflow_run_requested_instance.to_dict()
# create an instance of WebhookWorkflowRunRequested from a dict
webhook_workflow_run_requested_from_dict = WebhookWorkflowRunRequested.from_dict(webhook_workflow_run_requested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


