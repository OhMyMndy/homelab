# WebhookRepositoryArchived


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_repository_archived import WebhookRepositoryArchived

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryArchived from a JSON string
webhook_repository_archived_instance = WebhookRepositoryArchived.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryArchived.to_json())

# convert the object into a dict
webhook_repository_archived_dict = webhook_repository_archived_instance.to_dict()
# create an instance of WebhookRepositoryArchived from a dict
webhook_repository_archived_from_dict = WebhookRepositoryArchived.from_dict(webhook_repository_archived_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


