# WebhookPingFormEncoded

The webhooks ping payload encoded with URL encoding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** | A URL-encoded string of the ping JSON payload. The decoded payload is a JSON object. | 

## Example

```python
from github_openapi.models.webhook_ping_form_encoded import WebhookPingFormEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPingFormEncoded from a JSON string
webhook_ping_form_encoded_instance = WebhookPingFormEncoded.from_json(json)
# print the JSON string representation of the object
print(WebhookPingFormEncoded.to_json())

# convert the object into a dict
webhook_ping_form_encoded_dict = webhook_ping_form_encoded_instance.to_dict()
# create an instance of WebhookPingFormEncoded from a dict
webhook_ping_form_encoded_from_dict = WebhookPingFormEncoded.from_dict(webhook_ping_form_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


