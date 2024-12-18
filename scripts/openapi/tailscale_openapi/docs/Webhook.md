# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **str** | ID of the webhook endpoint.  | [optional] 
**endpoint_url** | **str** | The endpoint that events are sent to from Tailscale via POST requests.  | [optional] 
**provider_type** | **str** | The provider type for the webhook destination, or an empty string if none are applicable. Outgoing webhook events are sent in the format expected by the provider type if non-empty.  | [optional] 
**creator_login_name** | **str** | The login name for the creator of the webhook endpoint. In some cases, such as webhooks created with an OAuth client, this can be blank.  | [optional] 
**created** | **datetime** | The time the webhook endpoint was created.  | [optional] 
**last_modified** | **datetime** | The time the webhook endpoint was last modified.  | [optional] 
**subscriptions** | **List[str]** | The list of subscribed events that trigger POST requests to the configured endpoint URL. Learn more about [webhook events](/kb/1213/webhooks#events).  | [optional] 
**secret** | **str** | The webhook secret associated with the endpoint. Only populated on creation or when the secret is rotated.  This secret is used for generating the &#x60;Tailscale-Webhook-Signature&#x60; header in requests sent to the endpoint URL. Learn more about [verifying webhook event signatures](/kb/1213/webhooks#verifying-an-event-signature).  | [optional] 

## Example

```python
from tailscale_openapi.models.webhook import Webhook

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


