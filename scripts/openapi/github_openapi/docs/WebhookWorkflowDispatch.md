# WebhookWorkflowDispatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**inputs** | **Dict[str, object]** |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**ref** | **str** |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**workflow** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_workflow_dispatch import WebhookWorkflowDispatch

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookWorkflowDispatch from a JSON string
webhook_workflow_dispatch_instance = WebhookWorkflowDispatch.from_json(json)
# print the JSON string representation of the object
print(WebhookWorkflowDispatch.to_json())

# convert the object into a dict
webhook_workflow_dispatch_dict = webhook_workflow_dispatch_instance.to_dict()
# create an instance of WebhookWorkflowDispatch from a dict
webhook_workflow_dispatch_from_dict = WebhookWorkflowDispatch.from_dict(webhook_workflow_dispatch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


