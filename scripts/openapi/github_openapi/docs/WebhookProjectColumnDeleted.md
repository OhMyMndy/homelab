# WebhookProjectColumnDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**project_column** | [**WebhooksProjectColumn**](WebhooksProjectColumn.md) |  | 
**repository** | [**NullableRepositoryWebhooks**](NullableRepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_project_column_deleted import WebhookProjectColumnDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectColumnDeleted from a JSON string
webhook_project_column_deleted_instance = WebhookProjectColumnDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectColumnDeleted.to_json())

# convert the object into a dict
webhook_project_column_deleted_dict = webhook_project_column_deleted_instance.to_dict()
# create an instance of WebhookProjectColumnDeleted from a dict
webhook_project_column_deleted_from_dict = WebhookProjectColumnDeleted.from_dict(webhook_project_column_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


