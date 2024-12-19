# WebhookOrganizationRenamed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookOrganizationRenamedChanges**](WebhookOrganizationRenamedChanges.md) |  | [optional] 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**membership** | [**WebhooksMembership**](WebhooksMembership.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_organization_renamed import WebhookOrganizationRenamed

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOrganizationRenamed from a JSON string
webhook_organization_renamed_instance = WebhookOrganizationRenamed.from_json(json)
# print the JSON string representation of the object
print(WebhookOrganizationRenamed.to_json())

# convert the object into a dict
webhook_organization_renamed_dict = webhook_organization_renamed_instance.to_dict()
# create an instance of WebhookOrganizationRenamed from a dict
webhook_organization_renamed_from_dict = WebhookOrganizationRenamed.from_dict(webhook_organization_renamed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


