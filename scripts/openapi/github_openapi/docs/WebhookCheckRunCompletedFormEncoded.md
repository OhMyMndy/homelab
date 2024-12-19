# WebhookCheckRunCompletedFormEncoded

The check_run.completed webhook encoded with URL encoding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** | A URL-encoded string of the check_run.completed JSON payload. The decoded payload is a JSON object. | 

## Example

```python
from github_openapi.models.webhook_check_run_completed_form_encoded import WebhookCheckRunCompletedFormEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCheckRunCompletedFormEncoded from a JSON string
webhook_check_run_completed_form_encoded_instance = WebhookCheckRunCompletedFormEncoded.from_json(json)
# print the JSON string representation of the object
print(WebhookCheckRunCompletedFormEncoded.to_json())

# convert the object into a dict
webhook_check_run_completed_form_encoded_dict = webhook_check_run_completed_form_encoded_instance.to_dict()
# create an instance of WebhookCheckRunCompletedFormEncoded from a dict
webhook_check_run_completed_form_encoded_from_dict = WebhookCheckRunCompletedFormEncoded.from_dict(webhook_check_run_completed_form_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


