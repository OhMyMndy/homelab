# WebhookRepositoryImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**status** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_repository_import import WebhookRepositoryImport

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryImport from a JSON string
webhook_repository_import_instance = WebhookRepositoryImport.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryImport.to_json())

# convert the object into a dict
webhook_repository_import_dict = webhook_repository_import_instance.to_dict()
# create an instance of WebhookRepositoryImport from a dict
webhook_repository_import_from_dict = WebhookRepositoryImport.from_dict(webhook_repository_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


