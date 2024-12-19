# WebhookMembershipRemoved


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**member** | [**WebhooksUser**](WebhooksUser.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**scope** | **str** | The scope of the membership. Currently, can only be &#x60;team&#x60;. | 
**sender** | [**User2**](User2.md) |  | 
**team** | [**WebhooksTeam**](WebhooksTeam.md) |  | 

## Example

```python
from github_openapi.models.webhook_membership_removed import WebhookMembershipRemoved

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMembershipRemoved from a JSON string
webhook_membership_removed_instance = WebhookMembershipRemoved.from_json(json)
# print the JSON string representation of the object
print(WebhookMembershipRemoved.to_json())

# convert the object into a dict
webhook_membership_removed_dict = webhook_membership_removed_instance.to_dict()
# create an instance of WebhookMembershipRemoved from a dict
webhook_membership_removed_from_dict = WebhookMembershipRemoved.from_dict(webhook_membership_removed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


