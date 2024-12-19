# WebhookProjectColumnMoved


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**project_column** | [**WebhooksProjectColumn**](WebhooksProjectColumn.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_project_column_moved import WebhookProjectColumnMoved

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectColumnMoved from a JSON string
webhook_project_column_moved_instance = WebhookProjectColumnMoved.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectColumnMoved.to_json())

# convert the object into a dict
webhook_project_column_moved_dict = webhook_project_column_moved_instance.to_dict()
# create an instance of WebhookProjectColumnMoved from a dict
webhook_project_column_moved_from_dict = WebhookProjectColumnMoved.from_dict(webhook_project_column_moved_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


