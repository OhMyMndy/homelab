# WebhookOrganizationMemberAdded


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
from github_openapi.models.webhook_organization_member_added import WebhookOrganizationMemberAdded

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOrganizationMemberAdded from a JSON string
webhook_organization_member_added_instance = WebhookOrganizationMemberAdded.from_json(json)
# print the JSON string representation of the object
print(WebhookOrganizationMemberAdded.to_json())

# convert the object into a dict
webhook_organization_member_added_dict = webhook_organization_member_added_instance.to_dict()
# create an instance of WebhookOrganizationMemberAdded from a dict
webhook_organization_member_added_from_dict = WebhookOrganizationMemberAdded.from_dict(webhook_organization_member_added_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


