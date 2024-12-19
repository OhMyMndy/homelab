# WebhookBranchProtectionConfigurationDisabled


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
from github_openapi.models.webhook_branch_protection_configuration_disabled import WebhookBranchProtectionConfigurationDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookBranchProtectionConfigurationDisabled from a JSON string
webhook_branch_protection_configuration_disabled_instance = WebhookBranchProtectionConfigurationDisabled.from_json(json)
# print the JSON string representation of the object
print(WebhookBranchProtectionConfigurationDisabled.to_json())

# convert the object into a dict
webhook_branch_protection_configuration_disabled_dict = webhook_branch_protection_configuration_disabled_instance.to_dict()
# create an instance of WebhookBranchProtectionConfigurationDisabled from a dict
webhook_branch_protection_configuration_disabled_from_dict = WebhookBranchProtectionConfigurationDisabled.from_dict(webhook_branch_protection_configuration_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


