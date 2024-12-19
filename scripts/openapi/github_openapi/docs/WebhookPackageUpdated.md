# WebhookPackageUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**package** | [**WebhookPackageUpdatedPackage**](WebhookPackageUpdatedPackage.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_package_updated import WebhookPackageUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPackageUpdated from a JSON string
webhook_package_updated_instance = WebhookPackageUpdated.from_json(json)
# print the JSON string representation of the object
print(WebhookPackageUpdated.to_json())

# convert the object into a dict
webhook_package_updated_dict = webhook_package_updated_instance.to_dict()
# create an instance of WebhookPackageUpdated from a dict
webhook_package_updated_from_dict = WebhookPackageUpdated.from_dict(webhook_package_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


