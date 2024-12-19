# ReposUpdateWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**WebhookConfig**](WebhookConfig.md) |  | [optional] 
**events** | **List[str]** | Determines what [events](https://docs.github.com/webhooks/event-payloads) the hook is triggered for. This replaces the entire array of events. | [optional] [default to ["push"]]
**add_events** | **List[str]** | Determines a list of events to be added to the list of events that the Hook triggers for. | [optional] 
**remove_events** | **List[str]** | Determines a list of events to be removed from the list of events that the Hook triggers for. | [optional] 
**active** | **bool** | Determines if notifications are sent when the webhook is triggered. Set to &#x60;true&#x60; to send notifications. | [optional] [default to True]

## Example

```python
from github_openapi.models.repos_update_webhook_request import ReposUpdateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateWebhookRequest from a JSON string
repos_update_webhook_request_instance = ReposUpdateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateWebhookRequest.to_json())

# convert the object into a dict
repos_update_webhook_request_dict = repos_update_webhook_request_instance.to_dict()
# create an instance of ReposUpdateWebhookRequest from a dict
repos_update_webhook_request_from_dict = ReposUpdateWebhookRequest.from_dict(repos_update_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


