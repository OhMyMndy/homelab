# ReposCreateWebhookRequestConfig

Key/value pairs to provide settings for this webhook.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to which the payloads will be delivered. | [optional] 
**content_type** | **str** | The media type used to serialize the payloads. Supported values include &#x60;json&#x60; and &#x60;form&#x60;. The default is &#x60;form&#x60;. | [optional] 
**secret** | **str** | If provided, the &#x60;secret&#x60; will be used as the &#x60;key&#x60; to generate the HMAC hex digest value for [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers). | [optional] 
**insecure_ssl** | [**WebhookConfigInsecureSsl**](WebhookConfigInsecureSsl.md) |  | [optional] 

## Example

```python
from github_openapi.models.repos_create_webhook_request_config import ReposCreateWebhookRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateWebhookRequestConfig from a JSON string
repos_create_webhook_request_config_instance = ReposCreateWebhookRequestConfig.from_json(json)
# print the JSON string representation of the object
print(ReposCreateWebhookRequestConfig.to_json())

# convert the object into a dict
repos_create_webhook_request_config_dict = repos_create_webhook_request_config_instance.to_dict()
# create an instance of ReposCreateWebhookRequestConfig from a dict
repos_create_webhook_request_config_from_dict = ReposCreateWebhookRequestConfig.from_dict(repos_create_webhook_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

