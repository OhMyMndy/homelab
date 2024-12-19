# Webhook

The webhook that is being pinged

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Determines whether the hook is actually triggered for the events it subscribes to. | 
**app_id** | **int** | Only included for GitHub Apps. When you register a new GitHub App, GitHub sends a ping event to the webhook URL you specified during registration. The GitHub App ID sent in this field is required for authenticating an app. | [optional] 
**config** | [**WebhookConfig**](WebhookConfig.md) |  | 
**created_at** | **datetime** |  | 
**deliveries_url** | **str** |  | [optional] 
**events** | **List[str]** | Determines what events the hook is triggered for. Default: [&#39;push&#39;]. | 
**id** | **int** | Unique identifier of the webhook. | 
**last_response** | [**HookResponse**](HookResponse.md) |  | [optional] 
**name** | **str** | The type of webhook. The only valid value is &#39;web&#39;. | 
**ping_url** | **str** |  | [optional] 
**test_url** | **str** |  | [optional] 
**type** | **str** |  | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


