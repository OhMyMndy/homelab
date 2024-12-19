# WebhookReleaseUnpublished


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**release** | [**WebhooksRelease1**](WebhooksRelease1.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_release_unpublished import WebhookReleaseUnpublished

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookReleaseUnpublished from a JSON string
webhook_release_unpublished_instance = WebhookReleaseUnpublished.from_json(json)
# print the JSON string representation of the object
print(WebhookReleaseUnpublished.to_json())

# convert the object into a dict
webhook_release_unpublished_dict = webhook_release_unpublished_instance.to_dict()
# create an instance of WebhookReleaseUnpublished from a dict
webhook_release_unpublished_from_dict = WebhookReleaseUnpublished.from_dict(webhook_release_unpublished_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


