# AppsUpdateWebhookConfigForAppRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to which the payloads will be delivered. | [optional] 
**content_type** | **str** | The media type used to serialize the payloads. Supported values include &#x60;json&#x60; and &#x60;form&#x60;. The default is &#x60;form&#x60;. | [optional] 
**secret** | **str** | If provided, the &#x60;secret&#x60; will be used as the &#x60;key&#x60; to generate the HMAC hex digest value for [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers). | [optional] 
**insecure_ssl** | [**WebhookConfigInsecureSsl**](WebhookConfigInsecureSsl.md) |  | [optional] 

## Example

```python
from github_openapi.models.apps_update_webhook_config_for_app_request import AppsUpdateWebhookConfigForAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppsUpdateWebhookConfigForAppRequest from a JSON string
apps_update_webhook_config_for_app_request_instance = AppsUpdateWebhookConfigForAppRequest.from_json(json)
# print the JSON string representation of the object
print(AppsUpdateWebhookConfigForAppRequest.to_json())

# convert the object into a dict
apps_update_webhook_config_for_app_request_dict = apps_update_webhook_config_for_app_request_instance.to_dict()
# create an instance of AppsUpdateWebhookConfigForAppRequest from a dict
apps_update_webhook_config_for_app_request_from_dict = AppsUpdateWebhookConfigForAppRequest.from_dict(apps_update_webhook_config_for_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


