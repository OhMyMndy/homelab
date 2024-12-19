# WebhookProjectCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**project** | [**WebhooksProject**](WebhooksProject.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_project_created import WebhookProjectCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectCreated from a JSON string
webhook_project_created_instance = WebhookProjectCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectCreated.to_json())

# convert the object into a dict
webhook_project_created_dict = webhook_project_created_instance.to_dict()
# create an instance of WebhookProjectCreated from a dict
webhook_project_created_from_dict = WebhookProjectCreated.from_dict(webhook_project_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


