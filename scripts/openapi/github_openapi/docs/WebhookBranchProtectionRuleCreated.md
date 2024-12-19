# WebhookBranchProtectionRuleCreated


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
from github_openapi.models.webhook_branch_protection_rule_created import WebhookBranchProtectionRuleCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookBranchProtectionRuleCreated from a JSON string
webhook_branch_protection_rule_created_instance = WebhookBranchProtectionRuleCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookBranchProtectionRuleCreated.to_json())

# convert the object into a dict
webhook_branch_protection_rule_created_dict = webhook_branch_protection_rule_created_instance.to_dict()
# create an instance of WebhookBranchProtectionRuleCreated from a dict
webhook_branch_protection_rule_created_from_dict = WebhookBranchProtectionRuleCreated.from_dict(webhook_branch_protection_rule_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


