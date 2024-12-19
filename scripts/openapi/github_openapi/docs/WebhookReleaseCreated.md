# WebhookReleaseCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**release** | [**WebhooksRelease**](WebhooksRelease.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_release_created import WebhookReleaseCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookReleaseCreated from a JSON string
webhook_release_created_instance = WebhookReleaseCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookReleaseCreated.to_json())

# convert the object into a dict
webhook_release_created_dict = webhook_release_created_instance.to_dict()
# create an instance of WebhookReleaseCreated from a dict
webhook_release_created_from_dict = WebhookReleaseCreated.from_dict(webhook_release_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


