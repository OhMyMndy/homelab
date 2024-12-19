# WebhookBranchProtectionRuleDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**rule** | [**WebhooksRule**](WebhooksRule.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_branch_protection_rule_deleted import WebhookBranchProtectionRuleDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookBranchProtectionRuleDeleted from a JSON string
webhook_branch_protection_rule_deleted_instance = WebhookBranchProtectionRuleDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookBranchProtectionRuleDeleted.to_json())

# convert the object into a dict
webhook_branch_protection_rule_deleted_dict = webhook_branch_protection_rule_deleted_instance.to_dict()
# create an instance of WebhookBranchProtectionRuleDeleted from a dict
webhook_branch_protection_rule_deleted_from_dict = WebhookBranchProtectionRuleDeleted.from_dict(webhook_branch_protection_rule_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


