# WebhookSecretScanningAlertLocationCreatedFormEncoded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** | A URL-encoded string of the secret_scanning_alert_location.created JSON payload. The decoded payload is a JSON object. | 

## Example

```python
from github_openapi.models.webhook_secret_scanning_alert_location_created_form_encoded import WebhookSecretScanningAlertLocationCreatedFormEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecretScanningAlertLocationCreatedFormEncoded from a JSON string
webhook_secret_scanning_alert_location_created_form_encoded_instance = WebhookSecretScanningAlertLocationCreatedFormEncoded.from_json(json)
# print the JSON string representation of the object
print(WebhookSecretScanningAlertLocationCreatedFormEncoded.to_json())

# convert the object into a dict
webhook_secret_scanning_alert_location_created_form_encoded_dict = webhook_secret_scanning_alert_location_created_form_encoded_instance.to_dict()
# create an instance of WebhookSecretScanningAlertLocationCreatedFormEncoded from a dict
webhook_secret_scanning_alert_location_created_form_encoded_from_dict = WebhookSecretScanningAlertLocationCreatedFormEncoded.from_dict(webhook_secret_scanning_alert_location_created_form_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


