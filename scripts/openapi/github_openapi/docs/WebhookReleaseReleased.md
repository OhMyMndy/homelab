# WebhookReleaseReleased


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**release** | [**WebhooksRelease**](WebhooksRelease.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_release_released import WebhookReleaseReleased

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookReleaseReleased from a JSON string
webhook_release_released_instance = WebhookReleaseReleased.from_json(json)
# print the JSON string representation of the object
print(WebhookReleaseReleased.to_json())

# convert the object into a dict
webhook_release_released_dict = webhook_release_released_instance.to_dict()
# create an instance of WebhookReleaseReleased from a dict
webhook_release_released_from_dict = WebhookReleaseReleased.from_dict(webhook_release_released_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


