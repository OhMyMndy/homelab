# WebhookRepositoryAdvisoryPublished


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**repository_advisory** | [**RepositoryAdvisory**](RepositoryAdvisory.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_repository_advisory_published import WebhookRepositoryAdvisoryPublished

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRepositoryAdvisoryPublished from a JSON string
webhook_repository_advisory_published_instance = WebhookRepositoryAdvisoryPublished.from_json(json)
# print the JSON string representation of the object
print(WebhookRepositoryAdvisoryPublished.to_json())

# convert the object into a dict
webhook_repository_advisory_published_dict = webhook_repository_advisory_published_instance.to_dict()
# create an instance of WebhookRepositoryAdvisoryPublished from a dict
webhook_repository_advisory_published_from_dict = WebhookRepositoryAdvisoryPublished.from_dict(webhook_repository_advisory_published_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


