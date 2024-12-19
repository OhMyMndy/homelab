# WebhookCheckRunRequestedActionFormEncoded

The check_run.requested_action webhook encoded with URL encoding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** | A URL-encoded string of the check_run.requested_action JSON payload. The decoded payload is a JSON object. | 

## Example

```python
from github_openapi.models.webhook_check_run_requested_action_form_encoded import WebhookCheckRunRequestedActionFormEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCheckRunRequestedActionFormEncoded from a JSON string
webhook_check_run_requested_action_form_encoded_instance = WebhookCheckRunRequestedActionFormEncoded.from_json(json)
# print the JSON string representation of the object
print(WebhookCheckRunRequestedActionFormEncoded.to_json())

# convert the object into a dict
webhook_check_run_requested_action_form_encoded_dict = webhook_check_run_requested_action_form_encoded_instance.to_dict()
# create an instance of WebhookCheckRunRequestedActionFormEncoded from a dict
webhook_check_run_requested_action_form_encoded_from_dict = WebhookCheckRunRequestedActionFormEncoded.from_dict(webhook_check_run_requested_action_form_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


