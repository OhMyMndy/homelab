# WebhookOrganizationMemberRemoved


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**membership** | [**WebhooksMembership**](WebhooksMembership.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_organization_member_removed import WebhookOrganizationMemberRemoved

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOrganizationMemberRemoved from a JSON string
webhook_organization_member_removed_instance = WebhookOrganizationMemberRemoved.from_json(json)
# print the JSON string representation of the object
print(WebhookOrganizationMemberRemoved.to_json())

# convert the object into a dict
webhook_organization_member_removed_dict = webhook_organization_member_removed_instance.to_dict()
# create an instance of WebhookOrganizationMemberRemoved from a dict
webhook_organization_member_removed_from_dict = WebhookOrganizationMemberRemoved.from_dict(webhook_organization_member_removed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


