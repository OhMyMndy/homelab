# WebhookOrganizationDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**membership** | [**WebhooksMembership**](WebhooksMembership.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_organization_deleted import WebhookOrganizationDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOrganizationDeleted from a JSON string
webhook_organization_deleted_instance = WebhookOrganizationDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookOrganizationDeleted.to_json())

# convert the object into a dict
webhook_organization_deleted_dict = webhook_organization_deleted_instance.to_dict()
# create an instance of WebhookOrganizationDeleted from a dict
webhook_organization_deleted_from_dict = WebhookOrganizationDeleted.from_dict(webhook_organization_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


