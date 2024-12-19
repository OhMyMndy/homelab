# WebhookConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | The media type used to serialize the payloads. Supported values include &#x60;json&#x60; and &#x60;form&#x60;. The default is &#x60;form&#x60;. | [optional] 
**insecure_ssl** | [**WebhookConfigInsecureSsl**](WebhookConfigInsecureSsl.md) |  | [optional] 
**secret** | **str** | If provided, the &#x60;secret&#x60; will be used as the &#x60;key&#x60; to generate the HMAC hex digest value for [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers). | [optional] 
**url** | **str** | The URL to which the payloads will be delivered. | [optional] 

## Example

```python
from github_openapi.models.webhook_config import WebhookConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookConfig from a JSON string
webhook_config_instance = WebhookConfig.from_json(json)
# print the JSON string representation of the object
print(WebhookConfig.to_json())

# convert the object into a dict
webhook_config_dict = webhook_config_instance.to_dict()
# create an instance of WebhookConfig from a dict
webhook_config_from_dict = WebhookConfig.from_dict(webhook_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


