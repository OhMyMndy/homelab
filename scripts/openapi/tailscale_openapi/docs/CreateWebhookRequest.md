# CreateWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_url** | **str** | The endpoint that events are sent to from Tailscale via POST requests.  | 
**provider_type** | [**ProviderType**](ProviderType.md) |  | [optional] 
**subscriptions** | **List[str]** | The list of subscribed events that trigger POST requests to the configured endpoint URL. Learn more about [webhook events](/kb/1213/webhooks#events).  | 

## Example

```python
from tailscale_openapi.models.create_webhook_request import CreateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookRequest from a JSON string
create_webhook_request_instance = CreateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookRequest.to_json())

# convert the object into a dict
create_webhook_request_dict = create_webhook_request_instance.to_dict()
# create an instance of CreateWebhookRequest from a dict
create_webhook_request_from_dict = CreateWebhookRequest.from_dict(create_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


