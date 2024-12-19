# WebhookInstallationTargetRenamed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**WebhookInstallationTargetRenamedAccount**](WebhookInstallationTargetRenamedAccount.md) |  | 
**action** | **str** |  | 
**changes** | [**WebhookInstallationTargetRenamedChanges**](WebhookInstallationTargetRenamedChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**target_type** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_installation_target_renamed import WebhookInstallationTargetRenamed

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookInstallationTargetRenamed from a JSON string
webhook_installation_target_renamed_instance = WebhookInstallationTargetRenamed.from_json(json)
# print the JSON string representation of the object
print(WebhookInstallationTargetRenamed.to_json())

# convert the object into a dict
webhook_installation_target_renamed_dict = webhook_installation_target_renamed_instance.to_dict()
# create an instance of WebhookInstallationTargetRenamed from a dict
webhook_installation_target_renamed_from_dict = WebhookInstallationTargetRenamed.from_dict(webhook_installation_target_renamed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


