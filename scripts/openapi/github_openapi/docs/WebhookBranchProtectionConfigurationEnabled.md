# WebhookBranchProtectionConfigurationEnabled


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
from github_openapi.models.webhook_branch_protection_configuration_enabled import WebhookBranchProtectionConfigurationEnabled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookBranchProtectionConfigurationEnabled from a JSON string
webhook_branch_protection_configuration_enabled_instance = WebhookBranchProtectionConfigurationEnabled.from_json(json)
# print the JSON string representation of the object
print(WebhookBranchProtectionConfigurationEnabled.to_json())

# convert the object into a dict
webhook_branch_protection_configuration_enabled_dict = webhook_branch_protection_configuration_enabled_instance.to_dict()
# create an instance of WebhookBranchProtectionConfigurationEnabled from a dict
webhook_branch_protection_configuration_enabled_from_dict = WebhookBranchProtectionConfigurationEnabled.from_dict(webhook_branch_protection_configuration_enabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


