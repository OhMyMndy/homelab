# WebhookWatchStarted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_watch_started import WebhookWatchStarted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookWatchStarted from a JSON string
webhook_watch_started_instance = WebhookWatchStarted.from_json(json)
# print the JSON string representation of the object
print(WebhookWatchStarted.to_json())

# convert the object into a dict
webhook_watch_started_dict = webhook_watch_started_instance.to_dict()
# create an instance of WebhookWatchStarted from a dict
webhook_watch_started_from_dict = WebhookWatchStarted.from_dict(webhook_watch_started_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


