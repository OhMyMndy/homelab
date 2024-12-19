# WebhookOrganizationMemberInvited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**invitation** | [**WebhookOrganizationMemberInvitedInvitation**](WebhookOrganizationMemberInvitedInvitation.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**user** | [**WebhooksUser**](WebhooksUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_organization_member_invited import WebhookOrganizationMemberInvited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOrganizationMemberInvited from a JSON string
webhook_organization_member_invited_instance = WebhookOrganizationMemberInvited.from_json(json)
# print the JSON string representation of the object
print(WebhookOrganizationMemberInvited.to_json())

# convert the object into a dict
webhook_organization_member_invited_dict = webhook_organization_member_invited_instance.to_dict()
# create an instance of WebhookOrganizationMemberInvited from a dict
webhook_organization_member_invited_from_dict = WebhookOrganizationMemberInvited.from_dict(webhook_organization_member_invited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


