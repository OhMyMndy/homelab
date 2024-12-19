# WebhookPackagePublished


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**package** | [**WebhookPackagePublishedPackage**](WebhookPackagePublishedPackage.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_package_published import WebhookPackagePublished

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPackagePublished from a JSON string
webhook_package_published_instance = WebhookPackagePublished.from_json(json)
# print the JSON string representation of the object
print(WebhookPackagePublished.to_json())

# convert the object into a dict
webhook_package_published_dict = webhook_package_published_instance.to_dict()
# create an instance of WebhookPackagePublished from a dict
webhook_package_published_from_dict = WebhookPackagePublished.from_dict(webhook_package_published_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


