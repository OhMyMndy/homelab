# WebhookProjectColumnCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**project_column** | [**WebhooksProjectColumn**](WebhooksProjectColumn.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_project_column_created import WebhookProjectColumnCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectColumnCreated from a JSON string
webhook_project_column_created_instance = WebhookProjectColumnCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectColumnCreated.to_json())

# convert the object into a dict
webhook_project_column_created_dict = webhook_project_column_created_instance.to_dict()
# create an instance of WebhookProjectColumnCreated from a dict
webhook_project_column_created_from_dict = WebhookProjectColumnCreated.from_dict(webhook_project_column_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


