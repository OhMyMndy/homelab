# WebhookRepositoryRenamed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookRepositoryRenamedChanges**](WebhookRepositoryRenamedChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_repository_renamed import WebhookRepositoryRenamed

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryRenamed from a JSON string
webhook_repository_renamed_instance = WebhookRepositoryRenamed.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryRenamed.to_json())

# convert the object into a dict
webhook_repository_renamed_dict = webhook_repository_renamed_instance.to_dict()
# create an instance of WebhookRepositoryRenamed from a dict
webhook_repository_renamed_from_dict = WebhookRepositoryRenamed.from_dict(webhook_repository_renamed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


