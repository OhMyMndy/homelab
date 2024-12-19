# ReposCreateWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Use &#x60;web&#x60; to create a webhook. Default: &#x60;web&#x60;. This parameter only accepts the value &#x60;web&#x60;. | [optional] 
**config** | [**ReposCreateWebhookRequestConfig**](ReposCreateWebhookRequestConfig.md) |  | [optional] 
**events** | **List[str]** | Determines what [events](https://docs.github.com/webhooks/event-payloads) the hook is triggered for. | [optional] [default to ["push"]]
**active** | **bool** | Determines if notifications are sent when the webhook is triggered. Set to &#x60;true&#x60; to send notifications. | [optional] [default to True]

## Example

```python
from github_openapi.models.repos_create_webhook_request import ReposCreateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateWebhookRequest from a JSON string
repos_create_webhook_request_instance = ReposCreateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateWebhookRequest.to_json())

# convert the object into a dict
repos_create_webhook_request_dict = repos_create_webhook_request_instance.to_dict()
# create an instance of ReposCreateWebhookRequest from a dict
repos_create_webhook_request_from_dict = ReposCreateWebhookRequest.from_dict(repos_create_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


