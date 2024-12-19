# WebhookPing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hook** | [**Webhook**](Webhook.md) |  | [optional] 
**hook_id** | **int** | The ID of the webhook that triggered the ping. | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**zen** | **str** | Random string of GitHub zen. | [optional] 

## Example

```python
from github_openapi.models.webhook_ping import WebhookPing

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPing from a JSON string
webhook_ping_instance = WebhookPing.from_json(json)
# print the JSON string representation of the object
print(WebhookPing.to_json())

# convert the object into a dict
webhook_ping_dict = webhook_ping_instance.to_dict()
# create an instance of WebhookPing from a dict
webhook_ping_from_dict = WebhookPing.from_dict(webhook_ping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


